<html>
    <head>
   	 <script language="javascript" src="http://code.jquery.com/jquery-1.4.2.min.js"></script>
        <meta charset="utf-8">
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

        <title>LM clusters visualization</title>


	<style>


	.tooltip {
	  position: relative;
 	 display: inline-block;
 	 border-bottom: 1px dotted black;
  	z-index: 100;
	}

	.tooltip .tooltiptext {
	  visibility: hidden;
 	 width: 720px;
 	 background-color: black;
  	 color: white;
  	 text-align: left;
  	 border-radius: 6px;
 	 padding: 5px 0;

 	 /* Position the tooltip */
 	 position: absolute;
 	 margin-left:+150px;
 	 margin-top: -100px;
 	 z-index: 100;
 	top: -50px;
  	left: 105%; 
	}

	.tooltip:hover .tooltiptext {
	  visibility: visible;
	}
	
	</style>


    </head>
	

    <body>
        	<a class = "w3-btn w3-black" href = "../clusters"> By clusters</font> </a>
    		<a class = "w3-btn w3-black" href = "../words"> By words</font> </a>
    		
		<div id="app-body">
		<%
		title = "word" if type == "words" else "cluster"
		opposite = "cluster" if title == "word" else "word"
		opposite_url = opposite + "s"
		token2occurrences = sorted(token2occurrences, key = lambda token_and_contexts: -len(token_and_contexts[1]))
		%>
		
		<p> <font size = '7'> {{title}} : {{token}} </font> </p>
		<div class="w3-container"> 
			<ul class="w3-ul w3-hoverable">
			% for (cooccurring_elem, contexts) in token2occurrences:
				% w = token if title == "word" else cooccurring_elem
				% size = len(contexts)

				<li> <div class="tooltip">
					<a class = "w3-button w3-block" href = "../{{opposite_url}}/{{cooccurring_elem}}">  <font size = 5> {{opposite}}: {{cooccurring_elem}} </font>  <br> <font size = 3> #co-occurrences: {{size}} </font> </a>

				<span class="tooltiptext"> 
				<ul>
				
				% for j in range(min(12, len(contexts))):
				
					<%
					context = contexts[j].split(" ")
					w_index = context.index(w)
					left = " ".join(context[:w_index])
					right = " ".join(context[w_index + 1:])
					%>
					
					<li>...{{left}} <span color = 'red'> <font size = '5'> {{w}} </font> </span> {{right}} ...</li>
				% end
				</ul>
				</span>
				</div> </li>
			% end
			</ul>
		</div>
				

		
		</div>
    </body>



</html>
