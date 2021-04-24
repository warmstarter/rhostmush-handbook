.. _utilities-ssl:
.. index:: Utilities - SSL, SSL - Utilities

======================================================
Setting up an SSL tunnel for secure connection options
======================================================

-------------------------------------
Quickstart for SSL setup with stunnel
-------------------------------------

#.  Modify your netrhost.conf file and add/change the following parameters:

    #. sconnect_reip 1
    #. sconnect_cmd SECRET-MAGIC-COOKIE

        #.  SECRET-MAGIC-COOKIE is a case sensitive single word phrase. Any printable character other than the '#' character is allowable.  You may use up to 30 characters.
        #.  Make sure the secret is a hard to guess phrase.  This is used by stunnel to forward on the originating IP address.

    #. sconnect_host localhost 127.0.0.1 othersite.goes.here

        #.  This is optional.  
        #.  If you do not specify it it defaults to 'localhost 127.0.0.1'.  If your domain has a unique name like 'localhost.localdomain' like some ubuntu distributions, then you should customize your stunnel_host.

#.  go into the stunnel directory
#.  ./stunnel_setup.sh   

    #. Choose the defaults or alter them based on preferences
    #. Make sure to choose the warpbubble conf file

#.  ./stunnel_start.sh
#.  Use ./stunnel_stop.sh to stop the SSL tunnel at any time

You do not need to shutdown the ssl handler if you shutdown the mush.  They
are entirely separate processes.

-------------------------------
Detailed SSL setup with stunnel
-------------------------------

To setup SSL connectivity, we use the STUNNEL application to tunnel SSL to 
the mush.  This acts a bit like a man in the middle but remains controlled 
by the game owner which would have access to the end point anyway.

.. note::

   it is assumed you will have already initially set up your netrhost.conf.

stunnel directory
=================

You would set up the stunnel from the 'stunnel' directory.  There the following
files are of relevance::

  README                     -- a readme explaining the points of stunnel
  stunnel.conf.example       -- The example stunnel.conf file.  If you wish to create this manually you're welcome to.  Just make sure the end file is stunnel.conf
  stunnel_setup.sh           -- the script to build a stunnel.conf file for you which will be dropped at your specified location.
  stunnel_kill.sh            -- Stop/terminate the stunnel process.
  stunnel_start.sh           -- Start the stunnel process.
  warpbubble.pl              -- the perl script that handles stunnel to mush connectivity.
  stunnel_src                -- If you do not have stunnel, this directory will allow you to download, compile and locally install.


Modifying netrhost.conf
=======================

To be able to utilize SSL, you first must set your netrhost.conf file with
the relevant information to enable SSL connectiions.  These three config
options must be set to be able to use SSL, however, sconnect_host if
not set will default to 'localhost 127.0.0.1'.

::

  sconnect_reip 1         -- This enables the SSL tunnel layer handler within rhost.
  sconnect_cmd XYZZY      -- this will set the secret SSL command handshake command to XYZZY.  This is case sensitive and can be up to 31 characters.  Please make sure to only use printable non-whitespace characters.  Ergo: one word
  sconnect_host wildcards -- This allows wildcarded sites (one or more) to allow to access the sconnect/stunnel handler.  This defaults to 'localhost' and '127.0.0.1' so if you have 'localhost.localdomain' instead then you must set this to whatever is seen as 'localhost' to you.  You can verify this by checking your /etc/hosts file.

.. note::

   the sconnect_host is optional.  If you do not specify it, it will default to two values:  'localhost' and '127.0.0.1'.
 
Running the stunnel setup program
=================================

At this point you're ready to run the stunnel setup program.  So at this point type the following::
 
    ./stunnel_setup.sh
 
This will prompt you through settings.  Most you can select the defaults to.
The SSL port you may need to change based on your administrative requirements.
It will prompt you with whatever you set for your mush name.  If you have not
selected a mush name at this point, you can select the defaults.

You will want to use the config file for warpbubble as this hides the secret.
  
Be aware that if you have DNS host lookups disabled on your mush, you
MUST have 127.0.0.1 as an entry for your sconnect_host file.

Starting the stunnel proxy
==========================

When you have your stunnel.conf file to the way you want, you then
issue the following command to run your SSL layer::

    ./stunnel_start.sh

Shutting down the stunnel proxy
===============================

If ever you need to bring down the SSL layer, you may kill it with the command::
 
    ./stunnel_stop.sh

Configuring firewall on the host
================================

Please be aware that the port that the SSL layer is on must be opened
in any firewall rule you specified to allow the connectivity.  This also must
not be the port the mush is running on and requires a separate port.
