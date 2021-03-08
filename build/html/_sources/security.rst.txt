========
Security
========

Considerations to locking down restrictions in RhostMUSH
========================================================

Sometimes, you want to have things run at various privilage levels and do not
want to have things with too much access.  Weither that is online objects or
players you want to block from connecting to your mush.  Here's things you can
do.

One thing to keep in mind is that RhostMUSH, unlike PennMUSH is not flag
dependant on permission level, it's ownership based.  While setting a wizard
flag on an object would work, it's not recommended and it is instead recommended
to chown the object in question to a wizard (like your wizard holder character)
Then the object must be set inherit to actually inherit the wizard.

Note: inherit is required to inherit anything from the player.  Flags, powers,
      toggles.  The only thing that is inherited automatically is depowers.

Online: Blocking object abilities
---------------------------------

We have various flag levels.  It is strongly recommanded you check wizhelp
on 'control' for a detailed overview of what each bitlevel can or can not do
prior to giving the ownership to the object.  Things useful for tweaking control
on players and objects:

FLAGS (access with @set)
++++++++++++++++++++++++

 IMMORTAL, ROYALTY, COUNCILOR, ARCHITECT, GUILDMASTER,
 FUBAR, SLAVE, SIDEFX, NO_CONNECT, WANDERER, SAFE,
 AUDITORIUM, BACKSTAGE, NOBACKSTAGE, INDESTRUCTIBLE,
 INHERIT, JUMP_OK, NO_TEL, NO_WALL, NO_EXAMINE, 
 NO_MODIFY, NO_CONNECT, NO_POSSESS, NO_PESTER, 
 NO_OVERRIDE, NO_USELOCK, NO_MOVE, NO_YELL, CLOAK,
 SCLOAK, DARK, UNFINDABLE, SEE_OEMIT, TELOK, SUSPECT,
 SPAMMONITOR

TOGGLES (@toggle)
+++++++++++++++++

 BRANDY_MAIL, PENN_MAIL, MUXPAGE, VPAGE, NOISY,
 MONITOR* (all monitor toggles), MORTALREALITY,
 NODEFAULT, NO_FORMAT, PAGELOCK, SNUFFDARK, VARIABLE

@powers, @depowers, and @locks
++++++++++++++++++++++++++++++

Please review help (and wizhelp) for each of these items on how it can affect
a player, thing, exit, or room.  The help is quite verbose.

Offline: Blocking twinks from being abusive on your game
--------------------------------------------------------

FLAGS                   : FUBAR, SLAVE, NO_CONNECT
Commands:               : @boot, @nuke, @toad, @turtle
Sitelocks: (@admin)     : forbid_host, forbid_site, register_host, register_site, noguest_host, noguest_site
Sitelock by player      : @badsite, @goodsite, NO_CONNECT (flag)
Monitoring player       : SUSPECT (flag), @snoop
TOR/Proxy blocking:     : @blacklist (see shell's tor_pull.sh), @admin proxy_checker (see wizhelp), @tor (see wizhelp)

Extended lockdown of the mush and considerations
================================================

These are flags, powers, toggles, and various conditions for consideration
when you decide to use some of the advanced features of RhostMUSH.
These are not all that is availble, but tend to be the juicier ones to consider.

Attribute Restriction
---------------------

  @attribute -- Used for user-defined attributes
  @admin attr_access -- used for built in attributes (like desc)
  @aflags -- Used to set up lovely delicious attribute permission masks

Command Restriction
-------------------

  @icmd    - Very useful.   Please see wizhelp on it.  It disallows commands from executing including overriding them with softcode alternatives
  @admin access - Changes permissions, disables, or sets to be overridden a command.  Useful when you plan to override commands with softcode.

Flag/Toggle Restriction
-----------------------

  @flagdef - Again, see wizhelp on this.  There are also netrhost.conf options so you can have them loaded at start.  This allows tweaking flags and toggles to who can set/unset/see as well as what type can use it or wha type it can be used on.

Config restrictions
-------------------

  @admin config_access - Changes permission of who can set a config param

Function Restrictions
---------------------

  @function/@lfunction -- Allows softcoded functions that you can optionally lock down at your leasure
  @admin function_access -- You can use this even on softcoded functions if you so desired.

Flags
-----

  GUEST    - This is your guest flag, it should only be set on guests
  WANDERER - the WANDERER flag is default on new players.  This flag disables all building abilitites of the player.  
  NO_COMMAND - You can use this to stop a player from being able to connect without worrying about changing their password
  FUBAR      - As the flag states, it f*'s them up beind all recognition.  It essentially stops them from doing absolutely anything in the mush but pose and say.  Yes, it even disables the quit command.
  SLAVE      - Funny enough, slave allows anything but say and pose.  To ruin a troll's life, set both FUBAR and SLAVE and sit back and smile.
  NO_TEL     - The target can't teleport or be teleported
  NO_MOVE    - The target is locked at their location unable to move at all
  NO_WALL    - They do not see any @wall except a wizard @wall/no_prefix.  This has the bonus of snuffing db save messages.
  NO_POSSESS - Sometimes it's useful to grant a builder character to multiple players.  The NO_POSSESS flag makes it so that player can not be logged in more than 2 times.
  NO_MODIFY  - The target can not be modified (except by immortal/#1)
  NO_EXAMINE - The target can not be examined/decompiled (except by immortal/#1)
  STOP       - Once a matching $command is found on an object set STOP, it 'stops' trying to find other $command matches.
  NOSTOP     - If a target that is set STOP is also set NOSTOP, it will check the master room for a command and execute that as well if found.
  NO_PESTER  - Stops target from @pemit or whisper.  You may use @icmd as well.
  NO_OVERRIDE - Useful for immortals.  By default they override all locks, including attribute locks.  This makes it so an immortal's passing of locks will behave like a mortals NO_USELOCK  - This is like NO_OVERRIDE but only effects uselocks.  You likely want to set this on your immortal and wizard.
  NO_ANSINAME - stops a target from having an ansified name
  NO_CODE     - lock down advanced coding from a target
  SPAMMONITOR - stop a target from issuing more than 60 commands a minute.
  FREE        - Stop costing money for day to day processing of commands/building

Toggles
-------

  MONITOR            - Enables site monitoring.  This is the main toggle
  MONITOR_SITE       - Adds site information to site monitoring 
  MONITOR_USERID     - Adds the userid to site monitoring
  MONITOR_STATS      - Adds connection stats to site monitoring
  MONITOR_FAIL       - Adds showing failed connections to site monitoring
  MONITOR_CONN       - Adds connection monitoring to site monitoring
  MONITOR_DISREASON  - Adds disconnect reasons to site monitoring
  MONITOR_TIME       - Adds time stamps to site monitoring
  MONITOR_BAD        - Shows all bad creation attempts to site monitoring
  MONITOR_VLIMIT     - Shows attempts to bypass MAX ATTRIBUTES
  MONITOR_AREG       - Shows all auto registration attempts 
  MONITOR_CPU        - Shows all CPU warnings and/or alerts on the mush
  NO_FORMAT          - Bypasses @conformat, @exitformat, and other formats
  SEE_SUSPECT        - Allows you to see suspect info in the WHO/DOING 
  FORCEHALTED        - Allows you to @force/@sudo a HALTED target
  NOSHPROG           - Disallows using '|' to execute commands outside @program
  PROG               - Allows the target to use @program
  IMMPROG            - Disables the ability to use @quitprogram from a @program
  PROG_ON_CONNECT    - Allows a @program to resume if someone reconnects
  IGNOREZONE         - Enables a zone to process @icmd's
  PAGELOCK           - Enforces target to require passing pagelocks
  MAIL_LOCKDOWN      - Blocks the ability of a wizard to check another player's mail
  ATRUSE             - Enables the attribute to use attribute content locking
  NOGLOBPARENT       - Disables the target from inheriting global parenting 
  LOGROOM            - Enables system logs on the room
  EXFULLWIZATTR      - Allows target to examine all wizard attributes
  NODEFAULT          - Disables attribute formatting/handling on the target
  CHKREALITY         - Enables the use of reality locks on the target
  HIDEIDLE           - Disables deidling when you execute any command
  MORTALREALITY      - Enforces a wizard to pass realities as a mortal
  SNUFFDARK          - Hides dark exits from a wizard

@powers
-------

  WIZ_WHO            - Allows target to see sites ala wizard who
  NOFORCE            - target an not be forced (except by immortal/#1)
  FREE_QUOTA         - Allow target to have unlimited quota
  JOIN_PLAYER        - Allow to 'join' a player's location
  NO_BOOT            - Player can not be booted except by immortal/#1
  STEAL              - Player can give negative money
  TEL_ANYWHERE       - Player can teleport anywhere
  STAT_ANY           - Player can @search, @stat, or @find things
  HALT_QUEUE_ALL     - Player can halt the queue
  SEARCH_ANY         - Player can search for anything
  WHO_UNFIND         - Player can see hidden player on WHO
  SHUTDOWN           - Player can @shutdown the mush
  PURGE              - Player can use /purge to @destroy and @nuke
  EXAMINE_FULL       - Player can examine anything (not set NO_EXAMINE or cloaked)
  FORMATTING         - @*formats allow passing what a person sees as %0, %1, etc  
  CHOWN_ANYWHERE     - Chown anything anywhere to yourself
  CHOWN_OTHER        - Chown something you don't own to yourself
  EXAMINE_ALL        - Examine other things (tiered)
  SEE_QUEUE_ALL      - Player can see the full queue
  GRAB_PLAYER        - Player can grab a remote player and pull them to location
  LONG_FINGERS       - Player is granted remote control of things they own
  BOOT               - Player can @boot
  SEE_QUEUE          - Player can see advanced queue features
  TEL_ANYTHING       - Player can @teleport anything
  PCREATE            - Player can @pcreate players
  NOWHO              - Allows the use of @hide
  HALT_QUEUE         - Allows halting queue by specified bitlevel
  SECURITY           - Allows setting  NOMOVE    NO_TEL   SLAVE   NO_YELL
  WRAITH             - Allows bypassing exit locks
  HIDEBIT            - Hides your admin level from lower levels
  FULLTEL            - Allows full immortal level teleportation
  EXECSCRIPT         - Allows executing external scripts in ~/game/scripts

@depowers
---------

  WALL               - Disables the ability to @wall  
  LONG_FINGERS       - Disables remote access to things
  STEAL              - Can not steal money 
  CREATE             - Can not create anything
  WIZ_WHO            - Can not access wizard who  
  CLOAK              - Can not wizard cloak
  BOOT               - Can not boot
  PAGE               - Can not page
  FORCE              - Can not @force/@sudo
  LOCKS              - Can not pass locks
  COMMAND            - Can not execute any $command (including master room)
  MASTER             - Can not use any master room $command
  EXAMINE            - Lowers or disables the ability to examine/decompile
  NUKE               - Can not nuke, toad, or turtle
  FREE               - No longer has free money for anything
  OVERRIDE           - No longer can override anything
  TEL_ANYWHERE       - No longer can teleport anywhere
  TEL_ANYTHING       - No longer can teleport anything other than themselves
  POWER              - Can no longer use @power
  MODIFY             - Can not modify things  
  CHOWN_ME           - Can not chown anything to themselves
  CHOWN_OTHER        - Can not chown anything to others
  ABUSE              - Can not use $commands on anything they do not own
  UNL_QUOTA          - No longer has infinite quota
  SEARCH_ANY         - Disables the ability to @search/@find things
  GIVE               - Disables ability to give things/money
  RECEIVE            - Disables the ability to recieve things/money
  NOGOLD             - Limits (or disables) how much gold someone can give
  NOSTEAL            - Can not give negative gold 
  PASSWORD           - Can not change password
  MORTAL_EXAMINE     - drops examine and all fetching to mortal only
  PERSONAL_COMMAND   - Disables all $commands on anything they own

Site Restrictions
-----------------

  These are accessable via the @admin command, and the following options are
  allowable.
  
  You may see all site information at any time with: @list sites

IP based restrictions
+++++++++++++++++++++

  You may use CIDR notation such as /32 instead of 255.255.255.255.
  Config file:  (see section on forbid_site as it describes and gives examples)
  Online Syntax: MASK::

                       @admin forbid_site=123.123.123.0 255.255.255.0
                       @admin forbid_site=123.123.123.123 255.255.255.255
  
       CIDR::

                       @admin forbid_site=123.123.123.0 /24
                       @admin forbid_site=123.123.123.123 /32 

       REMOVING: MASK::

                       @site/all 123.123.123.123=255.255.255.255
                       @site/forbid 123.123.123.0=254.255.255.0

                 CIDR::

                       @site/all 123.123.123.123=/32
                       @site/forbid 123.123.123.0=/24

    forbid_site      - Set the specified site forbid only
    register_site    - Set the specified site register only
    noguest_site     - Set the specified site unable to connect to guests
    suspect_site     - Set the specified site suspect on connect
    noautoreg_site   - Set the specified site to not allow autoregistration
    trust_site       - Allow site to bypass suspect site restrictions
    permit_site      - Allow site to bypass sitelock restrictions
    nodns_site       - Site will no longer do reverse DNS lookups
    noauth_site      - Site will no longer do AUTH ident lookups

DNS based restrictions
++++++++++++++++++++++

  These allow globbing wildcard matches.
  The advanced feature is you can specify filtering on
  when the condition is matched, such as allowing 2 players from a site to
  be connected before disallowing anyone else to connect.
  Config File: (see section on forbid_host as it describes and gives examples)
  Online Syntax::
 
            ADD:      @admin forbid_host=*.dsl*.comcast.net *.aol.com *another.site
            DEL:      @admin forbid_host=!*.aol.com
            ADVANCED: @admin forbid_host=mudconnect.com|3 (allow 3 at once only)

    forbid_host     - Set the specified site(s) forbid only
    register_host   - Set the specified site(s) register only
    noguest_host    - Set the specified site(s) unable to connect to guests
    suspect_host    - Set the specified site(s) suspect on connect
    noautoreg_host  - Set the specified site(s) to not allow autoregistration
    validate_host   - Do not allow any autoregistration from emails matching site
    goodmail_host   - Always allow autoregistration from emails matching site
    nobroadcast_host - Snuff online site broadcasts via MONITOR for specified site

Methods to block anonymous connections and the pros and cons of doing so
========================================================================

  Now let's assume you have some troll attempting to use proxies to connect.
  There's multiple ways to stop this.

Blacklisting through external tor_pull.sh script
------------------------------------------------

       In ~/Rhost/Server/game you will see a script called tor_pull.sh
       Execute this by running (from the game directory) ./tor_pull.sh
       This populates the blacklist with registered proxies from various sites 
       on the internet.  If you want specified ip's added, feel free to add
       them at the end of this file.

Blacklisting through internal @blacklist command
------------------------------------------------

       On the mush, have as part of your startup @blacklist/load
       This will load in the generated blacklist file for automatic forbid 
       sites based on the ip.

Blacklisting through internal @tor command
------------------------------------------

       @tor.  Please see 'wizhelp tor' on how to set this up.  It in effect
       will actively block all known exit nodes for TOR's annonymous proxy
       service.  It self-updates and will actively block TOR connections.

Blacklisting through internal @admin command
--------------------------------------------

       @admin proxy_checker (please see wizhelp)
       This little doodad uses MTU checking against packet size which will
       detect most methods of proxies.  Sadly, this also has false positives
       because some situations require a differentating MTU value such as
       briged network connect with things like cloud services, docker, or
       similar encapsulated network services.  However, this option has
       several settings from just monitoring/alerting of possible proxies
       to downright forbidding them.  If you're being actively attacked,
       it may be worth considering adding this to add additional protection.    

Setting up an SSL tunnel for secure connection options
======================================================

Quickstart for SSL setup with stunnel
-------------------------------------

#.  Modify your netrhost.conf file and add/change the following parameters:

    #. stunnel_reip 1
    #. stunnel_cmd SECRET-MAGIC-COOKIE

        #.  SECRET-MAGIC-COOKIE is a case sensitive single word phrase. Any printable character other than the '#' character is allowable.  You may use up to 30 characters.
        #.  Make sure the secret is a hard to guess phrase.  This is used by stunnel to forward on the originating IP address.

    #. stunnel_host localhost 127.0.0.1 othersite.goes.here

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

Detailed SSL setup with stunnel
-------------------------------

To setup SSL connectivity, we use the STUNNEL application to tunnel SSL to 
the mush.  This acts a bit like a man in the middle but remains controlled 
by the game owner which would have access to the end point anyway.

Note: it is assumed you will have already initially set up your netrhost.conf.

stunnel directory
+++++++++++++++++

You would set up the stunnel from the 'stunnel' directory.  There the following
files are of relevance:

README                     -- a readme explaining the points of stunnel
stunnel.conf.example       -- The example stunnel.conf file.  If you wish to create this manually you're welcome to.  Just make sure the end file is stunnel.conf
stunnel_setup.sh           -- the script to build a stunnel.conf file for you which will be dropped at your specified location.
stunnel_kill.sh            -- Stop/terminate the stunnel process.
stunnel_start.sh           -- Start the stunnel process.
warpbubble.pl              -- the perl script that handles stunnel to mush connectivity.
stunnel_src                -- If you do not have stunnel, this directory will allow you to download, compile and locally install.


Modifying netrhost.conf
+++++++++++++++++++++++

To be able to utilize SSL, you first must set your netrhost.conf file with
the relevant information to enable SSL connectiions.  These three config
options must be set to be able to use SSL, however, sconnect_host if
not set will default to 'localhost 127.0.0.1'.

sconnect_reip 1         -- This enables the SSL tunnel layer handler within rhost.
sconnect_cmd XYZZY      -- this will set the secret SSL command handshake command to XYZZY.  This is case sensitive and can be up to 31 characters.  Please make sure to only use printable non-whitespace characters.  Ergo: one word
sconnect_host wildcards -- This allows wildcarded sites (one or more) to allow to access the sconnect/stunnel handler.  This defaults to 'localhost' and '127.0.0.1' so if you have 'localhost.localdomain' instead then you must set this to whatever is seen as 'localhost' to you.  You can verify this by checking your /etc/hosts file.

Note: the sconnect_host is optional.  If you do not specify it, it will default to two values:  'localhost' and '127.0.0.1'.
 
Running the stunnel setup program
+++++++++++++++++++++++++++++++++

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
++++++++++++++++++++++++++

When you have your stunnel.conf file to the way you want, you then
issue the following command to run your SSL layer::

                ./stunnel_start.sh

Shutting down the stunnel proxy
+++++++++++++++++++++++++++++++

If ever you need to bring down the SSL layer, you may kill it with the command::
 
                ./stunnel_stop.sh

Configuring firewall on the host
++++++++++++++++++++++++++++++++

Please be aware that the port that the SSL layer is on must be opened
in any firewall rule you specified to allow the connectivity.  This also must
not be the port the mush is running on and requires a separate port.
