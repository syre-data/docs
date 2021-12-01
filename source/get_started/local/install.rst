.. _local_intro:

########################
Thot Local: Installation
########################

Congratulations! You've just been hired as the head of the R+D department at Puzzles Underwater Fireworks company. The city's aquarium just hired us for their annual New Year's Eve extravaganza, and they want to do something extra special this year: fireworks for the fish. Luckily, our team has been working hard for the past six months on two new recipes for silent explosions. A perfect solution so the fish don't get scared. Looks like your first project will be to compare the two recipes to see which is quieter. Good Luck!

To perform our analysis we'll use Thot. Thot offers three interfaces: the Command Line Interface (CLI), Thot Desktop, and Thot Web. The CLI and Thot Desktop are both run from your own computer, while Thot Web runs on Thot's servers and provides additional functionality.


.. raw:: html

	<h2>Getting Thot</h2>


Thot requires Python (v3) which you can get from the `official Python site <https://www.python.org/downloads/>`_. 

After installing Python you can install Thot and the CLI by running

.. code-block:: bash

	python3 -m pip install thot-cli

from your terminal. This will install both the ``thot-data`` and ``thot-cli`` packages.

**Desktop**

#. Download the Thot Desktop app, following the links below:

	* `Windows 10 <https://thot-data.com/downloads/desktop/windows10/ThotDesktopSetup.exe>`_
	* `Mac Catalina <https://thot-data.com/downloads/desktop/mac_catalina/ThotDesktop.dmg>`_
	* `Ubuntu 21+ <https://thot-data.com/downloads/desktop/ubuntu21/ThotDesktop.deb>`_
	* `Ubuntu 20+ <https://thot-data.com/downloads/desktop/ubuntu20/ThotDesktop.deb>`_
	* `Ubuntu 16+ <https://thot-data.com/downloads/desktop/ubuntu16/ThotDesktop.deb>`_

#. Install Thot Desktop

	* **Windows 10:** Run ``ThotDesktopSetup.exe``. If you get a security warning, click on the `More info` button, then click the `Run anyway` button that appears at the bottom.

	* **Mac:** Double click on ``ThotDesktop.dmg`` then drag the ThotDesktop icon into the Applications folder. If a warning stating ``Thot Desktop cannot be opened because the developer cannot be verified`` click cancel, open ``Preferences > Security & Privacy`` and at the bottom of the page select ``Open Anyway`` next to the warning for ThotDesktop.

	* **Ubuntu:** From the terminal run 

		.. code-block:: bask

			sudo dpkg -i ThotDesktop.deb


.. rst-class:: centered

	.. panels::

		**Quick Start**
		^^^^^^^^^^^^^^^

		:fa:`clock` 15 minutes

		Learn the basics of Thot to get up and running.

		+++

		.. link-button:: quick_start
			:type: ref
			:text: Get Quick Started
			:classes: btn-outline-success btn-block stretched-link

		---

		
		**Tutorial**
		^^^^^^^^^^^^

		:fa:`clock` 60 minutes

		Implement a Thot project from scratch to learn all of Thot's functionality.
		
		+++

		.. link-button:: tutorial/containers
			:type: ref
			:text: Get Started
			:classes: btn-outline-primary btn-block stretched-link


.. note::
	We will use Pandas for the analysis. To get Pandas you can `visit their website  <https://pandas.pydata.org/getting_started.html>`_.

..
	.. seealso::
	For additional functionality use our web verison.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   quick_start
   tutorial/containers
   cheat_sheet
   utilities