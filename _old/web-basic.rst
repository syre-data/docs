.. _hosted_project_basics:

#####################
Hosted Project: Basic
#####################
Congratulations! You've just been hired as the head of the R+D department at Puzzles Underwater Fireworks company. The city's aquarium just hired us for their annual New Year's Eve extravaganza, and they want to do something extra special this year: fireworks for the fish. Luckily, our team has been working hard for the past six months on two new recipes for silent explosions. A perfect solution so the fish don't get scared. Looks like your first project will be to compare the two recipes to see which is quieter. Good Luck!

************
Getting Thot
************

Go to our website at `thot-data.com <http://thot-data.com>`_, and create an account if you haven't already, otherwise log in.

***********************
Organizing Your Project
***********************

The first thing we need to do is organize our project. Thot uses a tree structure to organize your projects, giving your project different levels. The top level should be the most important grouping to you, becoming less important as you move down the tree. 

For this project the most important thing we need to test is which recipe is quieter, so our top level grouping will be the recipes. Unfortunately, testing underwater fireworks happens to be quite expensive, so we will only be able to make two batches for each recipe. The batches will be our second level. This gives us the tree in :numref:`Fig. %s <fig_hosted_project_organization>`

.. _fig_hosted_project_organization:

.. figure:: /_static/examples/fireworks/fireworks-tree.png
	:align: center
	:alt: Fireworks tree structure
	:figclass: align-center

	Project tree for the silent fireworks test.

**********************
Creating a New Project
**********************

Luckily our researchers have already written the analysis scripts for us, and tabulated the data, so all we have to do is create the project and run the analysis.

.. only:: builder_html or readthedocs

	:download:`Click here to download the project. </_static/examples/fireworks/hosted/fireworks.zip>`

From your home dashboard, click on the :badge:`Projects, badge-primary` button, then click the :badge:`New, badge-primary` button. This will take you to the New Project editor. The first thing you'll see here is a box, called a Container, and a tools panel. Containers are the organizational units of a Thot project. 

The first thing we'll do is give our project a name. Click in the Name box of the Container and call it ``Silent Fireworks``. Let's edit the other properties of this Container now. 

Click on the pen icon :fa:`pen, style=fas`, opening up the Container editor. From here, add a description about what the project is about. Something like

	Determining whether recipe A or B is quieter.

Let's save the changes we made by clicking the :badge:`Save, badge-primary` button at the bottom of the editor.


Adding Levels
=============

We'll start by creating the Recipe A subtree. First click on the plus sign :fa:`plus-circle` to add a child Container to the project, and name it ``Recipe A``. Open the editor just as before by clicking on the pen icon. This time we'll set a few additional properties. First, set its type to ``recipe``. Next we'll add some metadata to the Container that we can use during the analysis. 

.. admonition:: Metadata
	
	Metadata is data about data. During our course of research, we will often run the same type of experiment with different samples or experimental parameters. Metadata is how Thot incorporates this data about data into your projects.

Click on the :badge:`Add Metadata, badge-success` button. Our metadata will be named ``recipe``, have a type of ``String``, and a value of ``A``. Save the Container just as before.

Let's now add the batch Containers. This time we'll add both batches at once. To do this hold the :kbd:`Ctrl` key and click on the plus icon. This will reveal the Add Multiple Children dialogue box. In this case we want to add two children, one for each batch. Enter ``2`` into the input box and click the :badge:`Add, badge-primary` button.

Name the first Container ``Batch 1``, and the second ``Batch 2``. To quickly move to the next Container you can press the :kbd:`Tab` key and to move to the previous one hold :kbd:`Shift` then press :kbd:`Tab`.


Edit Batch 1 by setting its type to ``batch`` and adding a piece of metadata named ``batch`` of type ``Number`` and value ``1``. We'll also add our first piece of actual data to Batch 1.

Click the :badge:`New Assets, badge-success` button, navigate to the project folder, and select the file ``a1-data.csv``. This creates an Asset for the data, and adds it to the Container. To access the Asset in our analysis script we'll find it by its type. To set this click on the down arrow :fa:`chevron-down` to open its editor. Double click on the ``(No type)`` text to open its type editor, and set it to `noise-data`. To save the changes you can either click on the :badge:`Save, badge-success` button, or press :kbd:`Shift + Enter`. To close the editor without saving press `Esc`. To minimize the Asset's editor click on the up arrow :fa:`chevron-up`.

Save the changes to Batch 1, and we'll now move on to Batch 2. This time let's add the data in another way. Instead of doing it from Batch 2's editor, will do it directly from the Container Tree. Find the data file ``a2-data.csv`` and drag and drop it on to the Batch 2 Container. This adds an Asset for the data and adds it to the Container.

Open Batch 2's editor, set its type and add a piece of metadata similar to how we did for Batch 1. Be sure to change the metadata value to ``2`` though. We'll also set the type of the Asset exactly as we did for Batch 1.


Project Assets
==============

As you've started to see, Thot's interface is designed to allow you to do the same thing in many ways. This allows you to work in the way that is most convenient to you. Let's see another way to add Assets to our project.

Switch to the Project Assets view by clicking on the Assets icon :fa:`file-image` in the tools panel. Here you can see a list of all the Assets in our project. We can also add Assets to the project, and associate them with Containers later. We'll add the Assets for Recipe B to the project now. Drag and drop the data files ``b1-data.csv`` and ``b2-data.csv`` to the designated area to add them. Just as we did before, set their type to ``noise-data``. Let's also change the names of the data to be a bit more descriptive. To do this double click on their name, opening up the editor. Let's name them ``A1 Data``, ``A2 Data``, ``B1 Data``, and ``B2 Data``.

Return to the Container Tree view by clicking on its icon :fa:`sitemap` in the tools panels. Add Recipe B to the project, and Batches 1 and 2 to the recipe. Set Recipe B's type to ``recipe`` and add a string metadata with value ``B`` to it, just as we did for Recipe A.

Edit Recipe B > Batch 1 as before, setting its type to ``batch``, and adding a ``batch`` number metadata with value ``1``. Let's add our data Asset. Because it's already been added to the project all we have to do is associate it to the Container. Click on the :badge:`Add Asset, badge-success` button, and select it from the drop down list, then click the :badge:`Add Asset, badge-success` button again to add it. Save your changes as usual.

Finally let's edit Recipe B > Batch 2. Again setting its type to ``batch``, adding a ``batch`` number metadata with value ``2``, and adding its Asset. We also want to make a note here. Notes allow us to makes remarks directly on our data or analysis. On the day we fabricated this batch the humidity was a bit higher than usual, which we think may have affected the explosive powders. Click the :badge:`Add Note, badge-success` button to add a note. Title it ``Fabrication Humidity`` and make the note

	We noticed an elevated humidity during fabrication of this batch. While all the powders seem normal, it may have an influence on their performance.

Save your changes.


Analysis Scripts
================

We'll now add the analysis Scripts to our project. Go to the Project Scripts view by clicking on the cogs icon :fa:`cogs`. Drag and drop all three scripts into the drop zone. We can change the name and properties of these scripts just as we did for the Assets. Let's give them a bit nicer names:
+ noise-stats.py -> Noise Stats
+ recipe-stats.py -> Recipe Stats
+ recipe-comparison.py -> Recipe Comparison

Let's now associate these Scripts with their respective Containers. We'll start with Recipe A > Batch 1. click on the pen to edit, and click on the :badge:`Add Script, badge-success` button. Select the ``Noise Stats`` Script and save the container. Do the same for the other batches. We'll then repeat the process for both recipes adding the ``Recipe Stats`` Script to them, and finally we'll add the ``Recipe Comparison`` Script to the root container at the top.

Finally we need to add a library dependency to our project. Our Scripts use the `Pandas  <https://pandas.pydata.org/>`_ library, so we need to tell our project about this dependency. Open the Library view by clicking on the book icon :fa:`book`. Pandas is considered a remote library because we haven't uploaded it directly to our Thot account. To add it as a dependency in our project type ``pandas`` into the Name field and select ``Python`` as the language. You can leave the version blank, as we'll use the most recent version. Click the :badge:`Add Library, badge-success` button to add it to our project.

Great! That finished our project set up. We can ensure we have everything set up the way we want by going to the Container Tree view and changing the **Preview** of our Containers. Go through each of the options to verify the Containers have the desired properties and associations.

Let's now save the project by clicking on the save icon :fa:`save` in the tool panel. This will save our project and take us to the project page.

************
Project Page
************

Let's start off by adding a tag to our project. Double click on the Silent Fireworks Container to open its editor. Then double click on the (No tags) section. This opens up the tag editor. Tags can be used to search for different items both within a project and across projects. Let's give our project the tags ``underwater`` and ``low noise``. To do this, enter both values separated by a comma. To save you can either click on the :badge:`Save, badge-success` button, or press :kbd:`Shift + Enter`, just as we did with the noise data Asset before. To close the editor without saving you can press the :kbd:`Esc` key.

Notice now that we are in the Project editor, instead of the Project Creation editor there is no longer a :badge:`Save, badge-primary` button at the bottom of the Container editor. This is because any changes you make are automaitcally saved when you submit them. To close the editor you can either click on one of the view in the tools panel, or click on the close icon :fa:`times-circle` in the upper right hand of the editor.


Analyzing the Project
=====================

Now that our project is all set up, let's finally analyze it. We can choose to analyze just a part of the project, or the whole thing. Let's start off by analyzing Recipe A > Batch 1.

Select its Container by single clicking on it. This activates some of the tools that were disabled before. Click on the Analyze button :fa:`chart-line`
. When the Analysis is done you'll see the new Asset show up in the preview panel on the right hand side of the screen.

Now let's analyze the whole Recipe A subtree. Open the Recipe A Container editor, and click on the :badge:`Analyze, badge-primary` button. Once the analysis is complete we will see the new Assets show up in the Assets section.

Let's open the Container editor for Recipe A. Here we see that we can download the entire container, which will also download all of its children. We can also download individual Assets. 

Click on the Batch 1 child to navigate to it. Here you'll see that we now have two versions of the Noise Statistics Asset that our script created. This is because the Noise Stats analysis ran twice on it: once when we analyzed Batch 1 itself, and again when we analyzed Recipe A. This is one of the key concepts in Thot -- analysis runs from the bottom of the tree upwards, allowing each higher level access to all the Assets below it.

Let's remove all the Assets we've created so far, then analyze the entire project. Click on the trash can icon :fa:`trash` in the corner of the Asset preview card to remove it. You can navigate to Recipe A by scrolling to the top of the Container editor and clicking it in the breadcrumbs navigation, or by exiting the navigator and re-opening it for Recipe A. Let's also remove the Noise Stats Asset for Batch B.

Finally, let's analyze the entire project. Select the Silent Fireworks Container, and analyze it. Let's download the entire project so we can browse all of our Assets. With the Silent Fireworks Container still selected, click the download icon :fa:`download`. Extract the zip file, and browse through the folders. When you download a Container it downloads it as a Local Thot project, which you can learn more about in the :ref:`Local Project: Basics <local_project_basics>` tutorial. 

Take a look at the Recipe Comparison bar chart. Which recipe should we go with?

*******
Summary
*******

In this tutorial we learned the basics of creating and analyzing a Thot project. We began by creating a new project. We created our Container Tree, organizing our project. We added properties, notes, Assets, and Scripts to our Containers. We were able to add Assets both within the Container, and from the Project Assets view. To add Scripts we first added them in the Project Scripts view, then associated them with our desired Containers. Finally, we declared our project's dependencies in the Library view.

Once we saved our project we were taken to the Project view. From here we saw how we could modify our Containers, download Containers and Assets, and analyze our project.
