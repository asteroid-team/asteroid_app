#Source separation 
On this page you will find examples related to the source separation task
(the overlapping speech of two speakers is separated).
  
The model ([DPRNNTasNet](https://arxiv.org/pdf/1910.06379.pdf)) was trained on [WHAM!](http://wham.whisper.ai/) with 8KHz data.
  
We randomly selected unseen data from WHAM! test set and processed it by the network to create examples.
  
Each example is composed of :
* `The mixture` The original wav file that will be fed to the network. The mixture is composed of 2 clean sources.
* `The sources`  The clean sources used to create the mixture.
* `The estimates` The outputs of the network.
  
