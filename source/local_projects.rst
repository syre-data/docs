##############
Local Projects
##############

Congratualations on being hired as the head of the R+D department at Puzzles Underwater Fireworks company. The city's aquarium just hired us for their annual New Year's Eve extravaganza, and they want to do something extra special this year: firewoks for the fish. Luckily, our team has been working hard for the past six months on two new recipes for silent explosions. A perfect solution so the fish don't get scared. Looks your first project will be to compare the two recipes to see which is quieter. Good Luck!

************
Getting Thot
************

Thot requires Python (v3) which you can get from the `official Python site <https://www.python.org/downloads/>`_. After installing Python, you can install Thot by running

.. code-block:: bash

	python -m pip install thot-data


.. note::
	We will use Pandas for the analysis. To get Pandas you can `visit their website  <https://pandas.pydata.org/getting_started.html>`_.


***********************
Organizing Your Project
***********************

The first thing we need to do is organize our project. Thot uses a tree structure to organize your projects, giving your project different levels. The top level should be the most important grouping to you, becoming less important as you move down the tree. 

For this project the most important thing we need to test is which recipe is quieter, so out top level grouping will be the recipes. Unfortunately, testing underwater fireworks happens to be quite expensive, so we will only be able to make two batches for each recipe. The batches will be our second level. This gives us the tree in :numref:`Fig. %s <local_project_organization>`

.. _local_project_organization:

.. figure:: _static/examples/fireworks/fireworks-tree.png
	:align: center
	:alt: Fireworks tree structure
	:figclass: align-center

	Project tree for the silent fireworks test.

****************************
Setting Up Your Project Tree
****************************

Local projects use your file system as a database. We will begin by making a folder for the project. Let's call it ``silent_fireworks``. One of the main philosphies behind Thot is that data and analysis should be separate. Let's reflect this in our project by creating a ``data`` folder and a ``analysis`` folder.

We will build our project tree in two ways. First, we'll create the tree for Recipe A by hand, to get a sense of how Thot uses our folders as a database. And second, we will use Thot's Utilities package to build the tree for Recipe B, automating the process.

Recipe A
========

Move into the ``data`` folder. Here we will add a file called ``_container.json``. Adding this file to a folder tells Thot that this folder is a Container. What do Containers do? Well, they Contain things. Namely, they can contain other Containers, Assets, and Script Associations. We'll get to the Assets and Script Associations later on.

.. code-block:: JSON
	:caption: /_container.json

	{
		"name": "Silent Fireworks",
		"type": "project",
		"description": "Determining whether recipe A or B is quieter."
	}

.. note::
	JSON is a very strict language. Make sure everything is double quoted and there are no stray commas.

Great! the ``data`` frler is now considered the ``root`` of our project because it is the highest Container. Now let's add the Container for Recipe A. Make a folder called ``recipe-a`` and add a ``_container.json`` file to it.

.. code-block:: JSON
	:caption: /recipe-a/_container.json
	
	{
		"name": "Recipe A",
		"type": "recipe",
		"metadata": {
			"recipe": "a"
		}
	}

.. note::
	When naming files and folders avoid using spaces. Use underscores (_) or hyphens (-) instead.

Notice that we didn't include the ``description`` data in the Container file for Recipe A. If we're not going to use a field, we can just leave it out. We also added a new ``metadata`` field. This allows us to attach data to our data. Children Containers will inherit the metadata from their ancestors, but can overwrite it by declaring a new value with the same name.

On to the batches. From the Recipe A Container, make two new folders called ``batch-1`` and ``batch-2`` and make them Containers.

.. code-block:: JSON
	:caption: /recipe-a/batch-1/_container.json
	
	{
		"name": "Batch 1",
		"type": "batch",
		"metadata": {
			"batch": 1
		}
	}

.. code-block:: JSON
	:caption: /recipe-a/batch-2/_container.json
	
	{
		"name": "Batch 2",
		"type": "batch",
		"metadata": {
			"batch": 2
		}
	}

Your folder tree should now look like this
::

	silent_fireworks
	|-- data
	|	|__ recipe-a
	|		|-- _container.json
	|		|-- batch-1
	|		|	|__ _container.json
	|		|__ batch-2
	|			|__ _container.json
	|__ analysis

Recipe B
========

Now that we have the hang of making Containers by hand, let's speed up the process and automate it. To do this we'll use Thot's Utilities. Open up a terminal or command line and navigate to the project root (``data`` folder). Enter the command

.. code-block:: bash
	
	python -m thot.utilities add_containers --search '{ "type": "project" }' --containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "b" } } }'

.. warning::
	If you are on a Windows machine Thot's Utilities do not currently work.

Let's see what this is doing. :code:`python -m thot.utilities` will run the Utilities for us. next we pass in the tool we want to use :code:`add_containers`. We then tell the tool which Container we want to add the new Containers to :code:`--search '{ "type": "project" }'`. Finally, we describe the Container we want to add :code:`--containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "a" } } }'`.

This should have added a new folder to your project called ``recipe-b`` with the ``_container.json`` file already filled out. That didn't save us that much time, though. The real power comes when we need to add multiple Containers across our project. Let's try the same thing with the batches. 

.. code-block:: bash
	
	python -m thot.utilities add_containers --search '{ "name": "Recipe B" }' --containers '{ "batch-1": { "name": "Batch 1", "type": "batch", "metadata": { "batch": 1 } }, "batch-2": { "name": "Batch 2", "type": "batch", "metadata": { "batch": 2 } } }'

If you inspect one of the new ``_container.json`` files you'll notice many more properties than the ones we've explored so far. 

Great! We've now finished out 
::

	silent_fireworks
	|-- data
	|	|-- recipe-a
	|	|	|-- _container.json
	|	|	|-- batch-1
	|	|	|	|__ _container.json
	|	|	|__ batch-2
	|	|		|__ _container.json
	|	|__ recipe-b
	|		|-- _container.json
	|		|-- batch-1
	|		|	|__ _container.json
	|		|__ batch-2
	|			|__ _container.json
	|__ analysis

.. only:: builder_html

	:download:`Click Here to download this project step. <_static/examples/fireworks/project_steps/00-tree/project/project.zip>`

***************************
Adding Data to Your Project
***************************
Now that we have our tree, we can add data. Most often data is added to the lowest level Containers in our project, because these are the things we actually run experiments on. Luckily our researchers just finished up with their experiments and have provided you with the download link. 

.. only:: builder_html

	:download:`Click Here to download the results. <_static/examples/fireworks/project_steps/01-assets/experiment_data/data.zip>`

In Thot, any data files that we want to analyze -- CSV, text, images, binary, anything -- is called an Asset. Similar to Containers, an Asset is a folder with an ``_asset.json`` file in it. Let's create these Assets using Thot's Utilities. 

We want to add our Assets to the batches. Let's do the first by hand, then the rest using the Utilities. 

#. Navigate to the **Recipe A > Batch 1** folder. 
#. Create a new folder, calling it ``noise_data``.
#. Add an ``_asset.json`` file to the ``noise_data`` folder with the following content:

.. code-block:: JSON
	:caption: /recipe-a/batch-1/noise_data/_asset.json

	{
		"name": "Noise Data",
		"type": "noise-data",
		"file": "data.csv"
	}


You'll notice this was almost the same as creating the Containers, with one major change: the ``file`` field. This should point to the data file of the Asset, in our case ``data.csv``. From the experiment results, copy the ``recipe_a-batch_1.csv`` file into the Asset folder, and rename it to ``data.csv``. Great! we just made our first Asset. Doing this by hand, though, can be tedious, so let's see hwo to automate it.

From the project root (``data`` folder) run

.. code-block:: bash

	python -m thot.utilities add_assets --search '{ "type": "batch" }' --assets '{ "noise_data": { "name": "Noise Data", "type": "noise-data", "file": "data.csv" } }'

This will add three new Assets to your project. You can examine one of these new Assets to see all the available fields. Let's add the rest of the data from the experiment results to their respective Assets. Remember to rename the data files to ``data.csv`` to match the ``file`` field. This will make your file tree look like the one below.
::

	silent_fireworks
		|-- data
		|	|-- recipe-a
		|	|	|-- _container.json
		|	|	|-- batch-1
		|	|	|	|-- _container.json
		|	|	|	|__ noise_data
		|	|	|		|-- _asset.json
		|	|	|		|__ data.csv
		|	|	|__ batch-2
		|	|		|-- _container.json
		|	|		|__ noise_data
		|	|			|-- _asset.json
		|	|			|__ data.csv
		|	|__ recipe-b
		|		|-- _container.json
		|		|-- batch-1
		|		|	|-- _container.json
		|		|	|__ noise_data
		|		|		|-- _asset.json
		|		|		|__ data.csv
		|		|__ batch-2
		|			|-- _container.json
		|			|__ noise_data
		|				|-- _asset.json
		|				|__ data.csv
		|__ analysis

.. only:: builder_html

	:download:`Click Here to download this project step. <_static/examples/fireworks/project_steps/01-assets/project/project.zip>`

******************
Analyzing the Data
******************

Now for the fun to start! Let's create our first analysis script. Create a new file in the ``analysis`` folder called ``noise_stats.py``. Copy and paste the following code into the file.

.. literalinclude:: _static/examples/fireworks/project_steps/02-analysis/project/analysis/noise_stats.py
	:language: python
	:caption: noise_stats.py
	:linenos:

Let's go through and break down what each chunk of code is doing.

.. TODO [5]: Format table
.. .. list-table::
.. 	:class: fixed-width
.. 	:header-rows: 1

.. 	* - Line No.
.. 	  - Description
.. 	* - 2-3
.. 	  - Import the packages we're goin to use, namely Pandas and Thot. In this case we only need to use a small part: LocalProject.
.. 	* - 6
.. 	  - Initialize the Thot project, giving us access to all the data stored within it.
.. 	* - 9
.. 	  - Find the Noise Data Asset we made for each batch by search for Assets who have a ``type`` of 'noise-data'.
.. 	* - 12
.. 	  - Load the noise data into a Pandas DataFrame.
.. 	* - 15
.. 	  - Compute statistics on the noise data.
.. 	* - 18-24
.. 	  - Create a new Asset to store the noise statistics in. Notice that the ``stats_properties`` dictionary we pass in mimics exactly the structure of the ``_asset.json`` files we created earlier. ``thot.add_asset()`` accepts as it's second argument an ``_id`` for the new Asset.
.. 	* - 27
.. 	  - Save the statistics to the new Asset.


+ **lines 2-3:** Import the packages we're goin to use, namely Pandas and Thot. In this case we only need to use a small part: LocalProject.

+ **line 6:** Initialize the Thot project, giving us access to all the data stored within it.

+ **line 9:** Find the Noise Data Asset we made for each batch by search for Assets who have a ``type`` of 'noise-data'.

+ **line 12:** Load the noise data into a Pandas DataFrame.

+ **line 15:** Compute statistics on the noise data.

+ **lines 18-24:** Create a new Asset to store the noise statistics in. Notice that the ``stats_properties`` dictionary we pass in mimics exactly the structure of the ``_asset.json`` files we created earlier. ``thot.add_asset()`` accepts as it's second argument an ``_id`` for the new Asset.

+  **line 27:** Saves the statistics to the new Asset.

Now we need to tell Thot which Containers to run this script from. This is done by creating Script Associations. We'll start off again creating one by hand, then see how to automate the process using the Utilities.


Navigate to the **Recipe A > Batch 1** Container. We create Script Associations by placing a ``_scripts.json`` file in a Container. Go ahead and create this file and paste the contents below inside it.

.. code-block:: JSON

	[
		{
			"script": "root:/../analysis/noise_stats.py"
		}
	]

This tells Thot to run the ``noise_stats.py`` script from this Container. The ``script`` field is the path to the script to run, it can be a relative or absolute path. The special ``root:`` directive points to the project root.

Before adding the script to the rest of the batches, let's try it out.

.. code-block:: bash
	
	python -m thot.runner

You should see the ``noise_stats`` Asset be added to the folder. Great! Now let's make it so we analyze all the batches. Navigate to the project root (``data`` folder) and run

.. code-block:: bash
	
	python -m thot.utilities set_scripts -s '{ "type": "batch" }' --scripts '[ { "script": "root:/../analysis/noise_stats.py" } ]'

You'll notice that we replaced the ``--search`` flag from the previous command like this with the ``-s`` flag. The two are synonyms for each other, ``-s`` just giving us a shorthand for ``--search``. 

Now let's analyze the entrie project by running ``python -m thot.runner`` again. This will create a new Noise Statistics Asset for each of the batches.

.. only:: builder_html

	:download:`Click Here to download this project step. <_static/examples/fireworks/project_steps/02-analysis/project/project.zip>`

Moving On Up
============

Coming soon...


.. 	