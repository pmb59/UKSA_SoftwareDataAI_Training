===================
Notebooks on Python
===================

In this file you'll find two introductory notebooks on python. These will guide you through the basic syntax, through operations including on matrices, loops, conditionals, the numpy and pandas packages and indexing.  These notebooks can be run in your own jupyter lab environment or you can also use `google colab <https://colab.research.google.com>`_ . 

If you are working on a work computer or another resource where installing packages is not easy we would reocmmend using google colab to view these notebooks. Please note that to complete the course you will not need to install python packages to your own machiene as computational resouces will be provided for you on our cluster.  You will only need your sign-in details to access this. 

To open these notebooks in google colab:

  1. click on the .ipynb file you wish to open - this will open another github page where you will see the notebook
  2. click the button on the top right hand corner of the opened notebook which says 'download raw file' - the icon for this looks like a down arrow over a line - make sure that you file is a .ipynb not an .html file
  3. open google colab here: `google colab <https://colab.research.google.com>`_ 
  4. on the 'open notebook' screen, click upload and find the downloaded file on your computer.
  5. To run cells in the notebook you can use the button 'runtime' or you can press shift+enter in each cell. 

--------------------------------
Python installation and packages
--------------------------------

The easist way to install python and python packages are through a system package manager. 

* Conda

Conda is system package manager which works cross platform, it is not limited to Python.  A Conda ‘channel’  is the path Conda uses to find and install software packages. Conda is free but the python defaults package manager Anaconda is no longer free for all use (whilst this is a training course will we endeavour to use software that is as open and flexible as possible). Please see this blog to understand more. 

* `Mamba <https://mamba.readthedocs.io/en/latest/>`_

Mamba is a rewrite of Conda (still free and open source) which is quicker at resolving dependencies.  Micromamba is mamba in a single binary.  This makes installation and maintenance easier.  We will use micromamba. 

* Pip

Pip is a python package manager it installs packages which are in the python package index (PyPI). We will also use pip btu we will get mamba to install it.

^^^^^^^^^^
Installing
^^^^^^^^^^

Installing Micromamba on your machine Navigate to the micromamba install webpage: https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#umamba-install 

Follow the instructions for your machine - see also slide summaries on the moodle page. 

Once micromamba is installed you can use the shell script and yaml file provided for this course to install all the relevant packages including the jupyter lab envionment. 

