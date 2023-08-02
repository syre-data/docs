##############
Thot Utilities
##############


.. warning::

    These docs are for Thot versions 0.9.x and below.

    For the versions 0.10.0 and above, please visit `our new tutorials <https://github.com/thot-data/tutorials>`_.

Thot Utilities is a command line tool built to automate the common or tedious tasks you may have to perform when managing your local projects.

**********
Containers
**********

Add Containers
==============


Remove Containers
=================

.. note::
	Removing Containers doesn't delete anything, it just renames the ``_container.json`` file so Thot does not recognize it as a Container anymore.

.. warning::
	Removing a Container removes the entrie subtree below it.


******
Assets
******

Add Assets
==========


Remove Assets
=============

.. note::
	Removing Assets doesn't delete anything, it just renames the ``_asset.json`` file so Thot does not recognize it as an Asset anymore.


Converting Data Files to Assets
===============================

Convert can be a bit complicated because you can use functions to assign properties

The basic command is 

.. code-block:: bash
	:caption: data_to_assets

	thot utils data_to_assets --search <glob> --assets <asset_dictionary> --kwargs { "_id": <id>, "rename": <rename> }

``<glob>`` is a `glob pattern <https://en.wikipedia.org/wiki/Glob_(programming)>`__ to match the data.

``<asset_dictionary>`` is either a function that returns a dictionary representing  the Asset, or a dictionary representing the Asset where the values can either be static or a lambda function that returns the value for the given field. Functions are passed the full path of the asset file.

``<id>`` and ``<rename>`` can be either a string or a lambda function. If ``<rename>`` is a function it is passed the absolute path of the original data file. If ``<id>`` is a function it is passed the same.

Functions are passed the absolute path of the Asset file (i.e. after the original file has been moved to the Asset folder and renamed).

The ``_id`` field sets the id of the Asset, i.e. the relative path.

The ``rename`` field will rename the data file once moved to the Asset folder.

You also have to make sure that everything is properly quoted i.e. You can use different types of quotes inside of eachother, or need to escape the same type of quote with a backslash (\\).


Most basic use

.. code-block:: bash
	
	thot utils data_to_assets


*******
Scritps
*******

Add Scripts
===========


Remove Scripts
==============



Set Scripts
===========
