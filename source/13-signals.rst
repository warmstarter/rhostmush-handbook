--------------------------------------------------------------------------------
Signals and why you need them for control
--------------------------------------------------------------------------------

Rhost by default allows signals at the shell to handle various processes in-game.

The following signals are useful.

TERM (kill -TERM or kill -15)
-----------------------------

   - This will immediately terminate the mush, dumping a special flatfile called
     netrhost.db.TERM and scramming the db in question by force-closing it
     without any writes.  A TERM is the effort for the mush to shut down the
     mush as fast as possible to avoid any db corruption if possible since
     a TERM signal is common during a server shutdown, so time is paramount.

USR1 (kill -USR1)
-----------------

   - This by default issues a reboot on the server.  This is a special parameter
     because this can actually be changed in-game to do any number of other 
     things.  Please refer to the RhostMUSH running in question if this is
     the default behavior or if the method for USR1 is doing something else.

USR2 (kill -USR2)
-----------------

   - This will shutdown (cleanly) the mush.  This behaves as if you issued
     a @shutdown from within the game, and follows all proper procedure
     in bringing the game down cleanly and safely.  This shoudl be used
     when doing maintenance on the game or if you need to bring it down
     from the shell.

KILL (kill -KILL or kill -9)
----------------------------

   - This signal can not be caught and will immediately terminate the game
     without any safty to the database at all.  Short of something horribly
     wrong going on, this should never be used to bring down your mush.
     Doing so will almost certainly corrupt your databases (ALL OF THEM)
     that are open, including but not limited to your main database, your
     mail database, your autoregistration database, and so forth.  So if
     you do this, plan to do some database recovery from your flat files.
     Also, when you bring down a mush in this manner, you need to issue
     Startmush -f to bring it back up.
