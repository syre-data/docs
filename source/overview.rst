########
Overview
########


.. warning::

    These docs are for Thot versions 0.9.x and below.

    For the versions 0.10.0 and above, please visit `our new tutorials <https://github.com/thot-data/tutorials>`_.

`Thot <https://thot.so>`_ is a software program to manage and analyze scientific data. 

Thot’s core principle is

.. rst-class:: font-weight-bold, text-center
.. pull-quote::

	Data and analysis should be modular and independent.

*******************
Thinking About Thot
*******************

To achieve this core principle Thot uses **top-down organization** and **bottom-up analysis**, visualized in :numref:`Fig. %s <fig_organization_analysis_model_inside_out>`. Another way to think about this is outside-in organization and inside-out analysis. This is implemented in a tree structure where each node has access to all the resources below it, and properties are inherited from above.

.. _fig_organization_analysis_model_top_down:

.. figure:: /_static/overview/organization-analysis-model.png
	:align: center
	:width: 65%
	:alt: Top-down organization, bottom-up analysis.
	:figclass: align-center
	:class: no-scaled-link

.. _fig_organization_analysis_model_inside_out:

.. figure:: /_static/overview/organization-analysis-model-nested.png
	:align: center
	:width: 65%
	:alt: Outside-in organization, inside-out analysis.
	:figclass: align-center
	:class: no-scaled-link

	Organization and analysis structure of a Thot project. Two ways of visualizing the structure, both are valid. (first) Top-down organization, bottom-up analysis. (second) Outside-in organization, inside-out analysis.

There are three types of Resources that make up a Thot project: **Containers** :fa:`square, style=far`, **Assets** :fa:`file-alt, style=far` :fa:`file-image`, and **Scripts** :fa:`cogs`. Containers are the organizational units of Thot. Containers can contain other Containers and Assets. Assets represent data in Thot. An Asset can be any type of file or resource which is consumed or produced by a Script. A Script represents an analysis procedure. Scripts are associated with Containers, allowing them to be reused. When a Script is being run on a Continer it ahs access to all the Assets in that Container's sub-tree and produces Assets in the Container it is being run on.

Containers
==========

Containers are the organizational building blocks of your project. They allow you to structure your projects and analysis in a logical way. Following the top-down organizational approach, Containers can contain both other Containers as children, and Assets. They can also have descriptors and metadata attached to them. Child containers inherit all the properties of their parents. Containers are also associated with Scripts, which analyze its Assets and produce new Assets.

.. figure:: /_static/overview/container-model.png
	:align: center
	:width: 45%
	:alt: Container model.
	:figclass: align-center
	:class: no-scaled-link

	Containers can contain other Containers and Assets, and have Scripts associated with them.

Assets
======

An Asset is anything that is consumed or created in your analysis. This includes raw data, calculated data, images, or any other resource. Each Asset can have its own descriptors and metadata attached to it.

Scripts
=======

A Script is a multi-input, multi-output function whose inputs and outputs are Assets. The input to a script is *consumed* and the output is *produced*. Produced Assets can then be consumed by other Scripts in the future.

.. figure:: /_static/overview/script-model.png
	:align: center
	:width: 55%
	:alt: Script model.
	:figclass: align-center
	:class: no-scaled-link

	Scripts consume and produce Assets.


Common Resource Properties
==========================

Each Resource has common properties, called Descriptors, that can be asigned to it, and can also have notes attached to it. In addition, Containers and Assets can have metadata assigned to them.

Descriptors
-----------

Descriptors are human-readable pieces of data that describe what they are attached to. These properties can be used to identify classes of Objects (through its type or tags), or individual objects (by its name).

+ Name
+ Type
+ Tags
+ Description

Notes
-----

Notes allow you to kep track of any observations, reminders, or comments you may have. For Scripts, this may be a reminder of analaysis that still needs to be implemented or tested. For Containers and Assets a note allows you to comment directly on the resource your referencing.

Metadata
--------

Metadata is data about data. This allows you to track the variations in your experiments, and easily utilize that information in your analysis. By using metadata to track your experimental parameters, you can directly compare experiments of the same type to analyze what effect changing an experiemntal parameter has on that measurement. Metadata is inherited by children from their ancestors, allowing you to easily group your experimental parameters.

.. admonition:: Example

	Imagine we are interested in doing a simple measurement of gravity. We drop balls of different weights from different heights. Assume we have light and heavy balls, and we will drop each from a short and tall height, measuring the time it takes to hit the ground.

	Our data for each experiment is the time, but we must modify this data with information about the drop height and ball weight. This is where metadata comes in. By marking each piece of data with metadata we can track these experimental parameters without modifying our data. And, because metadata is inherited, we can group our experiments first by ball weight, then by drop height, making our analysis more intuitive.

	.. figure:: /_static/examples/gravity/structure.png
		:align: center
		:width: 85%
		:alt: Example of metadata.
		:figclass: align-center
		:class: no-scaled-link

		Metadata adds information realted to experimental parameters to experimental data. It is inherited from ancestors allowing an intuitive grouping of experiments.


****************************************
Thot Projects: Organization and Analysis
****************************************

Thot is based on the idea that data and analysis should be separated, as stated in the core principle. This is implemented by keeping the data and analysis structures independent. Thot also takes the opinion that data should never be directly modified. This is enforced by allowing Scripts to only create new Assets, but never delete or modify existing ones.

Below is an example of a Thot Project's lifecycle to show how these ideas are refelected in Thot's architecture.

.. panels::
	:column: col-lg-12

	1) Organize using Containers
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	.. image:: /_static/overview/process-01-organize.png
		:width: 45%
		:class: no-scaled-link float-left mr-5


	Thot uses a Container tree to organize projects. This allows you to group your data in intuitive ways, easing your analysis process.

	---

	2) Add data using Assets
	^^^^^^^^^^^^^^^^^^^^^^^^

	.. image:: /_static/overview/process-02-data.png
		:width: 45%
		:class: no-scaled-link float-left mr-5

	Add experimental data to your project using Assets. This allows you to add descriptors, notes, and metadata to your data without modifying it.

	---
	
	3) Associate Scripts for analysis
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	.. image:: /_static/overview/process-03-associate.png
		:width: 45%
		:class: no-scaled-link float-left mr-5

	Tell Thot which Scripts to run on each Container by creating a Script Association.

	---
	
	4) Run the analysis
	^^^^^^^^^^^^^^^^^^^

	.. container:: float-left col-6 mr-4

		.. image:: /_static/overview/process-04a-analyze.png
			:class: no-scaled-link mb-5

		.. image:: /_static/overview/process-04b-analyze.png
			:class: no-scaled-link mb-5

		.. image:: /_static/overview/process-04c-analyze.png
			:class: no-scaled-link

	Starting from the bottom level of the Container tree, Thot automatically runs the analysis. After all the Scripts at one level are complete Thot runs the Scripts on the level above. This process is repeated, moving up the tree until the top is reached. This allows Scripts at higher levels to consume those produced at the lower levels. 

By keeping your Scripts separate from your data, you can reuse them on new projects. You can also retroactively add data to your projects, and without any modifciations, include it in your analysis just by re-analyzing the project.
