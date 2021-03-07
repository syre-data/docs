.. include:: <isonum.txt>

***********************
Organizing Your Project
***********************

The first thing we need to do is organize our project. Thot uses a tree structure to organize your projects, giving your project different levels. The top level should be the most important grouping to you, becoming less important as you move down the tree. 

For this project the most important thing we need to test is which recipe is quieter, so our top level grouping will be the recipes. Unfortunately, testing underwater fireworks happens to be quite expensive, so we will only be able to make two batches for each recipe. The batches will be our second level. This gives us the tree in :numref:`Fig. %s <local_project_organization>`.

.. _local_project_organization:

.. figure:: /_static/examples/fireworks/fireworks-tree.png
	:align: center
	:alt: Fireworks tree structure
	:figclass: align-center

	Project tree for the silent fireworks test.


**********************
Creating a New Project
**********************

Luckily our researchers have already written the analysis scripts and recorded the data for us, so all we have to do is create a Thot project for our experiments and run the analysis.

.. tabs::

	.. group-tab:: web

		From your home dashboard, click on the :badge:`Projects, badge-primary` button, then click the :badge:`New, badge-primary` button. This will take you to the New Project editor. The first thing you'll see here is a box, called a Container, and a tools panel. Containers are the organizational units of a Thot project. 

		The first thing we'll do is give our project a name. Click in the Name box of the Container and call it ``Silent Fireworks``. Let's edit the other properties of this Container now. 

		Click on the pen icon :fa:`pen, style=fas`, opening up the Container editor. From here, add a description about what the project is about. Something like

			Determining whether recipe A or B is quieter.

		Let's save the changes we made by clicking the :badge:`Save, badge-primary` button at the bottom of the editor.
			
	.. group-tab:: desktop

		TODO

	.. group-tab:: cli

		Local projects use your file system as a database. We will begin by making a folder for the project. Let's call it ``fireworks``. One of the main philosophies behind Thot is that data and analysis should be separate. Let's reflect this in our project by creating a ``data`` folder and an ``analysis`` folder.

		We will build our project tree in two ways. First, we'll create the tree for Recipe A by hand, to get a sense of how Thot uses our folders as a database. And second, we will use Thot's Utilities package to build the tree for Recipe B, automating the process.



****************************
Setting Up Your Project Tree
****************************

.. tabs::

	.. group-tab:: web

		We'll start by creating the Recipe A subtree. First click on the plus sign :fa:`plus-circle` to add a child Container to the project, and name it ``Recipe A``. Open the editor just as before by clicking on the pen icon. This time we'll set a few additional properties. First, set its type to ``recipe``. Next we'll add some metadata to the Container that we can use during the analysis. 

		.. admonition:: Metadata
			
			Metadata is data about data. During our course of research, we will often run the same type of experiment with different samples or experimental parameters. Metadata is how Thot incorporates this data about data into your projects.

		Click on the :badge:`Add Metadata, badge-success` button. Our metadata will be named ``recipe``, have a type of ``String``, and a value of ``A``. Save the Container just as before.

		Let's now add the batch Containers. This time we'll add both batches at once. To do this hold the :kbd:`Ctrl` key and click on the plus icon. This will reveal the Add Multiple Children dialogue box. In this case we want to add two children, one for each batch. Enter ``2`` into the input box and click the :badge:`Add, badge-primary` button.

		Name the first Container ``Batch 1``, and the second ``Batch 2``. To quickly move to the next Container you can press the :kbd:`Tab` key and to move to the previous one hold :kbd:`Shift` then press :kbd:`Tab`.

		Edit Batch 1 by setting its type to ``batch`` and adding a piece of metadata named ``batch`` of type ``Number`` and value ``1``. We'll also add our first piece of actual data to Batch 1.

		Add Recipe B to the project, and Batches 1 and 2 to the recipe. Set Recipe B's type to ``recipe`` and add a string metadata with value ``B`` to it, just as we did for Recipe A.
	
	.. group-tab:: desktop

		TODO


	.. group-tab:: cli

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

		Great! The ``data`` folder is now considered the ``root`` of our project because it is the highest Container. Now let's add the Container for Recipe A. Make a folder called ``recipe-a`` and add a ``_container.json`` file to it.

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
			thot utils add_containers --search '{ "type": "project" }' --containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "b" } } }'

			# For Windows
			thot utils add_containers --search "{ \"type\": \"project\" }" --containers "{ \"recipe-b\": { \"name\": \"Recipe B\", \"type\": \"recipe\", \"metadata\": { \"recipe\": \"b\" } } }"


		.. note::
			Windows does not interpret single quotes (') in the command line, so only double quotes can be used ("). Thus, to enclose strings double quotes must be used, and any double quotes inside the strings must be escaped with a backslash (\\).

			To convert from the Mac and Linux syntax to the Windows syntax, first escape all double quotes with a backslash ( ``"`` |rarr| ``\"``), then convert all single quotes into double quotes (``'`` |rarr| ``"``).

			Throughout this tutorial the Mac and Linux command line syntax will be used, with some examples of the change for Windows. However, it is assumed after the first few examples, you can make the necessary adjustments to the examples yourself.

		Let's see what this is doing. :code:`thot utils` will run the Utilities for us. Next we pass in the tool we want to use :code:`add_containers`. We then tell the tool which Container we want to add the new Containers to :code:`--search '{ "type": "project" }'`. Finally, we describe the Container we want to add :code:`--containers '{ "recipe-b": { "name": "Recipe B", "type": "recipe", "metadata": { "recipe": "b" } } }'`.

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

			:download:`Click here to download this project step. </_static/examples/fireworks/project_steps/00-tree/project/project.zip>`
