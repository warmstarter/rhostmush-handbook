===========================================================
What RhostMUSH is about and what's so great about RhostMUSH
===========================================================

RhostMUSH was founded in 1989, originally by Natasha Davis (Nyctasia) and as 
a branch from the original release of TinyMUD code.  It was her desire to make
a game that was flexible, with multiple levels of progression and highly 
customizeable.  She lost time and interest and passed the game to 
Steve Shivers (Seawolf), Mike McDermott (Thorin), and Jace Hoppel (Ashen-Shugar)

Through their work, the stability improved, we fixed it to be multi-platform
and as bug free as we could possibly make it.  We introduced several methods both 
in game and in source that allowed consistent memory bounds checking and 
various alerts for any mischievous naughtyness in-game or possibilities of any
hacks, patches, or alterations in the code causing leaks or issues.  

While not perfect, it has allowed us to have an absolutely outstanding 
turn around for any bugs sent our way, which anyone who uses RhostMUSH will
attest to.

Over the years, others have joined the RhostMUSH team, including Ambrosia
(who is the current dev lead), Lensman, Kage (who kindly provided the
UTF8/unicode port), Jeff/Loki, Rook, Noltar, and Odin.

We also have had hundreds of people who have offered (and provided) help,
patches, suggestions, bug fixes, and alternations all on their own and
every single one will have had their name mentioned in the RHOST.CHANGES
file in the readme directory.  It's far too large to have in the online
help files.

RhostMUSH today provides an amazing tool that allows nearly entire
customization in-game of every single feature available in Rhost without
having the requirement to modify the hardcode.  This includes but is
not limited to:

Recycle bin
===========

Yup, you guessed it.  RhostMUSH has a windows like recycle bin.
This means the objects you @nuke and @destroy become 'destroyed'
but not recycled until they are @purged.  If you use the Myrddin
CRON in the Mushcode directory, it by default sets up a job
to purge anything over 30 days old, which should be more than
sufficient for any needs.  The goodness of this?  You can recover
nuked things from any period of time, as long as they were not
@purged first.

Commands: @purge, @nuke, @destroy, @recover, @reclist

@snapshot
=========

Live image snapshots to unload or load to and from
disk.  As many snapshots as you want, as often as you want.  
It essentially does a flatfile dump of a dbref#.  Great for
backups or cross-Rhost portability.

Command: @snapshot

Wizard and Immortals by default
===============================

* are spoofable.  Meaning all their @pemits by default will not 
  trigger NOSPOOF.  If you do not wish this, set the SPOOF flag
  this applies to anyone below their level.
* override all locks.  There's two flags to disable this. 
  NO_OVERRIDE to stop overriding all locks (including attribs)
  and NO_USELOCK to just stop overriding uselocks.  
  This applies to anything their level and lower.
* optionally cloak from all non-immortals/God player.
  This can be highly abused if not careful and there
  is a @depower to disable cloaking and/or dark that will 
  disable this.
* immortals can optionally supercloak from even wizards.
  this can not be disabled, and you must consider that immortals
  should be treated as the God player (#1) since they are
  effectively #1 in nearly every way.

Titles and Captions to a player's name
======================================

@caption and @titlecaption

Have an alternate name with locks for NPC obfuscation
=====================================================

@altname
@lock/altname

Have multiple player aliases
============================

As well as a method to reserve player names per player w/o revealing who has what name.

@protect

Actively control how dark works both game-wide and individually
===============================================================

@depower dark

@admin allow_whodark, sweep_dark, command_dark, lcon_checks_dark,
secure_dark, see_owned_dark, idle_wiz_dark, player_dark

@toggle snuffdark

@flagdef to redefine who and what can set the DARK flag

Make config file changes in-game without having to reboot or have shell access
==============================================================================

@admin admin_object

Execute any binary or script as a localized function
====================================================

EXECSCRIPT (power), SIDEFX (flag)

Customized percent substitutions (like %n, %#, etc)
===================================================

@admin sub_include, @hook

Redefine percent substitutions (like %n, %#, etc)
=================================================

@admin sub_override, @hook

Localize command and function overrides in a sandbox
====================================================

@icmd, @lfunction, subeval(), sandbox()

Multiple Zones
==============

Have multiple zones which can optionally belong to multiple targets (multiple zones per target allowable!)

@zone, zones, lzone(), zonecmd()

Optionally control, enable, or disable sideeffects
==================================================

@admin sideeffects, SIDEFX (flag)

Have 31 cross-interactive realities for locations
=================================================

This works as a truly independant and self-contained environment.
A room can have 31 'layers', each 'layer' is a reality in 
the same physical space.  These layers can work independently
or allow interaction with other layers for vast customization.
This affects all methods within the game including all matching, 
looking, $commands, listens, movement, interaction, pretty 
much every single aspect of mushing.

REALITY LEVELS

Override any command with softcode
==================================

@admin access (check ignore)

Master room $commands to then override the hardcode

The abilility to raise or lower permissions on the various
==========================================================

staff bitlevels for each player.

@power, @depower, TOGGLES, FLAGS

Customize new commands on the connect screen
============================================

@admin file_object2

Softcode any txt file (like connect.txt)
========================================

and have it evaluate in-game.  It evaluates as the object it is on.

@admin file_object

Advanced tracing methods for debugging your code including labels!
==================================================================

Commands: @label

Functions: parenmatch(), trace()

Toggles: CPUTIME

Flags: TRACE

Attributes: TRACE_GREP, TRACE, TRACE_COLOR, TRACE_COLOR_<attr>

Substitutions: %_

Built in pretty-printing of attributes with the parenmatch() function
=====================================================================

Example Code Output:: 

  @emit [add(1,sub(2,div(3,4)),5)];@emit [extract(get(me/foo),3,1)

  Example Pretty Print: 
  @emit [
     add(
        1,sub(
           2,div(
              3,4
           )
        ),5
     )
  ];@emit [
     extract(
        get(
           me/foo
        ),3,1
     )
  ]


Plenty more not mentioned!
==========================

The flexibility to customize RhostMUSH is what is most daunting.
Don't fret, you don't need to do it to run RhostMUSH successfully.
In fact, the default configuration is mostly compatible with
MUSH and will work correctly out of the box for most needs.  For those
wishing to play, of course the sky is the limit of what you want to
do.  

Advanced features of RhostMUSH
==============================

Debugging/Tracing
-----------------

* Debugging in Rhost allows for advanced features like expressing where and
  when to do debugging via a trace() function, with toggled labels, and the
  ability to grep content from trace output.  There also exists features to
  color-match parenthesis, braces, and brackets in-game as well as pretty print
  the output of commands and functions.

  - help trace
  - help %_
  - help trace()
  - help parenmatch()
  - help parenstr()
  
Zoning
------

* Zoning in Rhost allows the same functionality of Penn and MUX, though the
  syntax is different.  It also allows the ability to belong to multiple
  zones at the same time and take advantage of mulitple zones at once.
  This allows for increased levels of complexity.

  - help zones
  - help @zone
  - help zonecmd()
  - help lzone()
  - help @Lock type twink
  - help @lock type zone
  
Reality Levels
--------------

* Reality levels allows for the ability to have a sandboxed 'existance'
  in each physical location across the entirity of the mush.  Each 
  reality is its own sandbox and can either stand alone or work 
  dependently with other realities.  A person can belong to multiple
  realities at the same time, and realities is geared to a method for
  send and receive.  Each 'method' requires to be in the given reality
  to affect it.

  - help reality levels
  - wizhelp chkreality
  - wizhelp reaity level
  - help @Lock type user
  
Function and Command Overriding
-------------------------------

* Functions and commands can both be overridden with softcode.  To 
  override a hardcoded command you first set the command ignore.
  There are various levels of ignoring so that you could have it
  ignored from mortals but have it executed fine for non-mortals.
  This allows you to use the actual physical command within a
  softcode override.  You may also use @Hook for altering how
  a command works.   Functions are overridden by setting the 
  function in question ignored, then writing a softcode alternative
  that is then executed and fetched appropriately.

  Commands:

     - wizhelp @admin
     - wizhelp access
     - wizhelp permissions
     - wizhelp @Hook
     - wizhelp hook setup

  Functions:

     - wizhelp @admin
     - wizhelp function_access
     - wizhelp @function
     - help @lfunction
     - wizhelp bypass()
  
The Recycle Bin
---------------

* Rhost has a recycle bin that works a bit like a windows recycle bin.  
  Whenever you destroy something within the mush, it is stacked onto
  the recycle bin and marked unavailable within the mush.  This marks
  the dbref# as garbage in any sense of the word.  However, the object
  is not able to be reused until purged.  Once purged, it is put onto
  a free list that can then be reassigned to a new object.

    - wizhelp @nuke
    - wizhelp @destroy
    - wizhelp @toad
    - wizhelp @turtle
    - wizhelp @purge
    - wizhelp @recover
    - wizhelp @reclist
  
  
Percent Substitution Adding/Overriding
--------------------------------------

* Rhost allows the ability to both override percent substitutions as 
  well as creating new ones.  This is done with @Hook and admin 
  params and issues softcode overriding.  Due to how it is evaluated
  there is no risk of recursion.

    - wizhelp @hook
    - wizhelp hook_cmd
    - wizhelp sub_include
    - wizhelp sub_override
  
Hooking
-------

* Hooking allows you to have advanced methods to manipulate commands
  including adding customized switches to them via softcode.  

    - wizhelp @hook
    - wizhelp hook_cmd
    - wizhelp hook_obj
    - wizhelp hook setup
  
Command based uselocks
----------------------

* This allows you to have unique uselocks per $command.  This is done
  through the use of the USELOCK attribute flag, then you set up
  a matching attribute name with a prefix of a ~ to specify how
  the lock is to be evaluated.  This works in the same manner
  as an evaluation lock.  To be able to use the USELOCK attribute flag
  you must be empowered to do so with the 'ATRUSE' @toggle.  You may
  also use the secure_atruselock config parameter to globally enable
  this and not require the toggle to be set.

  - wizhelp atruse toggle
  - help attribute uselocks 

Differentating between command and listen locks
-----------------------------------------------

* We distinguish between commands and listens with uselocks by passing
  an optional argument to all locks that are uselocks.  This optional
  argument is 0 for a default lock, 1 for a command lock and 2 for
  a listen lock.

  - help @lock type uselock

Wizard auto-overiding and how to disable it
-------------------------------------------

* By default wizards override all locks, including attribute locks, 
  can see all dark exits, and bypass pagelocks.  This can be 
  troublesome, and even abusive, so there's ways to disable this.

  - wizhelp @depower (for those abusing it)
  - wizhelp no_override (disable overiding locks)
  - wizhelp no_uselock (disable just uselock overriding)
  - wizhelp pagelock toggle (disable pagelock overriding)

Advanced FLAG and TOGGLE control
--------------------------------

* Flags and toggles can be controlled to have multiple permissions
  and enable/disable targets of how the flags are allowed to be
  set.  This is done through commands in-game or you can use
  conf file options to do so.

  - wizhelp @flagdef
  - wizhelp @toggledef
  - @admin @flagdef alternatives

    - wizhelp flag_access_set   
    - wizhelp flag_access_unset 
    - wizhelp flag_access_see   
    - wizhelp flag_access_type

  - @admin @toggledef alternatives

    - wizhelp toggle_access_set  
    - wizhelp toggle_access_unset
    - wizhelp toggle_access_see  
    - wizhelp toggle_access_type 

Advanced site control
---------------------

* We allow advanced site control by not only blocking various sites
  but we can specify how many times a player can be connected at the
  same time as well as how many times sites are able to connect at
  the same time.  This is done through normal site manipulation.
 
  - wizhelp forbid_host
  - wizhelp register_host
  - wizhelp noguest_host
  - wizhelp @list (site option)

Auto-Registration
-----------------

* Autoregistration is the method that a player can auto-register
  by providing their email on the connect screen.  It will email
  them a password and an optional document that the administrator
  provides.  This is well described in the wizhelp.

  - wizhelp autoregistration

Which bit level is best?
------------------------

* This is something that should be discussed by you and the staff
  of your game.  As a good rule of thumb, only provide the bitlevel
  that is required to do the job.  Too much power is always risky.
  In essence, each tier of bit can do everything the previous bitlevel
  can do, and then additional stuff on top of it.  The highest bitlevel
  is #1 itself, being bitlevel 7.  Then immortal, which should be
  considered the #1 character in most cases and is bitlevel 6.  Then
  the royalty character, which is equal to wizard on penn, mux, or
  other codebases.  For most things, this is the bitlevel you want
  to assign players.  The exception will likely be game owners or
  people who control the master room code.

  There's a bunch of readme files and online wizhelp that goes into
  detail of the various bitlevels and what each can do.  
 
  - wizhelp control

What are the limits for size/growth for RhostMUSH?
--------------------------------------------------

While using QDBM, there's really no set limits for most things.
The limits that we have are as followed:

* LBUF - 64K.  It is recommended to only use 32K as there is some issues with networking with 64K lbufs.

  - Compile time option with the menu configurator

* SBUF - 64 characters (if configured -- it's suggested you do).  

  - Compile time option with the menu configurator

* MBUF - 200 characters.  Not able to be changed.

* MAX CONNECTIONS - Limited by the total number of open sockets and descriptors on the account and server running on.  There are various tools to limit connection DoS attemps and other such nastiness.  This is well documented in the netrhost.conf file.

  - wizhelp max_players
  - ~/game/netrhost.conf

* MEMORY - no limit.  Generally runs between 8-50M depending on the size of the mush and the LBUF size specified.

* CPU  - no limit, but has built in cpu abort in code.  The netrhost.conf file documents this well for customizing.  the default values are usually good enough.

  - wizhelp max_cpu_cycles
  - wizhelp cpuintervalchk
  - wizhelp cputimechk
  - wizhelp cpu_secure_lvl
  - wizhelp heavy_cpu_max
  - ~/game/netrhost.conf

* DISK - no limit.  Generally will be 75-200M depending on size, number of backups and if you leave your compiled object files in.

* DB Size - (20000 default) There is no limit on the number of objects the db can have.  By default it's soft limited to 20K objects, which can be changed by a netrhost.conf file change.  We have had this up past 1.5 million objects, and other than a second or two of lag for complex searches we had no real problem.

  - wizhelp maximum_size
  - help @quota
  - wizhelp @quota
  - wizhelp @limit

* Attribute Size - 10K as a hard limit.  750 as a soft limit.  You can increase this but it can't exceed 10000 attributes.  This is to avoid DoS style attacks.

  - wizhelp vlimit
  - wizhelp @limit


Sqlite and MySQL/Maria setup and why use it?
--------------------------------------------

* Both of these can be configured separately or conjointly to
  run in parallel.  This can be done through the RhostMUSH
  configuration utility.  You generally want to use SQL for
  external data storage or accessing a central repository
  of data to share between multiple projects.  Like, for
  example between a wiki, a forum, and the mush.
    

Executing outside scripts and binaries within RhostMUSH
-------------------------------------------------------

* Rhost has execscript() which allows executing outside binaries
  or scripts as a native function.  All effort has been done to
  avoid any type of DoS based issue or hang by doing this, however
  the guidelines presented should be followed before doing so.

  - wizhelp execscript
  - wizhelp power execscript
  - help sidefx
  - wizhelp writing scripts

Pulling external data into RhostMUSH
------------------------------------

* You are capable of pulling external data in to RhostMUSH using several methods.  These are by using:

   - SQL (mysql or sqlite)
   - execscript
   - cron (wizhelp signal)

Integrating a unix cron right into RhostMUSH
--------------------------------------------

* The unix cron can be used to integrate with Rhost fairly 
  easilly by use of signals.  By using SIGUSR1 you can specify
  Rhost to execute code in-game, which part of that could be
  to pick up a pre-designed list of commands that the unix cron
  has set up.

  - wizhelp signal
  - wizhelp signal_cron

Signal handling, how it works, and when and why use it
------------------------------------------------------

* Signals are used to do different things for the mush.  By default,
  the following signals are recognized by the mush and will do
  the following as defaults.

  - SIGUSR1 - will do a reboot of the mush.  This is also customizable so that you can have it execute code in-mush if you want.
  - SIGUSR2 - will do a clean shutdown of the mush.
  - SIGTERM - will immediately scram the mush as cleanly and fast as possible.  It will avoid dumping anything to the database to speed up scramming, but write a TERM flat file to be loaded in if corruption.

Setting up global parents, global @parents, global attribute formatting, and other global setups
------------------------------------------------------------------------------------------------

* Global parents are useful when you want to have a global 'parent' 
  without actually having a defined '@parent'.  It always will be the
  highest tier in a lookup.  The way lookups will go will be::

    self->@parent(s)->@zone(s)->GlobalParent

 The type of the parent does not have to match the target.

 These global parents can be defined either by using a global
 generic parent or by using the type.  If a type is specified it
 overrides the generic.  The following parameters are used:

   - global_parent_obj     - The generic global parent (if defined)
   - global_parent_room    - The room global parent
   - global_parent_exit    - The exit global parent
   - global_parent_thing   - The thing global parent
   - global_parent_player  - The player global parent

* Global @parents are different than global parents in that any new
  item of similar type that is created is automatically assigned this
  physical @parent.  It's obviously more limiting since it sets
  the literal physical parent defined.  

  The type of the parent does not have to match the target.

  The following parameters are used:

   - room_parent           - The target that new rooms are @parented
   - exit_parent           - The target that new exits are @parented
   - thing_parent          - The target that new things are @parented
   - player_parent         - The target that new players are @parented

* Global attribute formatting is a method define a wrapper, of sorts,
  where attributes like @desc, @odesc, @succ, and anything similar
  can be processed through this.  All attributes will be either
  &FORMAT<attribute> or &<attribute>FORMAT based on the current 
  configuration.  Example: &FORMATDESC or &DESCFORMAT localy, or 
  use the following global objects for global formatting.  Local
  formatting has priority.

  The type of the parent does not have to match the target.

   - room_attr_default     - Target for room formatting
   - exit_attr_default     - Target for exit formatting
   - thing_attr_default    - Target for thing formatting
   - player_attr_default   - Target for player formatting


RhostMUSH limitations and how to get around them
------------------------------------------------

While Rhost is insanely configurable and quite powerful, there are
limitations that exist within it.

* Function invocations.  Sometimes you will hit a ceiling on evaluation.
  You may want to tweak values to allow more functions or commands
  to execute.  The following controls that:

  - function_invocation_limit [25000 default] - specifies the total functions you can execute per command.
  - function_recursion_limit [50] - specifies the total times a function can call itself over and over.  Rarely should this be increased and doing so can effect your stack depth.

* Command queue limits.  Sometimes you want more to be queued up for
  players or wizards.

  - player_queue_limit  - Max number of entries a player can queue
  - wizard_queue_limit  - Max number of entries a wizard can queue

* @limit is a wonderful way to lock down limitations per player or global.  Lots of power is available here.

  - @limit
  - vattr_limit_checkwiz - Enable @limit checks for wizards
  - wizmax_vattr_limit   - Set wizard global VATTR limits
  - wizmax_dest_limit    - Set wizard global @destroy limits
  - max_vattr_limit      - Set player global VATTR limits
  - max_dest_limit       - Set player global @destroy limits

* Lots of trace output can be cut off.  You can modify this with:

  - trace_output_limit   - Set lines of trace output shown

* To define how many commands a minute a player set SPAMMONITOR can use

  - spam_limit -- default 120

* If you examine things and see 'Output cut off' messages, you may want
  to increase your output limit, funny enough, the name of this is
  similar

   - output_limit - You should set this no less than 4 times the current size of your LBUF.

* Attributes names can not exceed 64 characters.  Sorry, it's a hard limit

* Sometime you may find a single \ may not work for an escape.  You can
  in most cases use a % instead or double escape the \ to make it work.
  Also look at lit() as a solution.

Advanced guest setup
--------------------

* After you set up your guests, you can set unique names to each guest
  if you so want after defining the dbref#'s your guests use.  This is
  done by defining them in the guest_namelist parameter.  You can also
  increase guests (or decrease them) between 0-31 guests.

  - wizhelp guest_namelist
  - wizhelp num_guests

Attribute permission masking and the joys of the power behind it
----------------------------------------------------------------

* Attribute contentlocks can be set up so you can lock the actual
  content that you can set (or even unset!) into an attribute.
  The beauty of this is that you can specify case sensitive 
  information, lock different ways contents in attributes are set
  based on who is setting it, or even on where it's being set.
  The sky's the limit.

   - global_attrdefault    - Target for defining content locks
  

The amazing @cluster and what it can do for you
-----------------------------------------------

* Clusters is the way to virtually assign multiple objects into 
  a single physical object.  It essentially chains together two
  or more objects to share attributes between them, so that any
  attribute set on any object in that cluster can be set or fetched
  as if it was a singular entity.  This allows some amazing ability
  to distribute attribute content or even have a farm of a massive
  amount of attributes without paying a hefty penalty on object bloat.

  - help cluster  -- Gives a fantastic overview of how clusters work.

What we plan for the future
---------------------------

* Things to look forward to the future with RhostMUSH.

    - Full Unicode/UTF8 in Rhost 4.0
    - A fully featured tag system in Rhost 4.0
    - Built in Python API handler in Rhost 4.0
    - Hopefully a built in Ruby and Perl API in Rhost 4.0/4.1
    - Cross-Mush execution between mushes in Rhost 4.1
    - More as we think about it :)
  
Additional features not covered otherwise
-----------------------------------------

* +/- 5.4 million years can be utilized with the built in time functions 
  which includes timefmt(), secs(), convtime(), convsecs(), and moon().  Party on!

* Changing permission levels in the middle of execution for evaluation.

   - see help on the streval and ueval function'

* Full features in-game customization of near every aspect of the game.

Random notes and things to know about RhostMUSH
===============================================

Here are some things to know about RhostMUSH and what you may or may not
want to do.  Things here are not covered in other documents:

Admin toggles to configure the WHO, various things you're used to, etc is in the
'netrhost.conf' file.  descriptions Notes in the autoconf.h file is in the 
README.AUTOCONF file.

Note on bits, their levels, and things they do
----------------------------------------------

* IMMORTAL - They can do anything.  Treat this as #1 and only give to
  people you trust.  Period.   You don't have to use this bit
  if you do not want to and just assume #1.

* ROYALTY - Unlike PENN/MUX, this is *not* a sub-wizard, this is a 
  FULL wizard.  Plus, they can do a bit more.

* COUNCILOR - Like royalty on PENN/MUX but they can modify.

* ARCHITECT - Can't do as much as councilor, but lot more than BUILDER.

* GUILDMASTER - Very limited.  Sees dbrief#'s, can ex things their
  level and lower and @quota players.
  
You need to @pcreate your guest characters and set them GUEST
-------------------------------------------------------------

It doesn't create them on the fly but we considered this better.
You have 31 total you can have.  It defaults to 10 in the
netrhost.conf file.  You can rename the guests anything you want,
but before you do so, you must add the dbref#'s to the param
guest_namelist

@powers are INHERITED
---------------------

Therefore, you need power_objects enabled (@admin)
to make this work properly for non-plauyers.
A power is taken before a bit level ONLY if higher than that bit.
Yes, powers are multi-level.  

@depowers are automatically checked first before anything else
--------------------------------------------------------------

This is also meaningless on objects.

Zones are unique
----------------

You can have things in multiple zones.

The db auto-repares itself when it can
--------------------------------------

It does this by purging anything
it can't identify.  Dataloss is better than unrecoverable data.
Yes, any such 'repairing' is logged so you know if something is up.

You can get your connect.txt to parse ansi
------------------------------------------

See ansi_txtfiles in wizhelp.

You can also override it with softcode if you so wanted.  

See file_object in wizhelp for more information on this.  

Re-compiled binaries do not require an @shutdown
------------------------------------------------

When re-compiling the binaries, all you have to remember is when done, issue

@reboot on the game and @readcache.

You do not need to @shutdown.

Softcode emulations of functions from other servers are included
----------------------------------------------------------------

Load the file softfunctions into the mush once it's set up.  This are 
@functions that will alias the functions that PENN, MUX, and TinyMUSH have
that is either named differently or we don't have for one reason or another.

===========================================================
What FLAGS, TOGGLES, POWERS, and DEPOWERS mean in RhostMUSH
===========================================================

What are Flags?
===============

Flags are pretty much exactly the same as any other mush.  It's a flag
that you set or unset on a target which then enables/disables or 
alters something that target can do.  There's help on all the flags 
in help and wizhelp.  

What are Toggles?
=================

Toggles were designed as a single point flag that immediately enables
or disables a set ability or condition, thus a 'toggle'.  It works 
exactly like a flag and was originally designed for two reasons.  To
distinguish from the multi-meaning of a 'flag', and because frankly
we ran out of flag space :)

What is an @power?
==================

A power is similar to a power on other mushes, but unlike them, our
powers are multi-tier.  This means that they can be customized to
empower something at a given bitlevel.  You may empower something
from guildmaster up to councilor level.  There are some powers 
with a power level of N/A meaning they are a toggle power granting
an absolute power level as specified in the help for that power.
This requires the INHERIT flag for non-players to inherit powers,
however, a specific object can be granted a power as well.

What is an @depower?
====================

This is the anti-thesis of @power.  Also, depowers do not require
inheritance.  They also have priority over flags, toggles, and
powers.  You can use depower to remove or lower abilities and
control from a target, even a full wizard (royalty) can be 
depowered.
