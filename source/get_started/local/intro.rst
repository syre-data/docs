.. _local_intro:

#################
Thot Local: Intro
#################

Congratulations! You've just been hired as the head of the R+D department at Puzzles Underwater Fireworks company. The city's aquarium just hired us for their annual New Year's Eve extravaganza, and they want to do something extra special this year: fireworks for the fish. Luckily, our team has been working hard for the past six months on two new recipes for silent explosions. A perfect solution so the fish don't get scared. Looks like your first project will be to compare the two recipes to see which is quieter. Good Luck!

To perform our analysis we'll use Thot. Thot offers three interfaces: the Command Line Interface (CLI), Thot Desktop, and Thot Web. The CLI and Thot Desktop are both run from your own computer, while Thot Web runs on Thot's servers and provides additional functionality.

************
Getting Thot
************

Thot requires Python (v3) which you can get from the `official Python site <https://www.python.org/downloads/>`_. 

After installing Python, you can install Thot and the CLI by running

.. code-block:: bash

	python -m pip install thot-cli

This will install both the ``thot-data`` and ``thot-cli`` packages.

**Desktop**

#. Download the Thot Desktop app, following the links below:

	* `Windows 10 <https://www.dropbox.com/sh/82zyipnf4giw7na/AABLx-ozn46hqPqU2PafLSnta?dl=0>`_
	* `Mac Catalina <https://www.dropbox.com/sh/wo6pkc1bpptb2hz/AABelJU5JUVyvubUbH2zYT9Ma?dl=0>`_
	* `Ubuntu 21+ <https://www.dropbox.com/sh/vh9f4f0pndcxxyl/AADC5gwLqbEJ7Nevaj1diVDPa?dl=0>`_
	* `Ubuntu 20+ <https://www.dropbox.com/sh/nabl73zkiugxv6o/AADU820YeHbdz8MBk3pVJ1mSa?dl=0>`_
	* `Ubuntu 16+ <https://www.dropbox.com/sh/dzekrad8lutr4wa/AADDDgI_aBH0ZvDmh-xOtgfga?dl=0>`_

#. Unzip the folder.
#. Install Thot Desktop

	* **Windows 10:** Run ``ThotDesktopSetup.exe``. If you get a security warning, click on the `More info` button, then click the `Run anyway` button that appears at the bottom.

	* **Mac:** Double click on ``ThotDesktop.dmg`` then drag the ThotDesktop icon into the Applications folder.

	* **Ubuntu:** From the terminal run 

		.. code-block:: bask

			sudo dpkg -i target/ThotDesktop.deb

.. note::
	We will use Pandas for the analysis. To get Pandas you can `visit their website  <https://pandas.pydata.org/getting_started.html>`_.

.. seealso::
	For additional functionality use our web verison.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   containers
   assets
   scripts  
   summary
   cheat_sheet
   utilities
