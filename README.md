# LM_visualization

This program visaulizes the learned states of a trained language model. A neural LM was trained until perplexity of ~75.5, and
its state were clsutered into to K=750 discrete clusters using the k-means algorithm. The program allows you to inspect: 

(1) Which words were clustered together into a single cluster; <br />
(2) In which clusters a given word is included; <br/>
(3) Contexts in which the word appeared, in a given cluster. <br/>

Running
------

Running requires python3 and [bottle](https://bottlepy.org/docs/dev/) (`pip3 install bottle`). `python3 main.py` would initialize the server, and the visualization is
then avaialble at `http://localhost:8080/`.
