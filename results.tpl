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

        	<a class = "w3-btn w3-black" href = "./clusters"> By clusters</font> </a>
    		<a class = "w3-btn w3-black" href = "./words"> By words</font> </a>

		<div id="app-body">
		
		<div class="w3-container"> 
			<ul class="w3-ul w3-hoverable">
				% for (token, count) in elements_by_freq:

					<li> 
						<a class = "w3-button w3-block" href = "{{type}}/{{token}}"> 
							<font size = '5'> {{token}} </font> 
						 </a>
					</li>
				% end
			'</ul> 
		</div>
		</div>
    </body>



</html>
