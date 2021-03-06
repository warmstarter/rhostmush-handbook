=================
 Troubleshooting
=================

------------------------------
Reporting bugs or getting help
------------------------------

If you find any bugs or problems, notify one of the developers of RhostMUSH and
a patch or workaround will be made available as soon as possible.  Current
developers are:  Seawolf, Thorin, Ashen-Shugar, Lensman, Kale, Mac, Zenty,
Ambrosia, Amos, and Morgan.  They can be found around the net.

Troubleshooting issues with starting up
=======================================

Problem: If it says the shared ID is already in use 
---------------------------------------------------

A1: please verify that it is the right shared debug_id in your netrhost.conf file

A2: Force a start by running::

  ./Startmush -f

Problem: Your log file is massive and your mush is running
----------------------------------------------------------

A1: To rotate this use the @logrotate command. See wizhelp on @logrotate

Problem: The database flatfile you're loading can't load because a db is already defined
----------------------------------------------------------------------------------------

A1: remove netrhost.db* and netrhost.gdbm* from your data directory

Problem: The mail database won't load and mail shows 'offline'
--------------------------------------------------------------

A1: from within the MUSH run::

  wmail/load 

-------------------------
Stack limit and debugging
-------------------------

Rhost uses a stack limit in the debug monitor.

This stack limit is set to a reasonable amount of 1000.
This is defined in the debug.h file in the hdrs directory.

This will directly impact the function_recursion_limit from being
set above 100.  If, for whatever reason, you really must have
a ridiculously high recursion limit, then it is a suggestion to
manually modify the stack limit in debug.h to a higher number.

We have reasonably set it to 10000 without too much issue, but keep
in mind, the overhead is higher for every stack you throw on the 
process table.  Higher stack means more memory used.

Also be aware that your shell stack limit directly is affected
to this value.  

Type::

   ulimit -a  

This will show you your shell stack limits.  Do NOT set the
STACKMAX value higher than your shell's stack value.

The value in ~/Rhost/Server/hdrs/debug.h is currently set as::

  #define STACKMAX 1000

Feel free to change this to a higher value if you wish.

The caveat.  This effects the debug stack daemon.  Meaning,
the only way for this to be updated is through @shutdown and
then a fresh ./Startmush.

A @reboot WILL NOT LOAD IN A NEW DEBUG MONITOR!!!!

You can issue @list stack to see the current stack ceiling ingame.

--------------------------------
How to reset the password for #1
--------------------------------

.. warning::

   You can only use one of these options at a time. Make sure to change back your nerhost.conf and then reboot after making the changes.

Method 1: Reset to Default Password
===================================

in your netrhost.conf file add::

  newpass_god 777

This will reset #1's password to the default 'Nyctasia'.

Method 2: Increase Permissions of Immortals
===========================================

in your netrhost.conf file add::

  newpass_god 1

This will allow IMMORTAL players to @newpassword #1 upon reboot.

------------------------------------------------
Troubleshooting difficulties compiling RhostMUSH
------------------------------------------------

Changes to conf for high-bit CPUs
=================================

RhostMUSH automatically detects 64-bit platforms, and should compile
cleanly on these.

In case you are trying to compile Rhost on some other crazy-wide CPUs
such as the PS2, PS3 or other 128 or 256 bit CPUs, you can easily do
so by changing a few lines of code in conf.c.

change::

  typedef unsigned int    pmath1;
  typedef int             pmath2;
  #define ALLIGN1 4

to::

  typedef unsigned long   pmath1;
  typedef long            pmath2;
  #define ALLIGN1 8

.. note::

  Replace 8 with the size of your CPU's long integer. (4 for 32-bit,
  8 for 64-bit, 16 for 128-bit, etc etc)

RhostMUSH has only been tested to work on the AMD64, but there is no
reason to believe the same will not hold true for IA64.

Changes to autconf for certain systems
======================================

You should not have to worry about this, but incase something really
weird occurs, you may need to look into these changes...


The autoconfig.h file needs to have modifications to it by hand.

There are three manual entries:

This one sets how it defines the int to character pointer.  It's safe
to keep it as 'unsigned int' for 32 bit platforms.  For non 32-bit, 
define it to  how an int is defined on that system::

        typedef unsigned int    pmath1;

This one sets how it defines the signed int to character pointer.  Same
restrictions apply as above for unsigned int::

        typedef int     pmath2;

This sets the allignment for the given platform.  4 represents a 32 bit
platform.  8 would represent a 64 bit platform, etc.  Change accordingly::

        #define ALLIGN1 4


.. warning::

   Make sure these three entries are defined in your autoconf.h file else
   the mush will not compile.

--------------------------
Dealing with DB Corruption
--------------------------

Ok.  Your database won't come up.

If you are reading this, then likely the scenerio is one of the following:

#.  The mush says it can't find your database files.
#.  The mush says it can't read or load your database files.
#.  The mush seems to load fine but I can't log in anyone and when I do
    all the names and attributes of things seem to be gone!
#.  Bringing up your mail database


First thing is first.  Don't have a panic attack.

If the mush says it can't find your database files
==================================================

Check the names of the database files in your 'data' directory
--------------------------------------------------------------

They should be named something like::

  netrhost.db
  netrhost.db.old
  netrhost.db.old.prev
  netrhost.gdbm.dir
  netrhost.gdbm.pag

And you may see a netrhost.db.flat

Check your netrhost.conf file
-----------------------------

If you never touched the \*database or muddb_name params, you should be good.

Verify your \*database params (and muddb_name) are still set to 'netrhost' as 
part of the name.  Ergo, the default values and you didn't change them.  
These should match up with the filenames in your data directory.

If these names do not match up, it can't find the database files to load.
So you shouldn't have to change these names, ever. :)

Check your mush.config file
---------------------------

If you never modified this file, you should be good.

The gamename should be 'netrhost' for this file.  This does NOT control
the name of your game.  This controls the name of all the files 
as associated to the mush.  So changing this means the netrhost.conf
file, all your database files, and so forth.  Please don't change this :)

If the mush says it can't read or load your database files
==========================================================

Double check everything for the previous issue. Make sure everything is named properly.

Verify you have enough disk space. (quota)
------------------------------------------

Some account have a limited quota to run in.  If you reached or exceed
your disk quota, you can have a corrupted database.  So always keep
your eye on the size.  quota -s to see a human readable format to see
how much quota you have left.  You want to make sure current in use is
below the 'grace' and soft/hard limits shown.  If not, you're out of
space.
  
You will need to remove some files before you repair and bring up your
mush again.  Try to keep your quota at least 200 megs free to allow
plenty of wonderful growth space for the mush.

Verify you have enough disk space.  (system)
--------------------------------------------

The second way you can run out of disk space is by the filesystem itself.
do a df -h . in your 'game' directory'.  That is df -h <period>.
This will return how much disk space is being used and how much remains.
If it shows 100% used, you're out of disk space and the db is corrupt.

At this point, you're pretty screwed.  You can see if anything exists
in your system to free up some space, but if the filesystem itself
is filled, reach out to the owner of the server and let them know.
It's a much bigger deal than just your mush if that's the case.

Until this issue is resolved, you can not repair and bring up your mush.
No disk to run the game.

If the mush seems to load fine but I can't log in anyone and when I do all the names and attributes of things seem to be gone!
==============================================================================================================================

Ok, at this point you likely had your mush up when the physical server
went down hard.  Weither through an emergency shutdown or a physical
power outage, your db likely was brought down hard during a write,
so it left it in a corrupt state.  These things happen.  This is
why we always strongly request you make daily flatfile dumps.

So, to recover your database.

The bad news
------------

If you have no flatfile backup or never bothered with backups?
I'm sorry, at this point you're SOA.  There's no easy way to
recover a corrupted binary database.  If you absolutely need
data out of it we may be able to help you to piece meal things
out of it, but otherwise it's a lost cause.  You'll have to start
over from scratch.  I'm sorry.

The good news
-------------

If you made backups, or if the server had a normal shutdown, you
likely have a flatfile backup.  You will see a netrhost.db.flat
in either the 'data' directory or 'prevflat' directory.  That
is your manual flatfile backup.

If the server had a normal shutdown, you will see a file called
netrhost.db.TERMFLAT.  This is a scram-emergency db flatfile.
It attempts to write this at the time of server shutdown to
hopefully keep a clean backup in the case of issues since
it identifies the server is coming down hard.  Make sure
if you plan to use the TERMFLAT as your recovery flatfile
that the very last line shows something like \** END OF DUMP \**.
That shows you had a successful backup.

Now, to restore your database?
------------------------------
 
Please refer to the file 'README.DBLOADING'.

Bringing up your mail database
==============================

Your mail db may or may not come up at this point.  

If after restoring main database your mail database works
---------------------------------------------------------

If your mail database came up and does not show
'Mail: mail is currently off' then you should be good to go.

Please issue on the MUSH::

  wmail/fix
  wmail/lfix

This will put your mail system in sync with your current database and
fix up any errors that may exist.

wmail/fix fixes the mail.

wmail/lfix loads in the fixes.

If after restoring main database your mail database does not work
-----------------------------------------------------------------

If your mail database is not up and shows 'Mail: mail is currently off' then your mail db is currupt.

------------------------------------
Dealing with a corrupt mail database
------------------------------------

It says when you try to access mail that mail is disabled and/or off.

Nothing you do can bring it on line.  Well, this is bad, but not horrible.

The mail db is totally separate from the main game database.  This means
that it in no way damaged or corrupted your main mush database.

The bad news?  Yes.  Your mail database is corrupt.  To bring it back,
is it hopes that you read ahead of time about how to backup your mush,
which would include the mail database.

Backing up your mail database
=============================

You should be making a flatifile dump of mail db daily by running on the MUSH::

  wmail/unload

To recover your mail, it assumes you have a mail flatfile in either the
~/Server/game/data directory or the ~/Server/game/prevflat directory.  The
latter directory is used in junction to the backup_flat.sh and will always
house the latest flatfile if not one recently dumped in your data directory.

Automatically recovering your mail database
===========================================

If you have a flatfile dump of your mail db, run this command on the MUSH::

  wmail/load

Yup, that's it.  It'll take care of everything else.  Isn't automation grand?

Doesn't even require a reboot :)

.. note::

     You may at this point wish to run the following:
     wmail/fix  -- this fixes the mail database and sync's it to the mush db.
     wmail/lfix -- this loads in the fixed mail database

If you have a very old mail database, this is likely going to be required
to sync against nuked players and other changes to the game since the flatfile.

If this is a new db that you have, you can skip the fixing.

Manually recovering your mail database
======================================

To recover your mail manually, you need to delete your mail databases, 
reboot, then reload your mail flatfiles.  If you have no mail flatfiles, 
well, you're going to have to start over with the mail database.  Sorry.

First, go into the 'game' subdirectory.  Inside that directory is a 'data'
directory.

You will be deleting all the files with the following names::

   RhostMUSH.mail.*                (like RhostMUSH.mail.dir/RhostMUSH.mail.pag)
   RhostMUSH.folder.*              (like RhostMUSH.folder.dir/RhostMUSH.folder.pag)

.. warning::

   DO NOT DELETE OTHER NAMED FILES!!!
  
Once these files are deleted, you may issue a @reboot to restart the mush.
This will unlock the mail system and load in a fresh db.

Now, if you have flatfiles of the old mail database, you will see in either
the 'data' directory or the 'prevflat' directory files that are called::

  RhostMUSH.dump.folder
  RhostMUSH.dump.mail

Make sure these two files are in the 'data' subdirectory.  Copy them in
if they exist in your 'prevflat' directory.

Once they are in the 'data' directory, within the mush type: wmail/load

This loads in the flatfile and recover the mail database.

Now, at this point the mail db may not be 100% in-sync with the game db.

So let's fix it.

wmail/fix   -- this will run a fix on the mail db and repair any issues.

wmail/lfix  -- this will load the fixed flatfile back into the mush.

At this point you should be good to go.
