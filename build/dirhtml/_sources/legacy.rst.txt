===========================================
 Upgrading a Legacy RhostMUSH Installation
===========================================

----------------------------------------
Converting database betwen GDBM and QDBM
----------------------------------------

Ok, if you plan to recompile your game that is using GDBM to QDBM, or visa versa
some bad news.

The databases are NOT COMPATIBLE to each other, at least in the binary form.

Downgrading QDBM to GDBM
========================

.. warning::

   I would NEVER change from QDBM back to GDBM, but if you're set on it these steps:

   You would use the same steps if you plan to move QDBM to GDBM.  I however would
   not do this.  Moving from QDBM to GDBM is a huge step backwards.  Seriously,
   don't do it unless you have absolutely no other recourse.

   IF you plan (for whatever reason) to move from QDBM to GDBM, you should verify
   the following

#.  You have on a 64 bit system, no object that has more than 400 attributes on it.
#.  You have on a 32 bit system, no object that has more than 750 attributes on it.
#.  Any CONTENT of any attribute must be below 4000 characters in length.
#.  Once you have that done, you may follow the procedures below on converting (upgrade) from GDBM to QDBM.  This works the same as converting (downgrading) QDBM back down to GDBM

Upgradging GDBM to QDBM
=======================

Now, if you've kept reading and plan to convert your GDBM database to QDBM great news!
It's more stable, it's faster, and lets you have far more flexibility.

So, BEFORE YOU RECOMPILE YOUR CODE.  This is what you have to do.

While logged in to your mush, issue the following commands
----------------------------------------------------------

 #.  @dump/flat    -- This will make a flatfile dump of your MUSH database
 #.  wmail/unload  -- This will make a flatfile dump of your MAIL database
 #.  @areg/unload  -- If you use the AutoRegistration engine, this dumps it
 #.  newsdb/unload -- If you use the hardcoded news/bbs engine.  This dumps it

Verify the files exist
----------------------

 #.  Server/game/data/netrhost.db.flat
 #.  Server/game/data/RhostMUSH.dump.folder
 #.  Server/game/data/RhostMUSH.dump.mail
 #.  (Optional) Server/game/data/RhostMUSH.areg.dump
 #.  (Optional) Server/game/data/RhostMUSH.news.flat

Shutdown the MUSH
-----------------

@shutdown your mush

From the Server directory
-------------------------

#.  make clean

#.  make confsource

   #.  Select QDBM and if you wish at this time increase your LBUF size

   #.  Select any other options you may want

#.  (r)un and let it compile.

.. todo::

   Figure out why that asterisk is there.

#.  Main DB: Delete (rm) the following files (from Rhost/Server/game/data)::

     netrhost.gdbm*
     netrhost.db
     netrhost.db.new
     netrhost.db.new.prev

#.  Mail DB: Delete (rm) the following files (from Rhost/Server/game/data)::

     RhostMUSH.folder.dir  
     RhostMUSH.folder.pag  
     RhostMUSH.mail.dir  
     RhostMUSH.mail.pag  

#.  (Optional) AutoReg DB: Delete (rm) the following files (from Rhost/Server/game/data)::

     RhostMUSH.areg.dir  
     RhostMUSH.areg.pag  

#.  (Optional) News/BBS DB: Delete (rm) the following files (from Rhost/Server/game/data)::

     RhostMUSH.news.dir
     RhostMUSH.news.pag

From the Server/game directory
------------------------------

#.  Load the database::
    
    ./db_load data/netrhost.gdbm data/netrhost.db.flat data/netrhost.db.new

#.  Start the MUSH back::
    
    ./Startmush

While logged into the mush issue the following commands
-------------------------------------------------------

#.  Load in the mail database::

     wmail/load

#.  (optional) Load in the autoreg database::

     @areg/load

#.  (optional) Load in the news/bbs database::

     newsdb/load

Verify that you have QDBM running and your valid values
-------------------------------------------------------

#.  @list options system#.  @list options (spammy)

-----------------------------------
Updating RhostMUSH prior to 3.9.5p2
-----------------------------------

Ok.

So you're running an old RhostMUSH.

One prior to 3.9.5p2 and want to take advantage of the new
format of the Makefile and the automated mysql stuff and
all the other goodies that isn't really (easilly) done
with just patch.sh.

Well, you're in luck.  It is actually fairly easy to do.

This is what you have to do.

First thing's first.

#.  Log into your existing mush.  Let's make current backups
    of all your flatfiles.  Issue::

     @dump/flat
     wmail/unload
     @areg/unload
     newsdb/unload

#.  Shutdown your game::
   
     @shutdown

#.  Make an image of all your current backed up files.  From The Server/game directory you would type::

    ./backup_flat.sh -s

.. note::

   Please remember the '-s' to the ./backup_flat.sh.

#.  Make note of the most recently created file in the directory Server/game/oldflat.  It's usually named something like::

     RhostMUSH.dbflat1.tar.gz

.. note::

   You will need this file later.

#.  Rename your 'Rhost' directory to something else.  This is the directory that you have containing the 'Server' directory.  Name it anything you want other than 'Rhost'.  For those not used to unix you would type::

     mv Rhost Rhost_old

#.  Pull in the latest Rhost.  You would type::

     git clone https://github.com/RhostMUSH/trunk Rhost

.. note::

   You would type this in the same directory you have renamed your old 'Rhost' directory

#.  go into the Rhost/Server directory.   Type::

     make confsource

.. note::

   Select what options you want (including the mysql and other goodies) then compile it (also within the menu, it's the 'r' option).

#.   Once your game is compiled and ready to go you need to copy in the data from your old game.  Copy the RhostMUSH.dbflat1.tar.gz we mentioned in step #4 to the Server/game directory of your NEW GAME DIRECTORY.  From within the 'game' directory of your current game you should be able to issue (if you named the old one Rhost_old). Again this needs to be done FROM YOUR Server/game directory!!!

   #. cp netrhost.conf netrhost.conf.orig

   #. cp ../../Rhost_old/Server/game/RhostMUSH.dbflat1.tar.gz .

   #. tar -zxvf RhostMUSH.dbflat1.tar.gz 

   #. Compare your current netrhost.conf to the default one that came with the source (that you renamed to netrhost.conf.orig).  Likely the only sections you have to add to your current netrhost.conf (that came with your RhostMUSH.dbflat1.tar.gz archive), will be toward the end, with the include rhost_ingame.conf and rhost_mysql.conf.  Depending on how old your game is coming from you may need to add more options.  Any config option that is the same between the netrhost.conf files do not have to be copied over, and you want to keep your custom settings (like don't port or other stuff you have already customized).

   #. Load in your flatfile information::

       ./db_load data/netrhost.gdbm data/netrhost.db.flat data/netrhost.db.new

   #. Your ./Startmush should re-index all your txt files you originally made::

       ./Startmush

   #.  In your game type the following as an immortal or as #1.

      #.  Load in your mail flatfile::

           wmail/load

      #.  Load in your autoregistration flatfile (if available)::

           @areg/load

      #.  Load in your hardcoded bbs flatfile (if available)::

           newsdb/load

#.  You should be good to go on a current directory structure for Rhost.  Enjoy!


--------------------------------------------
Adding MySQL to RhostMUSH older than 3.9.5p2
--------------------------------------------

MySQL is now native in RhostMUSH as of 3.9.5p2.

.. warning::

   To autodetect it, YOU MUST HAVE mysql_config installed and running on your server.  Without this, even if you have mysql db installed it won't be able to recognize the parameters you will need for it and will thus fail.  Please check your linux distribution to see what packages are needed to install mysql_config.

Download the git repository to a seperate directory so that you can
copy over the files that it requires you to.

Suggestion::

   git clone https://github.com/RhostMUSH/trunk ~/tmprho

If you are patching UP from an older version, you need to update
the following files:

#.  update your src/Makefile to the one in the 3.9.5p2+ repo
    ( cp ~/tmprho/Server/src/Makefile ~/Rhost/Server/src/Makefile )
#.  update your bin/asksource.* files to the one in the 3.9.5p2+ repo
    ( cp ~/tmprho/Server/bin/asksource.* ~/Rhost/Server/bin/ )
#.  append 'include rhost_mysql.conf' BEFORE the rhost_ingame.conf file
    and before the section that says 'define local aliases' toward the end of
    your netrhost.conf file.
    ( edit your ~/Rhost/Server/game/netrhost.conf file )
#.  copy the game/rhost_mysql.conf file from the 3.9.5p2+ repo 
    ( cp ~/tmprho/Server/game/rhost_mysql.conf ~/Rhost/Server/game/ )
#.  The following lines have to be REPLACED/CHANGED in local.c ( toward the top ):
    ( you may edit this or copy the one from the other distro )
    ( do either:  edit ~/Rhost/Server/src/local.c )
    (        or:  cp ~/tmprho/Server/src/local.c ~/Rhost/Server/src/local.c )
     
.. note::

   IF REPLACING/CHANGING local.c COPY BELOW

.. code-block:: c

   /* Called when the mush starts up, immediatly prior to the main game
   * loop being entered. By this point all databases are loaded and
   * all variables configured.
   */
   #ifdef MYSQL_VERSION
    extern void local_mysql_init(void);
    extern int sql_shutdown(dbref player);
   #endif

   #ifdef SQLITE
    extern void local_sqlite_init(void);
   #endif /* SQLITE */

   void local_startup(void) {
   #ifdef SQLITE
    local_sqlite_init();
   #endif /* SQLITE */
   #ifdef MYSQL_VERSION
    local_mysql_init();
   #endif
    load_regexp_functions();
   }

   /* Called immediatly after the main game loop exits. At this point
   * all databases and variables are still configured
   */
   void local_shutdown(void) {
   #ifdef MYSQL_VERSION
    sql_shutdown(-1);
   #endif
   }


#.  Issue 'make clean' then make confsource to rebuild using the latest
    builder script to build in the mysql changes.
