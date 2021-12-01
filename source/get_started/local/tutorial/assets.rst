.. include:: <isonum.txt>


Adding Data to Your Project
===========================

Now that we have our tree, we can add data. Most often data is added to the lowest level Containers in our project because these are the things we actually run experiments on. Luckily our researchers just finished up with their experiments and have provided you with the download link.

.. only:: builder_html or readthedocs

	:download:`Click here to download the experimental results. </_static/examples/fireworks/project_steps/01-assets/experiment_data/data.zip>`

After downloading the experimetnal results, unzip the data and remember it's location.

In Thot, any data file we want to analyze -- CSV, text, images, binary, anything -- is called an Asset. Similar to Containers, an Asset is a folder with an ``_asset.json`` file in it.  

.. tabs::

	.. group-tab:: desktop

		We want to add our Assets to the batches. Let's do the first manually, then we'll use some more convenient methods.

		Go to the **File Tree** view and select ``Batch 1`` of ``Recipe A``. Click the **Add Asset** button. This opens the Asset Properties dialog, which should look quite familiar.

		.. figure:: /_static/get_started/local/asset_properties_dialog.png
			:align: center
			:alt: Asset Properties dialog.
			:figclass: align-center

			Asset Properties dialog.

		Give the Asset the following properties, and select the ``recipe_a-batch_1.csv`` file.

		=========	==========
		**Name:**	Noise Data
		**Type:**	noise-data
		=========	==========

		You'll notice this moves the data file to a the newly created Asset folder inside the ``Batch 1`` folder. This is because we had the **Move asset file** option selected. 

		Do the same for ``Batch 2``.

		Let's add the ``Recipe B`` data a bit differently. Switch to the **Project** view and refresh the project. Let's preview what Assets we already have by clicking on the dropdown menu in the upper left of the workspace where it says **-None-** and select **Assets**. 

		.. figure:: /_static/get_started/local/project_view_assets_preview.png
			:align: center
			:alt: Project view Assets preview.
			:figclass: align-center

			Project view Assets preview.

		Now open a file explorer and navigate to the data folder. Drag and drop the data for ``Recipe B`` on to the respective batches. You'll see the Assets appear in the preview as you add them, but the names don't look very pretty. Let's edit that by double clicking on them. This opens the familiar **Asset Properties** dialog, where we can set the ``Name`` and ``Type`` properties with the same values as before.

		.. figure:: /_static/get_started/local/assets_complete.png
			:align: center
			:alt: Project with all the Assets added.
			:figclass: align-center

			Project with all the Assets added.

		
	.. group-tab:: cli

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

			thot utils add_assets --search '{ "type": "batch" }' --assets '{ "noise_data": { "name": "Noise Data", "type": "noise-data", "file": "data.csv" } }'

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


Wonderful! We've now created our project structure and added our data. Next we'll look at how to analyze the data using Thot Scripts.

.. only:: builder_html or readthedocs

	:download:`Click here to download this project step. </_static/examples/fireworks/project_steps/01-assets/project/project.zip>`