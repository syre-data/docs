###############
Writing Scripts
###############

Thot Scripts are functions that consume and produce Assets.

.. figure:: /_static/script-model.png
	:align: center
	:width: 55%
	:alt: Script model.
	:figclass: align-center
	:class: no-scaled-link

	Scripts consume and produce Assets.

To use an anaylsis script for a Thot project as a Script, first load the Thot project in your script

.. code-block:: python
	:caption: Loading a Thot project into a script.

	# for hosted projects
	from thot.thot import ThotProject
	thot = ThotProject()

	# for local projects
	from thot.thot import LocalProject
	thot = LocalProject()

To consume an Asset, find it using it's descriptors.

.. code-block:: python
	:caption: Finding Assets.

	asset  = thot.find_asset(  { 'name': 'Basic Asset' } )
	assets = thot.find_assets( { 'type': 'basic-asset' } )

If we need properties from a Container, we can find those too.

.. code-block:: python
	:caption: Finding Containers.

	container  = thot.find_container(  { 'name': 'Basic Container' } )
	containers = thot.find_containers( { 'type': 'basic-container' } )

The properties of Assets and Containers are accessed as properties. Of particular interest are is ``Asset.file``, ``Asset.metadata``, and ``Container.metadata``.

.. code-block:: python
	:caption: Using Resource properties.

	asset_name = asset.name
	asset_file = asset.file

	number_metadata = container.metadata[ 'number_metadata' ]

An Asset's ``file`` property is the path to the file, allowing the data to be loaded and analyzed how you wish. For instace, using the `Pandas package <https://pandas.pydata.org/>`__ we can load our data into a DataFrame.

.. code-block:: python
	:caption: Loading data.

	import pandas as pd
	df = pd.read_csv( asset.file )

We can now manipulate our DataFrame however we wish, performing analysis as usual, and using the metadata to represent experiment parameters. Once we have analyzed our data, we will want to output that data, either for our use or the use of another Script. To do this we use Thots ``add_asset`` function. ``add_asset`` takes in the Asset's properties, and output the path where the data should be saved.

.. code-block:: python
	:caption: Adding an Asset.

	asset_properties = {
		'name': 'New Asset',
		'type': 'new-asset',
		'tags': [ 'data', 'csv' ],
		'description': 'A newly analyzed Asset.',
		metadata: {
			'number_metadata':  3,
			'string_metadata':  'Nickname',
			'boolean_metadata': False
		}
	}
	
	new_asset_path = thot.add_asset( asset_properties )
	df.to_csv( new_asset_path )

There are no limits on how many Assets a Script can consume or produce. Scripts can also be given a priority, dictating their run order. This is important if multiple Scripts are associated to a single Container, and one Script depends on the Asset created by another.