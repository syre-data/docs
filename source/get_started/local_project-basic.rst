.. include:: <isonum.txt>

####################
Local Project: Basic
####################

Congratulations! You've just been hired as the head of the R+D department at Puzzles Underwater Fireworks company. The city's aquarium just hired us for their annual New Year's Eve extravaganza, and they want to do something extra special this year: fireworks for the fish. Luckily, our team has been working hard for the past six months on two new recipes for silent explosions. A perfect solution so the fish don't get scared. Looks like your first project will be to compare the two recipes to see which is quieter. Good Luck!

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

.. figure:: /_static/examples/fireworks/fireworks-tree.png
	:align: center
	:alt: Fireworks tree structure
	:figclass: align-center

	Project tree for the silent fireworks test.

****************************
Setting Up Your Project Tree
****************************

Local projects use your file system as a database. We will begin by making a folder for the project. Let's call it ``fireworks``. One of the main philosphies behind Thot is that data and analysis should be separate. Let's reflect this in our project by creating a ``data`` folder and a ``analysis`` folder.

We will build our project tree in two ways. First, we'll create the tree for Recipe A by hand, to get a sense of how Thot uses our folders as a database. And second, we will use Thot's Utilities package to build the tree for Recipe B, automating the process.

Recipe A
========

Move into the ``data`` folder. Here we will add a file called ``_container.json``. Adding this file to a folder tells Thot that this folder is a Container. What do Containers do? Well, they Contain things. Namely, they can contain other Containers, Assets, and Script Associations. We'll get to the Assets and Script Associations later on.

.. code-block:: JSON
	:caption: _container.json

	{
		"name": "Silent Fireworks",
		"type": "project",
		"description": "Determining whether recipe A or B is quieter."
	}

.. note::
	JSON is a very strict format. Make sure everything is double quoted and there are no stray commas.

Great! the ``data`` folder is now considered the ``root`` of our project because it is the highest Container. Now let's add the Container for Recipe A. Make a folder called ``recipe-a`` and add a ``_container.json`` file to it.

.. code-block:: JSON
	:caption: recipe-a/_container.json
	
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
	:caption: recipe-a/batch-1/_container.json
	
	{
		"name": "Batch 1",
		"type": "batch",
		"metadata": {
			"batch": 1
		}
	}

.. code-block:: JSON
	:caption: recipe-a/batch-2/_container.json
	
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
	
	# For Mac and Linux
	python -m thot.utilities add_containers --search '{ "type": "project" }' --containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "b" } } }'

	# For Windows
	python -m thot.utilities add_containers --search "{ \"type\": \"project\" }" --containers "{ \"recipe-b\": { \"name\": \"Recipe B\", \"type\": \"recipe\", \"metadata\": { \"recipe\": \"b\" } } }"


.. note::
	Windows does not interpret single quotes (') in the command line, so only double quotes can be used ("). Thus, to enclose strings double quotes must be used, and any double quotes inside the strings must be escaped with a backslash (\\).

	To convert from the Mac and Linux syntax to the Windows syntax, first escape all double quotes with a backslash ( ``"`` |rarr| ``\"``), then convert all single quotes into double quotes (``'`` |rarr| ``"``).

	Throughout this tutorial the Mac and Linux command line syntax will be used, with some examples of the change for Windows. However, it is assumed after the first few examples, you can make the necessary adjustments to the examples yourself.

Let's see what this is doing. :code:`python -m thot.utilities` will run the Utilities for us. Next we pass in the tool we want to use :code:`add_containers`. We then tell the tool which Container we want to add the new Containers to :code:`--search '{ "type": "project" }'`. Finally, we describe the Container we want to add :code:`--containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "a" } } }'`.

This should have added a new folder to your project called ``recipe-b`` with the ``_container.json`` file already filled out. That didn't save us that much time, though. The real power comes when we need to add multiple Containers across our project. Let's try the same thing with the batches. 

.. code-block:: bash
	
	# For Mac and Linux
	python -m thot.utilities add_containers --search '{ "name": "Recipe B" }' --containers '{ "batch-1": { "name": "Batch 1", "type": "batch", "metadata": { "batch": 1 } }, "batch-2": { "name": "Batch 2", "type": "batch", "metadata": { "batch": 2 } } }'

	# For Windows
	python -m thot.utilities add_containers --search "{ \"name\": \"Recipe B\" }" --containers "{ \"batch-1\": { \"name\": \"Batch 1\", \"type\": \"batch\", \"metadata\": { \"batch\": 1 } }, \"batch-2\": { \"name\": \"Batch 2\", \"type\": \"batch\", \"metadata\": { \"batch\": 2 } } }"

If you inspect one of the new ``_container.json`` files you'll notice many more properties than the ones we've explored so far. 

Great! Our project's structure is now complete, and we can start adding data to it. The final folder structure should be as below.
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

.. only:: builder_html or readthedocs

	:download:`Click Here to download this project step. </_static/examples/fireworks/project_steps/00-tree/project/project.zip>`

***************************
Adding Data to Your Project
***************************
Now that we have our tree, we can add data. Most often data is added to the lowest level Containers in our project, because these are the things we actually run experiments on. Luckily our researchers just finished up with their experiments and have provided you with the download link. 

.. only:: builder_html or readthedocs

	:download:`Click Here to download the results. </_static/examples/fireworks/project_steps/01-assets/experiment_data/data.zip>`

In Thot, any data files that we want to analyze -- CSV, text, images, binary, anything -- is called an Asset. Similar to Containers, an Asset is a folder with an ``_asset.json`` file in it. Let's create these Assets using Thot's Utilities. 

We want to add our Assets to the batches. Let's do the first by hand, then the rest using the Utilities. 

#. Navigate to the **Recipe A > Batch 1** folder. 
#. Create a new folder, calling it ``noise_data``.
#. Add an ``_asset.json`` file to the ``noise_data`` folder with the following content:

.. code-block:: JSON
	:caption: recipe-a/batch-1/noise_data/_asset.json

	{
		"name": "Noise Data",
		"type": "noise-data",
		"file": "data.csv"
	}


You'll notice this was almost the same as creating the Containers, with one major change: the ``file`` field. This should point to the data file of the Asset, in our case ``data.csv``. From the experiment results, copy the ``recipe_a-batch_1.csv`` file into the Asset folder, and rename it to ``data.csv``. Great! we just made our first Asset. Doing this by hand, though, can be tedious, so let's see how to automate it.

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

.. only:: builder_html or readthedocs

	:download:`Click Here to download this project step. </_static/examples/fireworks/project_steps/01-assets/project/project.zip>`

******************
Analyzing the Data
******************

Now for the fun to start! Let's create our first analysis script. Create a new file in the ``analysis`` folder called ``noise_stats.py``. Copy and paste the following code into the file.

.. literalinclude:: /_static/examples/fireworks/project_steps/02-analysis/project/analysis/noise_stats.py
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
	:caption: recipe-a/batch-1/_script.json

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

.. only:: builder_html or readthedocs

	:download:`Click Here to download this project step. </_static/examples/fireworks/project_steps/02-analysis/project/project.zip>`

Moving On Up
============

Now that we have the statistics for each of our batches we can move up one level in our project tree to compile the statistics for each recipe. Let's first make the analysis script calling it ``recipe_stats.py``.

.. literalinclude:: /_static/examples/fireworks/project_steps/03-moving_up/project/analysis/recipe_stats.py
	:language: python
	:caption: recipe_stats.py
	:linenos:

Let's look at some of the new things we did here:

+ **line 9:** Get the Container the script is running in. In this case it will be Recipe A and Recipe B.

+ **line 12:** When analyzing the batches we only had one Asset we wanted to use, so used the ``find_asset()`` method. Now we want to pull in both ``noise_stats`` Assets, so use the ``find_assets()`` method, which returns a list of Assets that match the criteria. Also notice that the ``noise_stats`` aren't in the Recipe Containers directly, but are in the batch children Containers. This highlights a very important point: **Containers have access to their Assets as well as all their childrens' Assets.**

+ **line 16-23:** Iterate over each ``noise_stats`` Asset, creating a Pandas DataFrame from it, and adding it to the data list to be combined in line 27.

+ **line 37:** Use the name of the Container as part of the name for the new Asset. 

+ **line 43:** Export the new Asset, this time as a pickle (.pkl) file. This is a binary format used by Pandas to store DataFrames, making importing them later on easier.

Let's add this new script to run on our recipe Containers, and then run it. From the project root run

.. code-block:: bash

	python -m thot.utilities add_scripts -s '{ "type": "recipe" }' --scripts '{ "script": "root:/../analysis/recipe_stats.py" }'

	python -m thot.runner

Let's build our final analysis script now so we can see which recipe is better. In the analysis folder create the ``recipe_comparison.py`` script.

.. literalinclude::  /_static/examples/fireworks/project_steps/03-moving_up/project/analysis/recipe_comparison.py
	:language: python
	:caption: recipe_comparison.py
	:linenos:

Let's breakdown the new concepts:

+ **line 14:** Use the recipe metadata from the Asset to name the data.

+ **line 28, 44:** We;ve already seen that we can pull in multiple Assets into our scripts. here we also see that we can create multiple Assets in a single script. Also notice that one Asset is a CSV text file, while the other is a PNG image file. Assets can be any sort of file.

Add the proper Script Association (``_scripts.json``) to the root folder, and analyze the project. Take a look at the Assets we created so we know which recipe is quiter.

Congratulations! You just built your first Thot project, building it from scratch and analyzing the data to come to a final conclusion. We've only touched on the functionality of Thot, and with such a small project it's hard to get a sense of the power thot gives you in analyzing larger projects. To learn more about this you can go through the advanced tutorial (coming soon) and learn even more.

.. only:: builder_html or readthedocs

	:download:`Click Here to download the final project. </_static/examples/fireworks/project_steps/03-moving_up/project/project.zip>`

*******
Summary
*******

In this tutorial you learned how to build a local Thot project by creating a folder structure and adding ``_container.json`` files to create Containers. We then added data to our project by creating Assets using ``_asset.json`` files which point to their data file. Then we learned how to write an analysis script. We used Thot to pull in the data we wanted and used properties of the Asset. Finally, we created ``_scripts.json`` files to create Script Associations between Containers and the scripts to run on them.

Cheat Sheets
============

Here are the most important concepts and commands we learned through this tutorial.

+ The ``root:`` directive points to the project root.

Containers
----------

+ A Conatainer is a folder with a ``_container.json`` file in it. Containers can container other Containers, Assets, and Script Associations.

.. code-block:: JSON
	:caption: Basic ``_container.json`` file.
	
	{
		"name": "My Container",
		"type": "basic-container",
		"description": "A basic Container example.",
		"metadata": {
			"string_metadata": "I am a string",
			"number_metadata": 42,
			"boolean_metadata": true,
			"json_metadata": {
				"another_number": 2.71828
			}
		}
	}

+ Add children Containers to the matched search Containers.

.. code-block:: bash
	:caption: Adding children Containers.

	python -m thot.utilities add_containers --search '{ "type": "parent-container" }' --containers '{ "container_1": { "name": "Container 1", "type": "child-container" }, "container 2": { "name": "Container 2", "type": "child-container" }  }'

Assets
------

+ An Asset is a folder with an ``_asset.json`` file in it. Assets represent pieces of data in your project.

.. code-block:: JSON
	:caption: Basic ``_asset.json`` file.

	{
		"name": "My Asset",
		"type": "basic-asset",
		"description": "A basic Asset example.",
		"metadata": {
			"more_metadata": true
		},

		"file": "path/to/file.csv"
	}

+ Add Assets to the matched Containers.

.. code-block:: bash
	:caption: Add Assets.
	
	python -m thot.utilities add_assets --search '{ "type": "basic-container" }' --assets '{ "new_asset": { "name": "New Asset", "file": "data.pkl" } }'

Script Associations
-------------------

+ Script Associations are added to Containers in the ``_scripts.json`` file.

.. code-block:: JSON
	:caption: Basic ``_scripts.json`` file.

	[
		{
			"script": "path/to/script.py"
		},
		{
			"script": "root:/path/to/another.py"
		}
	]

+ Add Script Associations to the matched Containers.

.. code-block:: bash
	:caption: Add Script Associations.

	python -m thot.utilities add_scripts --search '{ "type": "basic-container" }' --scripts '{ "script": "path/to/script.py" }'

+ Set Script Associations of the matched Containers.

.. code-block:: bash
	:caption: Set Script Associations.

	python -m thot.utilities set_scripts --search '{ "type": "basic-container" }' --scripts '[ { "script": "path/to/script.py" }, { "script": "root:/path/to/another.py" } ]'


Analysis
--------

+ To initialize a local Thot project in your script.

.. code-block:: python
	:caption: Initialize a local Thot project.

	from thot.thot import LocalProject
	thot = LocalProject()

+ Finding Containers and Assets.

.. code-block:: python
	:caption: Finding Containers and Assets.

	container  = thot.find_container(  { 'name': 'Basic Container' } )
	containers = thot.find_containers( { 'type': 'basic-container' } )

	asset  = thot.find_asset(  { 'name': 'Basic Asset' } )
	assets = thot.find_assets( { 'type': 'basic-asset' } )

+ Getting the information from a Container or Asset is the same.

.. code-block:: python
	:caption: Getting information from Containers and Assets.

	file_path = asset.file
	container_name = container.name

	is_boolean    = container.metadata[ 'booean_metadata' ]
	nested_number = container.metadata[ 'json_metadata' ][ 'another_number' ]

+ Analyze the project.

.. code-block:: bash
	:caption: Analyzing a project.
	
	python -m thot.runner





