Analyzing the Data
==================

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
.. 	  - Import the packages we're going to use, namely Pandas and Thot. In this case we only need to use a small part: ThotProject.
.. 	* - 6
.. 	  - Initialize the Thot project, giving us access to all the data stored within it.
.. 	* - 9
.. 	  - Find the Noise Data Asset we made for each batch by search for Assets who have a ``type`` of ``noise-data``.
.. 	* - 12
.. 	  - Load the noise data into a Pandas DataFrame.
.. 	* - 15
.. 	  - Compute statistics on the noise data.
.. 	* - 18-24
.. 	  - Create a new Asset to store the noise statistics in. Notice that the ``stats_properties`` dictionary we pass in mimics exactly the structure of the ``_asset.json`` files we created earlier. ``db.add_asset()`` accepts as its second argument an ``_id`` for the new Asset.
.. 	* - 27
.. 	  - Save the statistics to the new Asset.


+ **lines 2-3:** Import the packages we're goin to use, namely Pandas and Thot. In this case we only need to use a small part: ThotProject.

+ **line 6:** Initialize the Thot project, giving us access to all the data stored within it.

+ **line 9:** Find the Noise Data Asset we made for each batch by search for Assets who have a ``type`` of 'noise-data'.

+ **line 12:** Load the noise data into a Pandas DataFrame.

+ **line 15:** Compute statistics on the noise data.

+ **lines 18-24:** Create a new Asset to store the noise statistics in. Notice that the ``stats_properties`` dictionary we pass in mimics exactly the structure of the ``_asset.json`` files we created earlier. ``db.add_asset()`` accepts as its second argument an ``_id`` for the new Asset.

+  **line 27:** Saves the statistics to the new Asset.

Now we need to tell Thot which Containers to run this script from. This is done by creating Script Associations. 

.. tabs::

	.. group-tab:: desktop

		Again, we'll see how to add Script Associations from both the **Project** and **File Tree** views.

		From the **Project** view right click on ``Recipe A`` > ``Batch 1`` and select **Edit Scripts**. This open the **Script Associations** dialog. Click the **Add Script** button at the top of the dialog and select the ``noise_stats.py`` Script we just created. We can ensure the Script Association was created successfully by changing the preview from Assets to Scripts.

		.. figure:: /_static/get_started/local/script_associations_dialog.png
			:align: center
			:alt: Script Associations dialog.
			:figclass: align-center

			Script Associations dialog.

		For ``Recipe A`` > ``Batch 2`` lets assign the same Script, but instead of right clicking on the Container to open the **Script Associations** dialog, double click on the Scripts preview of the Container. At the moment this is **(none)** for the Container.
		
		Now switch to the **File Tree** view and select ``Recipe B`` > ``Batch 1``. Click the **Add Scripts** button, and perform the same steps.

		**Add Scripts** will add Scripts to the selected Container, while **Set Scripts** will remove any previously associated Scripts, and set them to match what is submitted.

		Let's run our first analysis! From the **Project** view switch the **Assets** preview so we can see our new Assets being created. Then, when you're ready, click the **Analyze** button in the upper right of the workspace.

		.. warning::

			Running the analysis by pressing the ``Analyze`` button may give you an error. If this occurs please attempt to run the analysis from the command line.

			To do this open up a terminal (Anaconda prompt on Windows) navigate to teh project root (**data** folder) and run ``thot run``.

			More information is available in the ``cli`` tab of this section.

		.. figure:: /_static/get_started/local/noise_stats_analysis.png
			:align: center
			:alt: Analyze button.
			:figclass: align-center

			Analyze button.


		When the analysis is running we can continue to work on our project, and when the analysis is complete we will get a notification pop up and the new Assets will appear in our preview.


	.. group-tab:: cli

		We'll start off again creating a Script Association by hand, then see how to automate the process using the Utilities.

		Navigate to the **Recipe A > Batch 1** Container. We create Script Associations by placing a ``_scripts.json`` file in a Container. Go ahead and create this file and paste the contents below inside it.

		.. code-block:: JSON
			:caption: recipe-a/batch-1/_scripts.json

			[
				{
					"script": "root:/../analysis/noise_stats.py"
				}
			]

		This tells Thot to run the ``noise_stats.py`` script from this Container. The ``script`` field is the path to the script to run, it can be a relative or absolute path. The special ``root:`` directive points to the project root.

		Before adding the script to the rest of the batches, let's try it out. In your terminal run

		.. code-block:: bash
			
			thot run

		You should see the ``noise_stats`` Asset be added to the folder. Great! Now let's make it so we analyze all the batches. Navigate to the project root (``data`` folder) and run

		.. code-block:: bash
			
			thot utils set_scripts -s '{ "type": "batch" }' --scripts '[ { "script": "root:/../analysis/noise_stats.py" } ]'

		You'll notice that we replaced the ``--search`` flag from the previous command like this with the ``-s`` flag. The two are synonyms for each other, ``-s`` just giving us a shorthand for ``--search``. 

		Now let's analyze the entire project by running ``thot run`` again. This will create a new Noise Statistics Asset for each of the batches.

.. only:: builder_html or readthedocs

	:download:`Click here to download this project step. </_static/examples/fireworks/project_steps/02-analysis/project/project.zip>`



Moving On Up
------------

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

Let's add this new script to run on our recipe Containers, and then run it.

.. tabs::

	.. group-tab:: desktop

		Use any of the methods we learned before to associate the ``recipe_stats.py`` Script to the ``Recipe A`` and ``Recipe B`` Containers, then analyze the project again.

		
	.. group-tab:: cli

		From the project root run

		.. code-block:: bash

			thot utils add_scripts -s '{ "type": "recipe" }' --scripts '{ "script": "root:/../analysis/recipe_stats.py" }'

			thot run

Let's build our final analysis script now so we can see which recipe is better. In the analysis folder create the ``recipe_comparison.py`` script.

.. literalinclude::  /_static/examples/fireworks/project_steps/03-moving_up/project/analysis/recipe_comparison.py
	:language: python
	:caption: recipe_comparison.py
	:linenos:

Let's breakdown the new concepts:

+ **line 15:** Use the recipe metadata from the Asset to name the data.

+ **line 29, 45:** We've already seen that we can pull in multiple Assets into our scripts. Here we also see that we can create multiple Assets in a single script. Also notice that one Asset is a CSV text file, while the other is a PNG image file. Assets can be any sort of file.

.. tabs::

	.. group-tab:: desktop

		Add the proper Script Association to the ``Silent Fireworks`` Container, and analyze the project. 
		
	.. group-tab:: cli

		Add the proper Script Association (``_scripts.json``) to the root folder, and analyze the project.


And we're done! Take a look at the Assets we created so we know which recipe is quieter and can report to the boss which we should use to keep those fish as happy as possible.

.. only:: builder_html or readthedocs

	:download:`Click here to download the final project. </_static/examples/fireworks/project_steps/03-moving_up/project/project.zip>`