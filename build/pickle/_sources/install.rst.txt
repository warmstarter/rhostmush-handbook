.. _installing-rhostmush:

======================
 Installing RhostMUSH
======================

.. contents:: Table of Contents
   :local:
   :backlinks: top

.. _rhostmush-requirements:

----------------------
RhostMUSH Requirements
----------------------

.. _system-requirements:

System Requirements
===================

* Operating System: Unix-like

  - Almost any variant of Unix or Linux should compile cleanly and run
  - Preliminary support for Windows with an equivalent development environment

* Memory: 12-100 MB

  - Depending on size of database and buffers, as well as selected options
  - 1 GB (memory and swap combined) is the minimum required to compile

* Storage: 100 MB and up

  - Depending on size of database and backup retention policy

.. note::

  Third-party applications can use considerably more resources

.. _software-requirements:

Software Requirements
=====================

RhostMUSH is a Linux or Unix based server software that runs as a daemon on the host.
In order to build this software, you will need the bare minimum of the ability to run 'make' commands.

Package requirements are as follows:

* bash/ksh/dash (or compatible shell - for use with build menu)
* glibc and gcc/clang (compiling the code)
* git (to clone the source and maintain patches)
* libcrypt (for password encryption - this is usually standard on unix based systems)

Optional Packages
-----------------

RhostMUSH also offers optional linking and library attachments.
For some of these libraries it will attempt to do auto-detection,
but in a worse case scenario, there exists override hashes in the menu to disable options it thinks exist that do not.

Optional packages are as follows:

* libpcre (if you wish to use system pcre libraries instead of the built-in ones)
* mysql client & mysql_config (required for mysql capabilities)
* openssl dev libraries/headers (for MUX password compatibility, and digest() and advanced cryptology functionality.
* ruby/perl/python/etc (for custom interactive dynamic custom functions with the execscript() feature)
* sqlite3 libraries (required for sqlite capabilities)

.. _hosting-requirements:

Hosting Requirements
====================

* You will need a stable host and access to open a single port number of your choice on the firewall.
* Most games choose a number between 1025 and 9999, by convention.
* Please make sure your debug_id matches the port number + 5.

  - So if your port is 1234, your debug_id will be 12345.
  - The debug_id is for use in the API daemon that runs Rhost as a container to keep track of heap, stack, and execution location.

.. _obtaining-rhostmush:

-------------------------------
Obtaining RhostMUSH Source Code
-------------------------------

The only official source for obtaining RhostMUSH is through the 'RhostMUSH'
github account. If the source code was obtained in some other manner, there
are potentially any number of unintentional or intentional issues that you
might run into.

The recommended method of obtaing RhostMUSH is to clone it's git reposistory::

  git clone https://github.com/RhostMUSH/trunk Rhost

It is possible, but not recommended to download RhostMUSH via a web browser::

  https://github.com/RhostMUSH/trunk/archive/master.zip

.. note::

  This documentation generally assumes that you obtained the RhostMUSH source
  code by cloning it's git repository or at the very least downloading an
  archive of the source code from the GitHub website. It also assumes that
  all commands on the server are being run from within the main directory of
  that cloned git repo or equivalent.

-------------------------
Options for making a MUSH
-------------------------

There is a *lot* of options once your start making your MUSH, but there are
also a few big choices right as you get started making a MUSH. No matter which
choices you ultimately make, there are certain things you will need to know how
to do. This chapter is going to walk you through making the simplest possible
version of RhostMUSH. It's going to show you the things you would have to do
no matter which choices you were making.

In the process of making that simplest possible RhostMUSH you'll also learn
what the basics of those choices are and when and how you would make them.
Later chapters will get much more into all of those choices, but they will also
assume you know everything in this chapter already, or at least have it as a
handy point of reference.

While there are lots of little options, there are three big areas where you
make those choices.

Compile time options
====================

One of the first steps of making a MUSH or really any computer program is
to compile the source code. This takes what's basically text files full of code
and turns them into a program you can run. Within that source code are a
number of options to choose from, but any time you want to change one of them,
you have to recompile the source code and then restart the MUSH.

These choices are typically made through the ``confsource`` menu which you'll
be seeing momentarily. There are some pretty big choices here from whether or
not you want hardcoded +help and comsys, deciding between a more secure server
and certtain powerful but potentially dangerous MUSHcode options, and then
whether or not you want to be able to connect to a variety of external programs
like databases, webservers, and even other programming languages.

Configuration file options
==========================

While there are some options in RhostMUSH that can only be changed through
recompiling the source code, there are way more options that can be changed
without having to recompile. These choices are mostly made through the
``netrhost.conf`` file. Whenever a MUSH starts up or gets rebooted, it's
going to look to what's in that file. A few of those choices relate to
further configuring the choices you made with ``confsource``

The ``netrhost.conf`` file has some aesthetic options like what if anything
it says when the database is being saved or whether or not your MUSH will
allow ANSI color, both in general, but also in things like people's names.
It has a lot of very esoteric options for tuning the performance and safety
of your MUSH. It also is where you define things that connect to your database
like your master room and guests. It let's you determine which powers your
staff does or does not have, and it's also where you have an option to change
the password for #1 should you forget it. There are ways to change some of
these options from within the MUSH and even have those changes become new
defaults that survive a reboot. One thing you set there that you definitely
can't change from within the MUSH, is which port it runs on.

Starting database options
=========================

This last big choice is one that you probably are well aware of at least some
of the things it allows for, mostly because the database is basically where
everyone on a MUSH lives. Most of the choices you ever make about your MUSH
will happen in the database and it's something that's basically always going
to be changing in more ways than any one person could follow. No matter how
vast the database of a MUSH gets, they all started somewhere, and that's the
last big choice you have to make.

Depending on how you look at it, there's somewhere between thousands of choices
and two choices for a starting database. What I mean is that you have the
choice of starting with a brand new database to populate, only a room (#0) and
you (#1), even the Master Room is something you'd have to add to it. The other
option is to import an existing database, though to choose that option you'd
also have to have access to an existing database.

Besides the brand new database that can be made on-demand, RhostMUSH comes with
two databases that you can use to get your start. One is called 'Minimal' and
the other is called 'Ambrosia' after the lead RhostMUSH developed that made it.
Despite the name, they're both fairly minimal, there's no grid in either, but
what you get is a lot of pre-installed softcode and security, as well as a
``netrhost.conf``` file that has been tuned to work well with it. Even if you
don't use those databases you can take ideas for the ``netrhost.conf`` file for
tuning your MUSH or even use some RhostMUSH commands to import that softcode
into your database.

The Choices We Make
===================

Well, not you're aware of those three big choices, what they are, and where
you'll run across them. Later in this Handbook we'll be going through those
choices in-depth. In this chapter, what we'll be doing is using the default
options for for ``confsource`` and ``netrhost.conf`` and a brand new database.
Those options and that blank slate are necessary so that you have in front of
you a working MUSH with only #0 and #1 and get shown the way of building it
into whatever is your dream MUSH, and I know we all have one.

There will be a chance to make all those other choices later, in fact that
will be happening very soon. There's a lot of very interesting choices that
you can make with RhostMUSH, too many for anyone to ever be able to use them
all. If you don't start with mastering the basics, you'll never end up knowing
what are the most RhostMUSH options. I can't tell you what they are, it's truly
something you have to discover on your own. Remember, you want to build your
dream MUSH, not mine.
  
.. _compiling-rhostmush:

-------------------
Compiling RhostMush
-------------------

Setup directory permissions
===========================

In order to both compile and run, all of the RhostMUSH files and directories
need to have the proper permissions set. If you obtained the source code
directly from GitHub, it is likely that this step is not required, but there
is no harm in running it anyway::

 ./dirsetup.sh
 
If you did NOT obtain the source code directly from GitHub, it is possible that
even the above script will fail to run with 'permission denied' or similar
errors. It is recommended that you obtain the source code from there, but if
for whatever reason this is not an option, manually adjust your permissions
and then re-run the automated permission script::

  chmod +rx bin/*.sh src/*.sh game/*.sh game/Startmush game/db_*
  ./dirsetup.sh


Compile the source code
=======================

Once the source code has been obtained and the proper file and directory
permissions have been set, the RhostMUSH source code is ready to be compiled.
This is typically done through an interactive program where you configure the
options you want to have available to your installation::

  make confsource

The confsource Menu
-------------------

Troubleshooting compile errors
------------------------------

Should this result in an error, a script has been included to correct the most
common errors, after which you can once more try to compile::

  ./bin/script_setup.sh
  make confsource

Once the compile process successfully complete, you should be able to start-up
your new RhostMUSH server. If it complains about missing binaries make sure
they are linked. The provided script will fix this issue, and is not harmful
to run in any situation::

   make links

Recompiling the source code
---------------------------

If you plan to use ``make confsource`` to recompile your source, you should first
issue a 'make clean' before re-issuing a ``make confsource``.  ``make confsource``
remembers the last options you used.

A failure to issue ``make clean`` prior to re-compiling with ``make confsource`` or
re-compiling with ``make source`` can potentially leave stale object files which
may cause unforseen issues when running code, including but not limited to 
random crashes.  Generally whenever recompiling it's good to always make clean
first.

.. note::

  You may also issue ``make source`` if the ``Makefile`` is already defined how
  you want it to be.  Please remember to ``make clean`` before ``make source```
  whenever you alter the code or import new source code.


Note about Compiling
====================

If you are importing a MUX2 flatfile, make ABSOLUTELY SURE that you select
mux passwords as a compatibility option, or you will NOT BE ABLE to log in
to players as the password will not be recognizeable.

Make sure to keep QDBM selected as it's a much more stable database engine
that does not have attribute limit restrictions like GDBM does.

If you are converting from a Penn, TinyMUSH, or MUX database, make sure you
drill down into the LBUF section and select, at minimum, 8K lbufs.  You likely
want that anyway as it gives you far more room for attribute content storage.

You can go up to 32K safely.  While 64k is safe and does work, there are issues
with networking and older routers that use a 32K TCP buffer size that can
at times cut off the data as overflow resulting in output to the end-point
players not receiving their data.  So it is strongly recommended not to go
above 32K in lbuffer size.

Go ahead and select 64 char attributes.  It allows you to have 64 characters
for attribute names.  It's handy to have.

If you wish at this point to set up mysql and/or sqlite, you  may do so.
Yes, you can use them in parallel without any issue.

.. _ansible-install:

------------------------------------
Installing using an ansible playbook
------------------------------------

To begin, you will run the following command in a directory that will house your game::

   git clone https://github.com/RhostMUSH/trunk Rhost

You may also just run the yml file and ansible (ansible-playbook) to install your RhostMUSH engine::

   wget https://raw.githubusercontent.com/RhostMUSH/trunk/master/rhostinstall.yml
   ansible-playbook rhostinstall.yml

This downloads the latest stable version of the code, bringing with it all patches and scripts, documentation and support tools that you will need.

------------------------------
Starting a Newly Compiled MUSH
------------------------------

Configuring the game
====================

When setting up a mush for the first time, make sure you
have all the files configured correctly.  This is with using
the following file for configuration::

   - netrhost.conf

Starting the game
=================

Once done, you start up the system with the following command::

   - [sh/csh] ./Startmush
  
  It will prompt you to start a new db if it doesn't find one.
  
  You may also do the commands individually::

     [csh] netrhost -s netrhost.conf >& netrhost.log &
     [sh]  netrhost -s netrhost.conf > netrhost.log 2>&1 &

First login to the game
=======================

Once started, log in the #1 character (Wizard) with it's appropiate
password (no, not 'potrzebie', but 'Nyctasia').  There were private
reasons for the password change.

Once in, do a @shutdown to save the database.  Then you can run Startup
normally.   You may make a backup of your database at anytime on-line by
utilizing the @dump/flat option.  A script comes with this distribution
that allows the ability of auto-archiving your database for a configurable
number of backups.

-------------------------------------
Creating RHostMUSH with a Provided DB
-------------------------------------

Important before you actually start building
============================================

The main parts of making your RhostMUSH, easy pleasy:

#.  The stunnel directory contains TLS/SSL connectivity.  This has to be linked to another port and will tunnel to the mush port.  The README file explains how to set up and configure your TLS/SSL connection.
#.  ./patch.sh -- This makes sure you have the latest code.  If you got this by git clone https://github.com/RhostMUSH/trunk then you can ignore patching.  You can use ./patch.sh at any time to update your code.  It ignores local.c incase you make your own modules.
#.  make confsource.  Yup, it's menu driven, nifty eh?

    #. Options you may want to select (other than the defaults):
    #. 5  (%c is selected by default, but choose %x as well for MUX/TM3 compat)
    #. 9  (if you want $commands to require the COMMAND flag)
    #. 16 (if you want a wider WHO listing like older versions of MUX)
    #. 22 (if you're converting a TinyMUSH3 or TinyMUX/MUX2 flatfile)
    #.  24 (if you have issues with -lssl not being found)
    #. B3 (for 64 character attribute names)
    #. B6 (select 8K for Penn/MUX2/TM3 default, up to 32K.  64K is network intensive)
    #. B5 (will be autoselected if you choose 8K or more.  Pick this anyway)
    #. B4 (if you have sqlite libraries and wish to use this)

#.  'r' to compile with the settings you selected.  
#.  Modify your netrhost.conf file as specified.  Make sure to align your port and debug_id as shown in the netrhost.conf file.
#.  If you wish to port in an old flatfile, please refer to the readme directory on how to port your flatfile in (README.DBLOADING).

Using the prebuilt flatfile
===========================

There are pre-loaded flatfile databases you can use at this point.  The netrhost.db.flat
and corrisponding netrhost.conf file will be located in the minimal-DBs/minimal_db directory.

You may auto-load the minimal db and corresponding netrhost.conf file with the command::

    ./minimal.sh

This is ran from within the 'game' directory.  Once this is ran, you will need
to customize the netrhost.conf file for your purposes.  The port and debug_id must
be changed at the very least.  Keep the debug_id coordinated to the port as described.

To load a prebuilt flatfile
---------------------------

1.  Make a backup of your existing netrhost.conf file::
    
       cp game/netrhost.conf game/netrhost.conf.backup

2.  Copy the netrhost.conf file into your game directory::

       cp -f ./minimal-DBs/minimal_db/netrhost.conf ./game/netrhost.conf

3.  At this point you can modify your netrhost.conf file settings in your game directory.
    Using an editor modify the 'port' and 'debug_id' respectively in your netrhost.conf as state.
    The 'port' will be the port the mush listens on, the debug_id is for the debug-stack and is
    your port with a '5' at the end.  So if your port is 4444, the debug_id is 44445

4.  Load in the flatfile into the mush (You could do this in the Startmush as well)
    Manually::

       cd game
      
    ./db_load data/netrhost.gdbm ../minimal-DBs/minimal_db/netrhost.db.flat data/netrhost.db.new dwF
     
    Start your mush::

       ./Startmush

    This will load the db that you loaded. 

    ---------------OR-------

    From Startmush when prompted, hit <RETURN> for searching then select the number of the netrhost.db.flat that is listed as ~/minimal-DBs/minimal_db/netrhost.db.flat::

        ./Startmush

---------------------------------------------------------------
Almost Backwards Instructions for Compiling and Starting a MUSH
---------------------------------------------------------------

1.  You can modify your netrhost.conf file settings in your game directory.
    Using an editor modify the 'port' and 'debug_id' respectively in your netrhost.conf as stated.
    The 'port' will be the port the mush listens on, the debug_id is for the debug-stack and is
    your port with a '5' at the end.  So if your port is 4444, the debug_id is 44445
2.  Start your mush::

    --> ./Startmush

You can use the 'vi' editor or 'nano' if you like a more menu driven DOS like experience.
You can of course use any other editor you're familar with.

For a more thorough understanding of how to set things up, keep reading!

If you have syntax issues running 'make config', 'make confsource' 
or 'make bugreport' please run the script: ./bin/script_setup.sh

Now... things you may need to do on errors.

-----------------------------------------------
Basic Instructions for starting a new RhostMUSH
-----------------------------------------------

Manual configuration of source code
===================================

To do manual configuration (skip if the previous step worked for you) And yes, this is a bit of a pain in the bottom, hopefully you will not need this.

You need the following definitions defined to make this work:

#. TINY_U, USE_SIDEEFFECTS, MUX_INCDEC, ATTR_HACK
#. (u()/u2() switched)
#. (sideeffects)
#. (inc()/xinc() switched)
#. (support for _/~ attribs)
	
You only need to do this if you received the RhostMUSH src.  If you received a binary, continue on to the next part.

To compile the code, just type 'make confsource'.  It will prompt you with settings on what you need to do.  If you just want to quickly hand edit the Makefile, it is in the directory src (full path src/Makefile).  Then you may just run 'make source', if you so choose to hand-edit the Makefile.

After the compile process is done, type 'make links'!

Loading a database for your MUSH
================================

You now have a choice of optionally starting at a provided database or starting from scratch.

Option: Only perform these steps if using a provided database
-------------------------------------------------------------

Copy an existing flatfile and corresponding netrhost.conf file Default provied example::

   cp game/netrhost.conf game/netrhost.conf.backup
   cp -f minimal-DBs/minimal_db/netrhost.conf game/netrhost.conf
   cd game
   ./db_load data/netrhost.gdbm ../minimal-DBs/minimal_db/netrhost.db.flat data/netrhost.db.new

Configure the netrhost.conf file for your MUSH
++++++++++++++++++++++++++++++++++++++++++++++

        Go into the game directory and modify the netrhost.conf file
	The next step is configuring the mush to your config standards.
	There is a file in the game subdirectory called 'netrhost.conf'.
	You hand-edit this file and just follow what it says each 
	one does.  It's very well documented and should give you
	great details on what to edit.  For most things, you can
	feel comfortable to stick with the defaults unless you wish
	to change them.  The port and debug_id need to be changed.

-----------------------------------------------
Start a  MUSH and logging on for the first time
-----------------------------------------------

From the game diretory issue::

    ./Startmush 

To login::

    co Wizard Nyctasia


Option: Things to do once you have connected if you did NOT use a provided database
===================================================================================

#.  @dig your master room and in your netrhost.conf file define master_room to this dbref (without the #.  So like master_room 2)
#.  Create an immortal holder charater (@pcreate then @set immortal) Feel free to set up holder characters for all the bittypes which are: GUILDMASTER, ARCHITECT, COUNCILOR, WIZARD, IMMORTAL
#.  @chown/preserve the master room and #0 to the immortal holder character.
#.  Log into the immortal character
#.  @pcreate all your guest characters and set them up properly.  My suggestion::

       @dolist lnum(1,10)={@pcreate Guest##=guest;@set *Guest##=guest;@desc *Guest##=A guest player.;@adisconnect *Guest##=home;@lock *Guest##=*Guest##}
       
       @list guest will show your guest characters and if they're set up properly.

#.  Any master room code you load in from your immholder character (or @chown/preserve to it) The readme directory has softfunctions.minmax that has MUX/Penn compatability functions and comsys.  All other softcode (like mail wrappers) can be found on https://github.com/RhostMUSH/trunk in Mushcode.
#. Setup new character, staff, and take tasks that can only be accomplished by #1
#. Set up any other characters you want.  Anyone immortal can issue @function, @admin, or anything #1 can do.

.. todo::

   Figure out what they were trying to say by having those two sentences right after each other.

--------------------------------------
Customtize the textfiles for your game
--------------------------------------

   All connect.txt and customized files can be found in the ~/Server/game/txt directory.  There is a 
   README file there that explains their purposes in more detail.  You can see more information on
   all files and how they inter-relate with 'wizhelp file'.

---------------------------------
Three Options for Starting a MUSH
---------------------------------

The RhostMUSH Git Repository comes with three options for starting your Mush.

.. todo::

   Well, there's also some other pre-existing DB or upgrading, so let's try to make this a little more coherent.

Option 1: Creating a new game with a blank database
===================================================

  Modify your ./game/netrhost.conf file or what settings you want.
  Don't feel overwhelmed, it's all very well documented.

Options 2: Creating a new game with Ambrosia's default database
===============================================================

Follow minimal-DBs/Amb-MinimalRhost/IMPORTANT_README
  
The netrhost.conf file you will copy is in minimal-DBs/Amb-MinimalRhost/game
Copy this netrhost.conf file into your 'game' directory.

You will want the custom txt files under Amb-MinimalRhost/txt in your game/txt directory and to mkindx all the txt files.  You can run ./Startmush -i to index.
  
When ./Startmush prompts you to load a flatfile, say 'yes' and hit <RETURN> to have it search for flatfiles, then select netrhost.db.flat from under the minimal-DBs/Amb-MinimalRhost directory.
  
The main steps to make sure you do for ~/Server/minimal-DBs/Amb-MinimalRhost/netrhost.db.flat -- Ambrosia's secure and featured minimal db

#. Use the matching netrhost.conf file under the Amb-MinimalRhost/game directory
#. Load in the settings specified in the Amb-MinimalRhost/bin directory.

   #. Copy this file into your ~/Server/bin directory
   #. From 'Server' directory type: make clean
   #. From 'Server' directory type: make confsource and 'l'oad option 0
   #. Specify any -additional- options you want at this point.
   #. Recompile your code
#. Copy the files in Amb-MinimalRhost/game/txt into your ~/Server/game/txt directory
#. from your ~/Server/game txt file run on each of the txt files::

      ../mkindx <txtfile>.txt <txtfile>.indx

.. note::

      Where <txtfile> is the name of the file (minus the .txt extension)

#. If running, @reboot your game.

Option 3: Creating a new game with the generic default database
===============================================================

  Copy the netrhost.conf from minimal-DBs/minimal_db to your game directory.
 
  When ./Startmush prompts you to load a flatfile, say 'yes' and hit <RETURN>
  to have it search for flatfiles, then select netrhost.db.flat from under
  the minimal-DBs/minimal_db directory.

------------------
Starting your MUSH
------------------

Once you have used one of these three methods to obtaina database, you can start your mush up.
At this point type from the game directory::

    ./Startmush

.. todo::

  Considering this was already mentioned earlier in other parts, yeah this all needs to be a bit more coherent and focused.
  Check to see if there are other install bits not yet even integrated here.
