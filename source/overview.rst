########
Overview
########

*******************
Thinking About Thot
*******************

Thot is based on **top-down organization** and **bottom-up analysis**, or, congruently, **outside-in organization** and **inside-out analysis**.

[images]

There are three components of a Thot project: **Containers**, **Assets**, and **Scripts**.

Containers
==========

Containers are the organizational building blocks of your project. They allow you to structure your projects and analysis in a logical way. Following the top-down organizational approach, Containers can contain both other Containers as children, and Assets. They can also have descriptors and metadata attached to them. Child containers inherit all the properties of their parents. Containers are also associated with Scripts, which analyze its Assets and produce new Assets.

Assets
======

An Asset is anything that is consumed or created in your analysis. This includes raw data, calculated data, and images. Each Asset can have descriptors and metadata attached to it as well.

Scripts
=======

A Script is a multi-input, multi-output function where the inputs and outputs are Assets. The input to a script is *consumed* and the output is *produced*. The produced Assets can then be consumed by other Scripts in the future.

Descriptors
-----------

Descriptors are human-readable pieces of data that describe what they are attached to. These properties can be used to identify classes of Objects (through its type or tags), or individual objects (by its name).

+ Name
+ Type
+ Tags
+ Description

Metadata
--------

Metadata is data about data. Children inherit metadata from their parents.



************
Organization
************

Thot utilizes a tree structure to organize data. Properties of children are inherited form their ancestors.



********
Analysis
********

Thot is based on the idea that data and analysis should be separated and data should never be modified. You can think of a Thot analysis script as a machine reads data manipulates them and creates new pieces of data.