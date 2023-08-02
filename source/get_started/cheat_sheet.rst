Cheat Sheets
============


.. warning::

    These docs are for Thot versions 0.9.x and below.

    For the versions 0.10.0 and above, please visit `our new tutorials <https://github.com/thot-data/tutorials>`_.

Here are the most important concepts and commands we learned through this tutorial.

+ The ``root:`` directive points to the project root.


Containers
----------

+ A Container is a folder with a ``_container.json`` file in it. Containers can contain other Containers, Assets, and Script Associations.

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

.. tabs::

	.. group-tab:: desktop

		**Project view**

		* Add children to Containers by clicking on the :fa:`plus-circle, style=fas` icon.
		* Edit a Container's properties by clicking on the :fa:`pen, style=fas` icon or right clicking on the Container and selecting **Edit Properties**.
		* Toggle a Container's children's visibilty clicking on the :fa:`eye, style=fas` icon.
		* Duplicate a tree by right clicking on the desired root and selecting **Duplicate Tree**.
		* Remove a tree by right clicking on the root of it and selecting **Exclude Tree**.


		**File Tree view**

		* Add a child to a Container by slecting it then clicking the **Add Child** button.
		* Edit a Container's properties by selecting it and editing them from the side panel.
		* Make a folder a Container by selecting it and clicking the **Make Container** button.

		
	.. group-tab:: cli

		+ Add children Containers to the matched search Containers.

		.. code-block:: bash
			:caption: Adding children Containers.

			thot utils add_containers --search '{ "type": "parent-container" }' --containers '{ "container_1": { "name": "Container 1", "type": "child-container" }, "container 2": { "name": "Container 2", "type": "child-container" }  }'

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

.. tabs::

	.. group-tab:: desktop

		**Project view**

		* Add Assets to a Container by dragging and dropping them.
		* Edit a Container's Asset's properties by previewing them and double clicking on the Asset you want to edit.
		
		**File Tree view**

		* Add an Asset by selecting a Container and clicking the **Add Asset** button.
		* Edit an Asset's properties by selecting it and editing them from the side panel.
		* Make a folder an Asset by selecting it and clicking the **Make Asset** button. 
		
	.. group-tab:: cli

		+ Add Assets to the matched Containers.

		.. code-block:: bash
			:caption: Add Assets.
			
			thot utils add_assets --search '{ "type": "basic-container" }' --assets '{ "new_asset": { "name": "New Asset", "file": "data.pkl" } }'

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

.. tabs::

	.. group-tab:: desktop

		**Project view**

		* Add Script Associations to a Container by right clicking on it and selecting **Edit Scripts** or previews Scripts and double clicking on th preview area.

		**File Tree view**

		* Set a Container's Script Association by selecting it and click the **Set Scripts** button. This will remove any previously set Script Associations.

		* Add Script Associations to a Container by selecting it and clicking the **Add Scripts** button. This will add the Script Associations to any that were previously set. 
		
	.. group-tab:: cli

		+ Add Script Associations to the matched Containers.

		.. code-block:: bash
			:caption: Add Script Associations.

			thot utils add_scripts --search '{ "type": "basic-container" }' --scripts '{ "script": "path/to/script.py" }'

		+ Set Script Associations of the matched Containers.

		.. code-block:: bash
			:caption: Set Script Associations.

			thot utils set_scripts --search '{ "type": "basic-container" }' --scripts '[ { "script": "path/to/script.py" }, { "script": "root:/path/to/another.py" } ]'

Analysis
--------

+ To initialize a Thot project in your Python script.

.. code-block:: python
	:caption: Initialize a Thot project.

	from thot import ThotProject
	db = ThotProject()

+ Finding Containers and Assets.

.. code-block:: python
	:caption: Finding Containers and Assets.

	container  = db.find_container(  { 'name': 'Basic Container' } )
	containers = db.find_containers( { 'type': 'basic-container' } )

	asset  = db.find_asset(  { 'name': 'Basic Asset' } )
	assets = db.find_assets( { 'type': 'basic-asset' } )

+ Getting the information from a Container or Asset is the same.

.. code-block:: python
	:caption: Getting information from Containers and Assets.

	file_path = asset.file
	container_name = container.name

	is_boolean    = container.metadata[ 'boolean_metadata' ]
	nested_number = container.metadata[ 'json_metadata' ][ 'another_number' ]

+ Analyze the project.

.. tabs::

	.. group-tab:: desktop

		Click the **Analyze** button in the upper right corner of the **Project** view.
		
	.. group-tab:: cli

		.. code-block:: bash
			:caption: Analyzing a project.
			
			thot run

