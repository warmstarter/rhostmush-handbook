--------------------------------------------------------------------------------
What RhostMUSH is about and what's so great about RhostMUSH.
--------------------------------------------------------------------------------

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
-----------

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
---------

  Live image snapshots to unload or load to and from
  disk.  As many snapshots as you want, as often as you want.  
  It essentially does a flatfile dump of a dbref#.  Great for
  backups or cross-Rhost portability.
  Command: @snapshot

Wizard and Immortals by default
-------------------------------

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
--------------------------------------

  @caption and @titlecaption

Have an alternate name with locks for NPC obfuscation
-----------------------------------------------------

  @altname
  @lock/altname

Have multiple player aliases
----------------------------

  As well as a method
  to reserve player names per player w/o revealing who has what
  name.
  @protect

Actively control how dark works both game-wide and individually
---------------------------------------------------------------

  @depower dark
  @admin allow_whodark, sweep_dark, command_dark, lcon_checks_dark,
         secure_dark, see_owned_dark, idle_wiz_dark, player_dark
  @toggle snuffdark
  @flagdef to redefine who and what can set the DARK flag

Make config file changes in-game without having to reboot or have shell access
------------------------------------------------------------------------------

  @admin admin_object

Execute any binary or script as a localized function
----------------------------------------------------

  EXECSCRIPT (power), SIDEFX (flag)

Customized percent substitutions (like %n, %#, etc)
--------------------------------------------------

  @admin sub_include, @hook

Redefine percent substitutions (like %n, %#, etc)
-------------------------------------------------

  @admin sub_override, @hook

Localize command and function overrides in a sandbox
----------------------------------------------------
  @icmd, @lfunction, subeval(), sandbox()

Multiple Zones
--------------

  Have multiple zones which can optionally belong to
  multiple targets (multiple zones per target allowable!)
  @zone, zones, lzone(), zonecmd()

Optionally control, enable, or disable sideeffects
--------------------------------------------------

  @admin sideeffects, SIDEFX (flag)

Have 31 cross-interactive realities for locations
-------------------------------------------------

  This works as a truly independant and self-contained environment.
  A room can have 31 'layers', each 'layer' is a reality in 
  the same physical space.  These layers can work independently
  or allow interaction with other layers for vast customization.
  This affects all methods within the game including all matching, 
  looking, $commands, listens, movement, interaction, pretty 
  much every single aspect of mushing.
  REALITY LEVELS

Override any command with softcode
----------------------------------

  @admin access (check ignore)
  Master room $commands to then override the hardcode

The abilility to raise or lower permissions on the various
----------------------------------------------------------

  staff bitlevels for each player.
  @power, @depower, TOGGLES, FLAGS

Customize new commands on the connect screen
--------------------------------------------

  @admin file_object2

Softcode any txt file (like connect.txt)
----------------------------------------

  and have it evaluate in-game.  It evaluates as the object
  it is on.
  @admin file_object

Advanced tracing methods for debugging your code including labels!
------------------------------------------------------------------

  Commands: @label
  Functions: parenmatch(), trace()
  Toggles: CPUTIME
  Flags: TRACE
  Attributes: TRACE_GREP, TRACE, TRACE_COLOR, TRACE_COLOR_<attr>
  Substitutions: %_

Built in pretty-printing of attributes with the parenmatch() function
---------------------------------------------------------------------

  Example Code Output : 
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
--------------------------

The flexibility to customize RhostMUSH is what is most daunting.
Don't fret, you don't need to do it to run RhostMUSH successfully.
In fact, the default configuration is mostly compatible with
MUSH and will work correctly out of the box for most needs.  For those
wishing to play, of course the sky is the limit of what you want to
do.  
