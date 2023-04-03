=============
Installation
=============

This section shows how to install the package in order to reproduce our results.

From TestPyPi 
---------------------

As this is a toy project, the package was only deployed on TestPyPi and not PyPi. 

You can simply us 'pip' to install the full package.

1. First create a new virtual environment and activate it:
.. code:: sh
   $ python -m venv ~/myenv 
   $ source ~/myenv/bin/activate
.. include:: links.rst 

2. Install the package from TestPyPi with pip:
.. code:: sh
   $ pip install --extra-index-url https://test.pypi.org/simple src-bostonHousingWineQuality 
.. include:: links.rst 

3. Run the package:
.. code:: sh
   $ src-main	     # run the package with the standard configuration
   $ src-main --help # show help to see how to run the package with a different configuration
.. include:: links.rst 

Complete Installation
-----------------------

By proceeding this way, you won't be able to see the actual source code. If you want to access it, you can either check it out on github or clone the content to a local directory.

1. Clone the Github repository to a local directory and go to that new folder:
.. code:: sh
   $ git clone https://github.com/CedricLienhard/M05_miniProject.git
   $ cd M05_miniProject
.. include:: links.rst 

2. Create a new virtual environment and activate it:
.. code:: sh
   $ python -m venv ~/myenv 
   $ source ~/myenv/bin/activate
.. include:: links.rst 

3. Install all the necessary packages, which are listed in 2 .txt files:
.. code:: sh
   $ pip install -r requirements.txt
   $ pip install -r build-requirements.txt
.. include:: links.rst 

4. Run the main.py file, which is located in the 'src' folder:
.. code:: sh
   $ python -m src.main			# run the code with the standard configuration
   $ python -m src.main --help 	# show help to see how to run the code with a different configuration
.. include:: links.rst 

