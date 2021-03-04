----------------------------------------
Converting database betwen GDBM and QDBM
----------------------------------------

Ok, if you plan to recompile your game that is using GDBM to QDBM, or visa versa
some bad news.

The databases are NOT COMPATIBLE to each other, at least in the binary form.

Downgrading QDBM to GDBM
------------------------

I would NEVER change from QDBM back to GDBM, but if you're set on it these steps:

You would use the same steps if you plan to move QDBM to GDBM.  I however would
not do this.  Moving from QDBM to GDBM is a huge step backwards.  Seriously,
don't do it unless you have absolutely no other recourse.

However, WARNING:
IF you plan (for whatever reason) to move from QDBM to GDBM, you should verify
the following:
1.  You have on a 64 bit system, no object that has more than 400 attributes on it.
2.  You have on a 32 bit system, no object that has more than 750 attributes on it.
3.  Any CONTENT of any attribute must be below 4000 characters in length.
4.  Once you have that done, you may follow the procedures below on converting (upgrade)
    from GDBM to QDBM.  This works the same as converting (downgrading)
    QDBM back down to GDBM

Upgradging GDBM to QDBM
-----------------------

Now, if you've kept reading and plan to convert your GDBM database to QDBM great news!
It's more stable, it's faster, and lets you have far more flexibility.

So, BEFORE YOU RECOMPILE YOUR CODE.  This is what you have to do.

While logged in to your mush, issue the following commands
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    A.  @dump/flat    -- This will make a flatfile dump of your MUSH database
    B.  wmail/unload  -- This will make a flatfile dump of your MAIL database
    C.  @areg/unload  -- If you use the AutoRegistration engine, this dumps it
    D.  newsdb/unload -- If you use the hardcoded news/bbs engine.  This dumps it

Verify the files exist
++++++++++++++++++++++

    A.  .. Server/game/data/netrhost.db.flat
    B.  .. Server/game/data/RhostMUSH.dump.folder
        .. Server/game/data/RhostMUSH.dump.mail
    C.  (Optional) .. Server/game/data/RhostMUSH.areg.dump
    D.  (Optional) .. Server/game/data/RhostMUSH.news.flat

Shutdown the MUSH
+++++++++++++++++

@shutdown your mush

From the Server directory
+++++++++++++++++++++++++

    A.  make clean
    B.  make confsource
        1.  Select QDBM and if you wish at this time increase your LBUF size
        2.  Select any other options you may want
    C.  (r)un and let it compile.
    D.  Main DB: Delete (rm) the following files (from Rhost/Server/game/data)
        netrhost.gdbm*
        netrhost.db
        netrhost.db.new
        netrhost.db.new.prev
    E.  Mail DB: Delete (rm) the following files (from Rhost/Server/game/data)
        RhostMUSH.folder.dir  
        RhostMUSH.folder.pag  
        RhostMUSH.mail.dir  
        RhostMUSH.mail.pag  
    F.  (Optional) AutoReg DB: Delete (rm) the following files (from Rhost/Server/game/data)
        RhostMUSH.areg.dir  
        RhostMUSH.areg.pag  
    G.  (Optional) News/BBS DB: Delete (rm) the following files (from Rhost/Server/game/data)
        RhostMUSH.news.dir
        RhostMUSH.news.pag

From the Server/game directory
++++++++++++++++++++++++++++++

    A.  ./db_load data/netrhost.gdbm data/netrhost.db.flat data/netrhost.db.new
    B.  ./Startmush

While logged into the mush issue the following commands
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

    A.  Load in the mail database
        wmail/load
    B.  (optional) Load in the autoreg database
        @areg/load
    C.  (optional) Load in the news/bbs database
        newsdb/load

Verify that you have QDBM running and your valid values
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

    A.  @list options system
    B.  @list options (spammy)
