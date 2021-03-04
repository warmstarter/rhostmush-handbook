--------------------------------------------------------------------------------
What to type to Compile and Install RhostMUSH
--------------------------------------------------------------------------------

Note about Compiling
--------------------

To install, type:  make confsource

If your binaries do not work or you get an error type:  ./bin/script_setup.sh
Then type: make confsource

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

Note about Recompiling
----------------------

If you plan to use 'make confsource' to recompile your source, you should first
issue a 'make clean' before re-issuing a 'make confsource'.  'make confsource'
remembers the last options you used.

A failure to issue 'make clean' prior to re-compiling with 'make confsource' or
re-compiling with 'make source' can potentially leave stale object files which
may cause unforseen issues when running code, including but not limited to 
random crashes.  Generally whenever recompiling it's good to always make clean
first.

Note about Patching
-------------------

There's two ways you can look to patch the source.  If you plan to run the
RhostMUSH source from a git repository, then please use the git repo to
constantly update your code.  If you knew enough to want to set up a git repo
then we expect knowledge on how to keep source trees updated in the git repo
to be used the same as any other source distribution.

If, however, you have no idea what a git repo even is, or have no inclination
of using git to manage your RhostMUSH source, or just don't care one way
or another, then you can use the included patch.sh routine (from under the
Server directory) to patch your source at any time.

From the server directory just type: ./patch.sh

That will auto-compile your source, auto make all your header files and
essentially keep everything up to date to the latest source.
Once that's done, all you do from within the game is two commands:

1.  @reboot (or @reboot/silent)  -- This will load in the new binary
2.  @readcache  -- This will read in all the .txt file changes

Happy Rhosting.
