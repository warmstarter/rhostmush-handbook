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

1.  Log into your existing mush.  Let's make current backups
    of all your flatfiles.  Issue:
    A. @dump/flat
    B. wmail/unload
    C. @areg/unload
    D. newsdb/unload

2.  Shutdown your game (@shutdown)

3.  Make an image of all your current backed up files.  From
    The Server/game directory you would type:
                ./backup_flat.sh -s

    Please remember the '-s' to the ./backup_flat.sh.

4.  Make note of the most recently created file in the directory
    Server/game/oldflat.  It's usually named something like:
                RhostMUSH.dbflat1.tar.gz

    You will need this file later.

5.  Rename your 'Rhost' directory to something else.  This
    is the directory that you have containing the 'Server'
    directory.  Name it anything you want other than 'Rhost'.
    For those not used to unix you would type:
                mv Rhost Rhost_old

6.  Pull in the latest Rhost.  You would type:
                git clone https://github.com/RhostMUSH/trunk Rhost

    You would type this in the same directory you have renamed
    your old 'Rhost' directory

7.  go into the Rhost/Server directory.   Type:
                make confsource

    Select what options you want (including the mysql and other goodies)
    then compile it (also within the menu, it's the 'r' option).

8   Once your game is compiled and ready to go you need to copy in
    the data from your old game.  Copy the RhostMUSH.dbflat1.tar.gz
    we mentioned in step #4 to the Server/game directory of your NEW
    GAME DIRECTORY.  From within the 'game' directory of your current
    game you should be able to issue (if you named the old one Rhost_old):
    Again this needs to be done FROM YOUR Server/game directory!!!
    A. cp netrhost.conf netrhost.conf.orig
    B. cp ../../Rhost_old/Server/game/RhostMUSH.dbflat1.tar.gz .
    C. tar -zxvf RhostMUSH.dbflat1.tar.gz 
    D. Compare your current netrhost.conf to the default one that came with
       the source (that you renamed to netrhost.conf.orig).  Likely the
       only sections you have to add to your current netrhost.conf (that
       came with your RhostMUSH.dbflat1.tar.gz archive), will be toward 
       the end, with the include rhost_ingame.conf and rhost_mysql.conf.
       Depending on how old your game is coming from you may need to add
       more options.  Any config option that is the same between the 
       netrhost.conf files do not have to be copied over, and you want to
       keep your custom settings (like don't port or other stuff you 
       have already customized).
    E. ./db_load data/netrhost.gdbm data/netrhost.db.flat data/netrhost.db.new
       This loads in your flatfile information.
    F. ./Startmush  
       Your ./Startmush should re-index all your txt files you originally made.
    G.  In your game type the following as an immortal or as #1.
       1.  wmail/load
           This will load in your mail flatfile.
       2.  @areg/load
           This will load in your autoregistration flatfile (if available)
       3.  newsdb/load
           This will load in your hardcoded bbs flatfile (if available)

9.  You should be good to go on a current directory structure for Rhost.  Enjoy!


Adding MySQL to RhostMUSH older than 3.9.5p2
============================================

MySQL is now native in RhostMUSH as of 3.9.5p2.

*******************************************************************************
** IMPORTANT ** IMPORTANT ** IMPORTANT ** IMPORTANT **IMPORTANT ** IMPORTANT **
*******************************************************************************
To autodetect it, YOU MUST HAVE mysql_config installed and running
on your server.  Without this, even if you have mysql db installed
it won't be able to recognize the parameters you will need for it
and will thus fail.  Please check your linux distribution to see
what packages are needed to install mysql_config.
*******************************************************************************
** IMPORTANT ** IMPORTANT ** IMPORTANT ** IMPORTANT **IMPORTANT ** IMPORTANT **
*******************************************************************************

Download the git repository to a seperate directory so that you can
copy over the files that it requires you to.

Suggestion:  git clone http://github.com/RhostMUSH/trunk ~/tmprho

If you are patching UP from an older version, you need to update
the following files:

1.  update your src/Makefile to the one in the 3.9.5p2+ repo
    ( cp ~/tmprho/Server/src/Makefile ~/Rhost/Server/src/Makefile )
2.  update your bin/asksource.* files to the one in the 3.9.5p2+ repo
    ( cp ~/tmprho/Server/bin/asksource.* ~/Rhost/Server/bin/ )
3.  append 'include rhost_mysql.conf' BEFORE the rhost_ingame.conf file
    and before the section that says 'define local aliases' toward the end of
    your netrhost.conf file.
    ( edit your ~/Rhost/Server/game/netrhost.conf file )
4.  copy the game/rhost_mysql.conf file from the 3.9.5p2+ repo 
    ( cp ~/tmprho/Server/game/rhost_mysql.conf ~/Rhost/Server/game/ )
5.  The following lines have to be REPLACED/CHANGED in local.c ( toward the top ):
    ( you may edit this or copy the one from the other distro )
    ( do either:  edit ~/Rhost/Server/src/local.c )
    (        or:  cp ~/tmprho/Server/src/local.c ~/Rhost/Server/src/local.c )
     
//----------- IF REPLACING/CHANGING local.c COPY BELOW --------------------------
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
//----------- IF REPLACING/CHANGING local.c COPY ABOVE --------------------------

6.  Issue 'make clean' then make confsource to rebuild using the latest
    builder script to build in the mysql changes.

