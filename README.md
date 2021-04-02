
Generate graphs with python networkx and display them with cytoscape.js.

Page reload generates a new graph.

Some useful Glitch starter info (modified from
[here](https://support.glitch.com/t/how-to-use-python-on-glitch/11201/9);
see also [this one](https://support.glitch.com/t/uploading-a-whole-folder/3128/4) and [this one](https://support.glitch.com/t/tutorial-how-to-install-any-package-from-apt-get-on-glitch/10954)):

- having a `requirements.txt` file puts Glitch into Python mode,
  installing libraries from requirements.txt and starting from `start.sh`

- having a `glitch.json` file puts Glitch into custom mode,
  installing and running whatever you've defined
  (see e.g. [glitch.com/~pyp5js-test](https://glitch.com/~pyp5js-test))

- having a `package.json` file puts Glitch into Node.js mode,
  see e.g. [glitch.com/~hello-dreams](https://glitch.com/~hello-dreams). This seems to be the most common way and
  has some extra support (see [this one](https://glitch.happyfox.com/kb/article/17-what-are-the-technical-restrictions-for-glitch-projects/))

- (having no backend at all is a way too, as in [glitch.com/~hello-basic](https://glitch.com/~hello-basic)).
