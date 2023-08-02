.. include:: <isoamsa.txt>

###############
Writing Scripts
###############


.. warning::

    These docs are for Thot versions 0.9.x and below.

    For the versions 0.10.0 and above, please visit `our new tutorials <https://github.com/thot-data/tutorials>`_.

Thot Scripts are functions that consume and produce Assets.

.. figure:: /_static/overview/script-model.png
	:align: center
	:width: 55%
	:alt: Script model.
	:figclass: align-center
	:class: no-scaled-link

	Scripts consume and produce Assets.

********
Thot API
********

The Thot API exposes the ``ThotProject`` class containing five methods:

+ **find_container( <search> ):** Finds and returns a single Container matching the search, or ``None`` if none are found.

+ **find_containers( <search> ):** Finds and returns a list of Containers matching the search.

+ **find_asset( <search> ):** Finds and returns a single Asset matching the search, or ``None`` if none are found.

+ **find_assets( <search> ):** Finds and returns a list of Assets matching the search.

+ **add_asset( <properties> ):** Adds an Asset to the project with the given properties. Returns the path of the added Asset at which the Asset's data should be stored.

The ``find_*`` methods all accept a dictionary to search for. The dictionary's keys can be any property for an Asset or Container, with values to match against.

.. code-block:: python
	:caption: Valid search fields.

	{
		'name': str,
		'type': str,
		'tags': [ str ],
		'metadata': { 'key': value } 	
	}

``add_asset`` accepts a dictionary from which the Asset's properties are set. The dictionary's keys can be any valid Asset property, with corresponding value.
	
.. code-block:: python
	:caption: Valid Asset properties

	{ 
		'name': str, 
		'type': str, 
		'tags': [ str ],
		'description': str,
		'metadata': { 'key': value }
	}

Locally run projects have some modified functionality for convenience.

+ **dev_mode():** Returns ``True`` if the project is being run in "dev mode", ``False`` otherwise. This method is useful if you are testing scripts locally. (See :ref:`Testing Local Scripts <testing_local_scripts>` for more info.)

+ **add_asset( <properties>[, id] ):** An optional id parameter may be passed to set the Asset's id.


Examples
========

To use an anaylsis script for a Thot project as a Script, first load the Thot project in your script

.. code-block:: python
	:caption: Loading a Thot project into a script.

	from thot import ThotProject
	db = ThotProject()


To consume an Asset, find it using it's descriptors.

.. code-block:: python
	:caption: Finding Assets.

	asset  = db.find_asset(  { 'name': 'Basic Asset' } )
	assets = db.find_assets( { 'type': 'basic-asset' } )

If we need properties from a Container, we can find those too.

.. code-block:: python
	:caption: Finding Containers.

	container  = db.find_container(  { 'name': 'Basic Container' } )
	containers = db.find_containers( { 'type': 'basic-container' } )

The properties of Assets and Containers are accessed as properties. Of particular interest are is ``Asset.file``, ``Asset.metadata``, and ``Container.metadata``.

.. code-block:: python
	:caption: Using Resource properties.

	asset_name = asset.name
	asset_file = asset.file

	number_metadata = container.metadata[ 'number_metadata' ]

An Asset's ``file`` property is the path to the file, allowing the data to be loaded and analyzed how you wish. For instace, using the `Pandas package <https://pandas.pydata.org/>`_ we can load our data into a DataFrame.

.. code-block:: python
	:caption: Loading data.

	import pandas as pd
	df = pd.read_csv( asset.file )

We can now manipulate our DataFrame however we wish, performing analysis as usual, and using the metadata to represent experiment parameters. Once we have analyzed our data, we will want to output that data, either for our use or the use of another Script. To do this we use Thot's ``add_asset`` function. ``add_asset`` takes in the Asset's properties, and output the path where the data should be saved.

.. code-block:: python
	:caption: Adding an Asset.

	asset_properties = {
		'name': 'New Asset',
		'type': 'new-asset',
		'tags': [ 'data', 'csv' ],
		'description': 'A newly analyzed Asset.',
		'metadata': {
			'number_metadata':  3,
			'string_metadata':  'Nickname',
			'boolean_metadata': False
		}
	}
	
	new_asset_path = db.add_asset( asset_properties )
	df.to_csv( new_asset_path )

There are no limits on how many Assets a Script can consume or produce. Scripts can also be given a priority, dictating their run order. This is important if multiple Scripts are associated to a single Container, and one Script depends on the Asset created by another.

.. _testing_local_scripts:

*********************
Testing Local Scripts
*********************

.. note::

	This only applies to locally run projects.

It is conventient to test your analysis script on a specific Contain to ensure it is producing the correct results. Thot allows you to do this by passing in a root Container when creating the project.

.. code-block:: python
	:caption: Setting a Local Project's root Container.

	# for local projects only
	from thot import ThotProject
	db = ThotProject( dev_root = 'path/to/test/container' )

However with this arrangement, the script will always use the given Container as the root. Instead, we want to use the designated path only for testing, but allow Thot to set the root Container during the actual analysis. ``ThotProject`` has a ``dev_mode()`` method which allows the script to distinguish if Thot is running an analysis, or if you are just testing the script. You can initialize a ``ThotProject`` with the ``dev_root`` parameter for testing, and use the ``dev_mode`` method to only perform certain actions during testing.

.. code-block:: python
	:caption: Testing a local script.

	db = ThotProject( dev_root = 'path/to/test/container' )
	asset = db.find_asset( {} )
	if db.dev_mode():
		# only run when testing
		print( asset.name )
