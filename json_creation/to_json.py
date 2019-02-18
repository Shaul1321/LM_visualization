from collections import defaultdict
from collections import Counter
import json

def read_file(fname):

	with open(fname, "r") as f:

		lines = f.readlines()

	elements = [line.strip() for line in lines][:]
	return elements


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

		if len(w) <=1: continue
				
		
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
	
	state2words_json = json.dumps(state2words)
	words2states_json = json.dumps(words2states)
	
	with open("../view/states2words.json", "w") as f:

		f.write(state2words_json)
		
	with open("../view/words2states.json", "w") as f:

		f.write(words2states_json)
if __name__ == "__main__":
	to_json(read_file("../data/clusts.txt"), read_file("../data/words.txt"))
