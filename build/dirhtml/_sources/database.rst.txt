========
Database
========

Loading an existing Database
============================

To load in a previous database, you run the db_load script.

From the game directory you would type::

  ./db_load data/netrhost.gdbm yourflatfilehere data/netrhost.db.new

.. note::

   You may also do: ./Startmush 
   Then you just follow the prompts to load in your flatfile there.

If you wish to have #1's password reset to 'Nyctasia' please add this
to the bottom of your netrhost.conf file::

   newpass_god 777

The caveat is that you must not have any netrhost.db* or netrhost.gdbm* files
in your data directory prior to loading it in.  It'll error out if previous
files exist.  So you will need to move all files that start with netrhost.db*
and all files that start with netrhost.gdbm* to another directory.

Your flatfile tends to be named 'netrhost.db.flat' which is in your data 
directory.  You can, however, name your flatfile anything you want and have
it in any directory you want.

To make a flatfile in game, you just issue @dump/flat.  You can specify
a filename after it, otherwise it assumes the name 'netrhost.db.flat'.

Converting a flatfile database for use in RhostMUSH
===================================================

In the ~/Server/convert directory there is a script called 'doconvert.sh'

This script will convert most flatfiles from existing mush engines to 
RhostMUSH.  The exception is PennMUSH 1.8.0 and later.  For this there is a
BETA converter penn18x_converter.tgz.  This is proven to work, most of the time,
with codebases between 1.8.0 and 1.8.2.  It has not been fully vetted with
the latest PennMUSH databases.  Our apologies.

To convert a non-pennmush game (or a pennmush 1.7.4 or earlier), you first
need a valid flatfile of the game you're wanting to convert.  Please refer
to the documentatation of the mush engine in question (MUX, Penn 1.7, TM2/3)
on how to do this.  Once you have it type:::

  ./doconvert.sh FLATFILETOCONVERT FLATFILEOUTPUT

In this instance, FLATFILETOCONVERT will be the filename (with full path) to
the flatfile you are wishing to convert.

The FLATFILEOUTPUT is anyfilename you wish to name the RhostMUSH converted
flatfile.  I suggest netrhost_converted.db.flat so you know by the name
what it is.

Follow what it asks for and just let it do its thing.

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
