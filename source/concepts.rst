.. include:: <isonum.txt>

################
Concepts of Thot
################

There are two types of project you can run with Thot: :ref:`Local<local_projects>` and :ref:`Hosted<hosted_projects>`. Local projects are run on your computer -- no internet connection or registration required. Hosted projects are run from the `Thot website <http://www.thot-data.com>`_ and provide additional functionality. If you have a Hosted account, you can sync your Local Projects with it, so data is automatically uploaded to the Thot servers and analyzed.


********************
Creating a Project
********************

.. _local_projects:

Local Projects
==============

Local and Hosted projects really only differ in how they store your data. Local projects use your file directory as a database, while the Hosted version uses the Thot server. 

Local projects are just a set of folders and files on you computer. To tell Thot what a folder or file is you use an **Object File**. Object Files are just :ref:`JSON<json>` files that provide information to your project. There are three types of Object Files -- one for each component of a Thot project.

.. warning::
	A folder can be either a Container or an Asset, not both.

.. note::
	You can use ``root:`` to refer to the root Container of the project. This allows the use  of absolute paths within the project. Instead of writing ``../../../path/to/file.csv`` you could write ``root:/path/to/file.csv``.

_container.json
----------------

By adding a **_container.json** file to a folder you mark it as a Container. A Container file has the following properties:

+ **name:** The name of the Container. Can be used for retrieval in a script. If this is not provided, the base name of the folder is used.

+ **type:** Represents the class of the container. This is most useful to designate what level of the organizational structure the Container is at.

+ **description:** A description of the Container.

+ **tags:** A list of tags used for retrieving the container in a script.

+ **metadata:** A set of key-value pairs representing metadata about the Container and its children.

.. code-block:: JSON

	{
		"name": "",
		"type": "",
		"description": "",
		"tags": [],
		"metadata": {}
	}


_asset.json
------------

By adding an **_asset.json** file to a folder you mark it as an Asset. In addition to the basic properties of the Container, an Asset also has:

+ **file:** Absolute or relative path to the Asset file. It is best to put the file in the Asset folder, so a relative path is most convenient.

+ **creator:** The creator of the Asset. If the Asset was created by a specific machine, this is a good place to mark that. If the Asset was produced by a script, this will be set to the path of the script, allowing you to trace back its origin.

+ **creator_type**: This indicates whether the Asset was created by a user or a script. If a script produced it, this will automatically be set. 

.. code-block:: JSON

	{
		"name": "",
		"type": "",
		"description": "",
		"tags": [],
		"metadata": {},

		"file": "path/to/asset.csv",
		"creator": "",
		"creator_type": "user"
	}


.. _scripts_json:

_scripts.json
--------------

Scripts files are a bit different than those for Containers and Assets. These files create an association between a script and a Container. This file tells Thot which scripts to run, and in which order.

.. warning::
	Only Containers can contain a _scripts.json file.

A Scripts file contains a list of Script Associations:

+ **script:** Relative or absolute path to the script.

+ **priority:** The order in which to run the script. Lower priorities go first.

+ **autorun:** Whether to automatically run the scrpt when evaluating a project. If false you will have to manually run the script. 

.. code-block:: JSON

	[
		{
			"script": "path/to/script.py",
			"priority": 0,
			"autorun": true
		}
	]


Notes
-----

A **_notes** folder can also be included in a Container or Asset. Text files containing notes about the object can be stored in this folder. Each notes has the properties

+ **created:** The date of creation interpreted form the time the note was last modified.

+ **title:** The title of the note, interpreted from the name of the file.

+ **content:** The note itself, read from the contents of the file.


Utilities
---------

Thot comes with a ``utilities`` module to make building local projects an easier task. For full documentation use ``python -m thot.utilities -h``. All utility functions output the ids of modified of Containers.

Options


Utilities functions include some generic options that can be applied to all functions.

+ ``--root``, ``-r``: Specifies path to the root Container.

+ ``--overwrite``, ``-w``: If a conflict emergers, overwrite the original content with the provided content. Otherwise, leave the original content.

+ ``--search``, ``-s``: JSON object used to match Containers to apply the function to.

.. warning::
	Ensure that your JSON is properly quoted. You will likely have to place single quotes around the JSON string, and double quotes around property keys and strings within the object. E.g. ``'{ "string_property": "test string", "boolean_property": true, "number_property": 42 }'``

.. note::
	On Windows you must be careful with two things.

	First, you can not have spaces within quoted text. This results in an ``unrecognized arguments`` error. And second, Windows does not interpret single quotes (``'``) in the command line, so only double quotes (``"``) can be used. Thus, to enclose strings double quotes must be used, and any double quotes inside the strings must be escaped with a backslash (``\``).

	Thus, the example command above on a Windows machine should be written as ``"{\"string_property\":\"test string\",\"boolean_property\":true,\"number_property\":42}"``


Scripts
^^^^^^^

You can autotmatically add scripts to a project using the ``add_scripts`` function.

.. code-block:: bash

	python -m thot.utilities add_scripts --scripts <scripts_object>


Where ``<scripts_object>`` mimics the :ref:`_scripts.json<scripts_json>` file. For convenience, if only one script is being added it does not need to be enclosed in an array.


Scripts can also be automatically removed with the ``remove_scripts`` function.

.. code-block:: bash

	python -m thot.utilities remove_scripts --scripts [script_1, script_2, ...]

For convenience, if only a single script is being removed it does not need to be in an array. If a script does not exist on a selected Container it is not modified. Scripts are matched based on the ``"script"`` field.

Finally, you can set the scripts automatically using the ``set_scripts`` function.

.. code-block:: bash

	python -m thot.utilities set_scripts --scripts <scripts_object>


.. _json:

JSON
----

JSON is a file format that allows data to be stored in a human-readable form. You can find a nice introduction at `W3Schools <https://www.w3schools.com/js/js_json_syntax.asp>`_, and full documentation at `json.org <https://www.json.org/json-en.html>`_.



.. _hosted_projects:

Hosted Projects
===============

To create a Hosted project go to `thot-data.com <http://www.thot-data.com>`_ and `create an account <http://www.thot-data.com/register>`_ or `log in <http://www.thot-data.com/login>`_.

Hosted projects have additional features such as user friendly interfaces for project creation, sharing projects and scripts, and more.

A Hosted Project uses the Thot servers as its database. Anytime a change is made to a project, the relevant analysis are automatically run, unless the scripts are set to run manually.


***************
Writing Scripts
***************

Thot is founded on the idea that the same analysis needs to be run on different data sets. Often this is done manually, taking additional time and effort, and is prone to mistakes. By separating the analysis process from the data, Thot allows your data to be automatically analyzed.

Thot Projects
=============

Because Thot separates the analysis from the data, you need a way to pull your data in to the script in a Container relative manner. This is done using a Thot Project.

Because analysis is bottom-up, a script only has access to Containers and Assets below it.

Thot Interface
==============

Each Thot Project implements a standard interface. This makes converting between Local and Hosted projects easy. A Thot Interface consists of the following structure.

Properties
----------

+ **root:** Current Container being analyzed.

Methods
-------

+ **find_container( search = {} ):** Returns a Container matching the search criteria.

+ **find_containers( search = {} ):** Returns a list of Containers matching the search criteria.

+ **find_asset( search = {} ):** Returns an Asset matching the search criteria.

+ **find_assets( search = {} ):** Returns a list of Assets matching the search criteria.

+ **add_asset( asset [, id = None, overwrite = True] ):** Creates a new asset in the currently active Container. Returns the id of the new Asset. For a Local project the id is the absolute path to the Asset.

Local Project
=============

A Local Project is a Thot Interface that uses your local file system as its database. During the analysis everything is performed relative to the active Container.

A simple python script for a local project may look something like

.. code-block:: python

	import pandas as pd
	from thot import ThotProject

	db = ThotProject() # set up local project

	# retrieve data
	sample = db.find_container( { 'type': 'sample'  } )
	data = db.find_asset( { 'type': 'times' } )

	# analyze data
	df = pd.read_csv( data.file )
	stats = df.mean()

	# produce new Asset for future consumption
	stats_props = {
		'file': 'stats.csv',
		'type': 'stats',
		'name': '{} Stats'.format( sample.name )
	}

	asset_path = db.add_asset( stats_props, 'stats', overwrite = True )
	stats.to_csv( asset_path )


Testing Scripts
---------------

You can test your scripts using the ``dev_root`` argument when initializing a ``ThotProject``.

.. code-block:: python

	db = ThotProject( dev_root = 'path/to/test/container' )

This allows you to run your scripts in a Python interpreter without analyzing the entire project tree. 

The ``ThotProject``s also have a ``dev_mode()`` method that returns ``True`` if the script is being run manually (e.g. from the console or within a Jupyter Notebook), and ``False`` if it's being run by the :ref:`runner`. 

.. _runner:

Runner
------

Once your project is set up you use the Runner to evaluate it.

.. code-block:: shell

	thot run [--root <path/to/tree>] [--scripts [ <script_1>, <script_2>, ... ] ]

+ ``--root``: Specifies the root container whose tree should be run. This doesn't need to be the root of the project. If not included the current directory is used as the root. 

+ ``--scripts``: A JSON array specifying which scripts to run. If not included all scripts are run.
