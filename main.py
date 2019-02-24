#http://localhost:8080/static/index2.html

from bottle import route, run, template, static_file, get, post
from collections import defaultdict, Counter
import json
import os

def read_file(fname):

	with open(fname, "r") as f:

		lines = f.readlines()

	elements = [line.strip() for line in lines][:]
	return elements


def by_freq(data):

	
	c = Counter(data)
	items = c.items()
	items = sorted(items, key = lambda tup: -tup[1])
		
	return [(clean(item),count) for (item, count) in items]

def calculate_cluster_word_entropy(cluster_words):

	raise NotImplementedError
	

def clean(s):

	return s.replace("<S>", "*START*").replace("<E>", "*END*").replace('"', '"').replace("'", '"').replace('/', "SLASH").replace("``", '"').replace("<unk>", "UNK")
	


def chop_context(context):
	w_index = int(len(context) / 2) 
	start_index = context.index("<S>") if ("<S>" in context) else 0
	end_index = (len(context) - context[::-1].index("<E>")) if "<E>" in context else len(context)
	
	if end_index <= w_index:
		end_index = len(context) 
	if start_index > w_index:
		start_index = 0
		
	return context[start_index:end_index]

def to_json(states_in_order, words_in_order, window_size = 17):

	state2words = defaultdict(dict)
	words2states = defaultdict(dict)
	clust_counter = defaultdict(Counter)
	word_counter = defaultdict(Counter)
	
	seen_contexts = set()
	count = 0
	
	for i, (w, clust) in enumerate(zip(words_in_order, states_in_order)):

		#if len(w) <=1: continue
				
		w = clean(w)

		context = words_in_order[max(i - int(window_size/2),0): min(i + int(window_size/2), len(words_in_order))]		
		context = chop_context(context)
		context = clean(" ".join(context))

			
		if "words" not in state2words[clust]: state2words[clust]["words"] = defaultdict(list)
		if "clusters" not in words2states[w]:  words2states[w]["clusters"] = defaultdict(list)
		
		if context not in seen_contexts:
				state2words[clust]["words"][w].append(context)
				words2states[w]["clusters"][clust].append(context)
				word_counter[clust][w] += 1
				clust_counter[w][clust] += 1
				
				seen_contexts.add(context)

	
	for clust in state2words.keys():
		state2words[clust]["size"] = sum(word_counter[clust].values())
			
	for w in words2states.keys():
		words2states[w]["size"] = sum(clust_counter[w].values())
	
	return state2words, words2states

"""
@route('/static/:filename#.*#')
def server_static(filename="index2.html"):
	return static_file(filename, root = './')
"""

#@route('/status/')
#@route('/status/filename#.*#')
@route('/')
def server_static(filename='index.html'):
    return static_file(filename, root='./')

@get('/words') # or @route('/login')
def get_words():

	return json.dumps(words_by_freq[:])
	"""
	s = ['<ul class="w3-ul w3-hoverable">']
		
	for w in words_by_freq[:1000]:
 	
 		s.append('<li>' + w + '</li>')
	s.append('</ul>')
 	
	s = " ".join(s)
	return s
	"""
	
@get('/clusters') # or @route('/login')
def get_clusters():

	return json.dumps(clusts_by_freq)


@get('/words') # or @route('/login')
def get_words():

	return json.dumps(words_by_freq)

	
@route('/words/<word>')
def get_word(word):

	return json.dumps(words2states[word]["clusters"])

@route('/clusters/<clust>')
def get_cluster(clust):

	return json.dumps(state2words[clust]["words"])

if __name__ == '__main__':

	print("Loading data...")
	clusts, words = read_file("data/ordered_clusts.txt"), read_file("data/ordered_words.txt")
	clusts_by_freq, words_by_freq = by_freq(clusts), by_freq(words)
	state2words, words2states = to_json(clusts, words)
	print("Done.")
	run(host='localhost', port=8080)
