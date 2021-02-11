in this folder you will find examples related to the speech enhancement task
  (the speech of one speaker in a noisy environment is enhanced).
The model ([DPTNet](https://arxiv.org/pdf/2007.13975.pdf)) was trained on [LibriMix](https://arxiv.org/pdf/2005.11262.pdf) with 16Khz data.
  
We randomly selected unseen data from the [CHiME4](http://spandh.dcs.shef.ac.uk/chime_challenge/CHiME4/) dataset and processed it by the network to create examples.

The CHiMe4 dataset is composed of real noisy recording. Hence, it's not possible to compare the estimates to the clean sources
because they don't exist.
    
Each example is composed of :
* `The mixture` The original wav file that will be fed to the network. This mixture is a real utterance recorded in
  a noisy environment, hence no clean source is available.
* `The estimate` The output of the network.