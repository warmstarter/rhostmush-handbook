=================
Advanced Features
=================

.. _ansible-install:

Installing using an ansible playbook
====================================

To begin, you will run the following command in a directory that will house your game::

   git clone https://github.com/RhostMUSH/trunk Rhost

You may also just run the yml file and ansible (ansible-playbook) to install your RhostMUSH engine::

   wget https://raw.githubusercontent.com/RhostMUSH/trunk/master/rhostinstall.yml
   ansible-playbook rhostinstall.yml

This downloads the latest stable version of the code, bringing with it all patches and scripts, documentation and support tools that you will need.

Adding hardcoded modules
========================

RhostMUSH does support module writing.

Modifying sourcode to add a module
----------------------------------

This requires hooking your changes into local.c, then modifying the Makefile (in the src directory)
for any new source files that you wish to add.

Something to be aware of is that all localized data is ran after the system cache subroutine.

Adding an @startup to make use of modules
-----------------------------------------

This means that if your code is depending on @startups, you need to put a delay in the @startup
so that your local code can be loaded in as modules prior to the @startup execution.

Something that will not work::

  @startup me=@superhappyfuncommand loadmeup=now

A small alteration that will likely make this work fine::

  @startup me=@wait 1=@superhappyfuncommand loadmeup=now

That 1 second delay for the queue will give the game engine time to load in your module code.

Contributing your module back to Rhost
--------------------------------------

If you wish your modules to be part of the main Rhost distribution you have two options:

#.  Attempt to hack the bin/asksource.sh and bin/asksource.blank files.
#.  Ask one of the Rhost devs to do it for you :)

Reality Levels Setup
====================

Reality levels are a means to forbid (or allow) interaction between objects
in the same location.

Reality Levels Visibility
-------------------------

Each object (player, room, exit, thing) has two lists of reality levels. 
An Rx list, which describe what it can see and a Tx list, which describe 
where it can be seen. Those are bitfields. In order for X to see Y a bitwise
'and' is performed between X's RxLevel and Y's TxLevel. If the result is not
0, then X sees Y. If the result is 0, as far as X is concerned, Y doesn't 
exist. This affects contents lists, exit lists, look, say, pose, @emit, 
@verb, connect/disconnect, has arrived/has left messages, exit and object 
matching. 'here' and 'me' match always.

It doesn't affect @remit, @pemit, page, WHO or channels.
By default, all new objects are created with an RxLevel of 1 and TxLevel of 
1. Rooms are an exception, created with an RxLevel of 1 and a TxLevel of 
0xFFFFFFFF. Those default levels can be changed with configuration
parameters.

An object is always visible to itself, even if its Rx and Tx levels don't 
match. (See examples below)

Reality Levels Descriptions
---------------------------

For every reality level defined, you can define an attribute that serves as 
description. If you look at something and match more than one of its 
TxLevels, you'll see all the corresponding descriptions on the target 
object. If the object doesn't have any descriptions for the matching levels,
you'll see the regular @desc.

The @adesc attribute on the target is only triggered if the target can see 
the looker in turn. It's only triggered once, no matter how many descs the 
looker sees. The @odesc is shown only to those people that see /both/ the 
looker and the target.

Through extension, @afail/@ofail and similar pairs (@adrop/@odrop, 
@asucc/@osucc etc) work in the same way. @verb commands are similary 
affected.

Softcoded commands are only matched on the objects that can see the player.
The player doesn't have to see the object. This includes commands in the
Master Room.

Exits are treated specially. In order to be able to use an exit name (or to
use the 'move <exit>' command) the exit must be visible to the enactor. In
order to pass through the exit, the exit must see the enactor in turn. There
are reasons for this, which will become evident in the examples below.

Reality Levels Configuration parameters
---------------------------------------

A few configuration parameters have been introduced to deal with the reality
levels::

	reality_level <name> <value> [<desc attribute name>]

This directive can only be used in the config file (not with the @admin
command) and should be repeated for each reality level you want to define.
It defines a new level named <name> with a bitvalue of <value> and an 
optional desc attribute. There is a limit of 8 characters on <name>, a 
32-bit value on <value> (basically an unsigned long) and 32 characters on
the attribute name. A maximum of 32 reality levels can be defined::

	def_exit_tx <value>
	def_exit_rx <value>
	def_room_tx <value>
	def_room_rx <value>
	def_player_rx <value>
	def_player_tx <value>
	def_thing_rx <value>
	def_thing_tx <value>

These 8 directives define the default reality levels of newly created 
objects. They can be set in the config file or with the @admin command. 
Like above, <value> must be a decimal number::

	wiz_always_real <0|1>

If this parameter is set to 1 then wizards (and immortals on Rhost) will see
everything and will be visible to everyone. Their effective Rx and Tx levels
will always be 0xFFFFFFFF. Also settable in the config file and with the
@admin command.

Compile with -DREALITY_LEVELS compile time option to enable 'Real' needs to be '1'
This is an example file only to be added to the mush.conf file Format::

  reality_level <8 char name> <hex-byte-mask> <optional-desc: DESC default>

Reality Levels Example mush.conf
--------------------------------

::

  reality_level Real 1
  reality_level Obf1 2
  reality_level Obf2 4
  reality_level Obf3 8 OBFDESC
  reality_level Obf4 16 OBFDESC
  reality_level Obf5 32 OBFDESC
  reality_level Obf6 64 OBFDESC
  reality_level Obf7 128 OBFDESC
  reality_level Obf8 256 OBFDESC
  reality_level Obf9 512 OBFDESC
  reality_level Obf10 1024 OBFDESC
  reality_level Umbra 2048 UMBRADESC
  reality_level Fae 4096 FAEDESC
  reality_level Shadow 8192 SHADOWDESC
  reality_level Spy 16384
  reality_level Death 32768 DEATHDESC
  reality_level All 4294967295

Reality Levels Commands
-----------------------

Two wiz-only commands are used to set the reality levels of an object::

	@rxlevel <object>=<list>
	@txlevel <object>=<list>

<list> is a space-separated list of level names that have to be set on the
object. If a level name is prefixed with an exclamation mark (!) that level
will be cleared from the object.


.. warning::

   Changing the Tx levels of an object might make it invisible to you.
   In this case, you can still manipulate it by using his #dbref (or \*player 
   for players).

Functions
---------

There are five functions that deal with reality levels::

	hasrxlevel(<object>,<level>)
	hastxlevel(<object>,<level>)
        
These two functions check if an object has the specified Rx or Tx level.
You must control <object>. They return 0 or 1 and #-1 in case the object
does not exist or you don't have permissions::

	rxlevel(<object>)
	txlevel(<object>)
        
These two functions return a space-separated list of the object's Rx or Tx
levels. Again, you must control the object::

	cansee(<obj1>,<obj2>)

A wiz-only function, returns 1 of <obj1> can see <obj2> from a reality
levels point of view. It doesn't check if the objects are in the same 
location, the DARK/CLOAKED flags and so on. Just <obj1>'s Rx level against
<obj2>'s Tx level.

.. warning::

    If you are using it on MUX2.0 with /both/ reality levels and Wod
    Realms enabled, the function will perform both checks and the Wod Realms
    version checks against the DARK flag.

Example 1: A simplified Witchcraft setup
----------------------------------------

In Witchcraft, besides the various Gifted classes, characters can be spirits
There are spirit realms to which the mundane can not travel. Therefore we
will use 2 reality levels: Real and Ghost. Since some spirits can become
solid for a limited period of time, we will also use an additional desc for
the Ghost level, called GHOSTDESC. Therefore in the config file we will
have::

	reality_level Real 1
	reality_level Ghost 2 GHOSTDESC

Ghosts can pass through most mundane locks, so the exists should allows the
ghosts to pass::

	def_exit_rx 3

Note that def_exit_tx isn't set. Why? Because ghosts see the mundane world 
anyway, so a spirit character will have::

	@txlevel <player>=!Real Ghost
	@rxlevel <player>=Real Ghost

Let's assume 3 players::

  John is a Mundane. He won't see spirits.
  John's Rx: Real
  John's Tx: Real
  John's @desc: This is John.
  John's &GHOSTDESC: (Not important, since it's never visible)
  Johh's @adesc: %N has looked at you.
  John's @odesc: has looked at John.

Jack is a Gifted. He will sense spirits, but is still made from flesh and blood so visible to mundanes::

  Jack's Rx: Real Ghost
  Jack's Tx: Real
  Jack's @desc: This is Jack.
  Jack's &GHOSTDESC: (Not important, since it's never visible)
  Jack's @adesc: %N has looked at you.
  Jack's @odesc: has looked at Jack.

Frank is a ghost. He will see other spirits as well as mundanes, but won't be visible to mundanes. He can also become visible to everybody::

 Frank's Rx: Real Ghost
  Frank's Tx: Ghost
  Frank's @desc: This is Frank, looking human.
  Frank's &GHOSTDESC: This is Frank's ghostly shape.
  Frank's @adesc: %N has looked at you.
  Frank's @odesc: has looked at Frank.
  
Following are commands that each of the players enter and what they see.  I'll assume the +materialize command is defined like::

  &CMD_MATERIALIZE <cmdobject>=$+materialize:@txlevel %#=Real; @pemit %#=You are now material.


::

 |         John           |         Jack          |         Frank
                          |                       |
  > l                     |                       |
  A room                  |                       |
  This is a bare room.    |                       |
  Contents:               |                       |
  Jack                    |                       |
  Obvious exits:          |                       |
  Out <O>                 |                       |
                          |> l                    |
                          |A room                 |
                          |This is a bare room.   |
                          |Contents:              |
                          |John Frank             |
                          |Obvious exits:         |
                          |Out <O>                |
                          |                       |> l
                          |                       |A room
                          |                       |This is a bare room.
                          |                       |Contents:
                          |                       |John Jack
                          |                       |Obvious exits:
                          |                       |Out <O>
  >l Jack                 |                       |
  Jack                    |John has looked at you.|John has looked at Jack.
  This is Jack.           |                       |
  >l Frank                |                       |
  I don't see that here.  |                       |
                          |>l Frank               |
                          |Frank                  |Jack has looked at you.
                          |This is Frank's ghostly|
                          |shape.                 |
                          |                       |>l John
                          |Frank has looked at    |John
                          |John.                  |This is John.
                          |                       |>+materialize
                          |                       |You are now material.
  >l Frank                |                       |
  Frank                   |John has looked at     |Frank has looked at you.
  This is Frank, looking  |Frank.                 |
  human.                  |                       |
                          |>l Frank               |
  Jack has looked at      |Frank                  |John has looked at you.
  Frank.                  |This is Frank, looking |
                          |human.                 |
                          |This is Frank's ghostly|
                          |shape.                 |


Example 2: A WoD setup
----------------------

The reality levels will be defined like this::

  reality_level		Real 1
  reality_level		Obf1 2
  reality_level		Obf2 4
  reality_level		Obf3 8 OBFDESC
  reality_level		Obf4 16 OBFDESC
  reality_level		Obf5 32 OBFDESC
  reality_level		Umbra 64 UMBRADESC
  reality_level		Fae 128 FAEDESC
  reality_level		Shadow 256 SHADOWDESC
  reality_level		All 511

5 levels of Obfuscation, Umbra, Dreaming, Wraiths. 'All' is a handy
replacement for all levels, useful for wizards and wizobjects that should 
be visible on all levels. Also useful when you want to set an object's 
levels to something without knowing what he had before::

      @rxlevel #276=!All Real

!All will clear all levels, then the object will gain the Real level.
There is more than one Obfuscation level because of the relation between
Auspex and Obfuscation.

A vampire with Obfuscate 2, should not be visible by one with Auspex 1.
However one with Auspex 3 should see another vampire with Obfuscate 1, 2
/or/ 3.

Obfuscated players can move if they have Obf > 1. Umbral and Shadow players
should also be able to see most of the exits. So the exits at creation
should have default levels of Real + Obf2 + Obf3 + Obf4 + Obf5 + Umbra + 
Shadow = 1 + 4 + 8 + 16 + 32 + 64 + 256 = 381::

	def_exit_rx 381
	def_exit_tx 381

Obf1 is not included since an Obfuscated vampire should not be able to move
if it only has Obf1. Therefore they won't see the exits. If you want them 
to be able to see the exits, but not to use them, change the default Tx of 
the exits::

	def_exit_rx 381
	def_exit_tx 383

Joe the Mortal will have an RxLevel: Real and a TxLevel: Real
Jack the Malk, who likes to walk around Obfuscated and has Obfuscate 2 will
have an RxLevel: Real (he sees what the mortals see) but a TxLevel: Obf2
Jimmy the Nossie, who is using the Mask and has Obfuscate 4, but doesn't 
try to make himself invisible will have an RxLevel: Real (as Jack) 
and a TxLevel: Real Obf4. He will also set his @desc to what the mortals see and 
&OBFDESC to his real slimy desc. Simply put, he will be visible to mortals,
but not with his real desc.

Aldrin the Gangrel, has Auspex 4 and activates it. Therefore, his TxLevel 
will still be Real, but RxLevel: Real Obf1 Obf2 Obf3 Obf4 (all of them). So
he can see Joe, Jack and Jimmy's both descs.
Joe, on the other hand, won't see Jack at all. He will still see Jimmy, but
only Jimmy's @desc, not the OBFDESC

Frida the Fae... will have RxLevel: Real Fae and TxLevel: Real Fae. @desc
set to the mundane desc, &FAEDESC set to the Chimerical desc.
Emily the Enchanted will have an RxLevel: Real Fae, but the TxLevel: Real.
No &FAEDESC on her, although she'll be able to see it the one on Frida.
Gil the Garou, while travelling through the Umbra, will have RxLevel: Umbra
and TxLevel: Umbra. &UMBRADESC is his friend. He won't see mortals or other
characters who are not in the Umbra.

Barbie the Bastet, who's only peeking in the Umbra, without going there, 
will have RxLevel: Umbra, TxLevel: Real. Dangerous position since she
can't see the things that see her.

Deanna the Drake, who activates her spirit vision, will have 
RxLevel: Real Umbra and TxLevel: Real. She will see characters in Umbra and
real world at the same time and perceive the desc appropiate to the realm 
the ohter character is in.

Wanda the Wraith: RxLevel: Real Shadow, TxLevel: Shadow. Her @desc
would be empty, but the &SHADOWDESC should be set.
Marie the Mortal+ Medium: RxLevel: Real Shadow, TxLevel: Real

Global code objects that all characters should be able to use::

  RxLevel: All, TxLevel: All

Example 3: Softcode
-------------------

Considering the config directives from example 2 and assuming a function
getstat(<dbref>,<stat>) that will return the value of a player's stat from
the sheet here are softcode examples that implement some of the WoD powers.
In a real game you would have to use some more checks, of course.

:: 

  @create Reality Levels Commands (RLS)
  &CMD_OBFON rls=$+obf/on:@switch [setr(0, getstat(%#,Obfuscate))]=0, @pemit %#=You don't have Obfuscate!, {@txlevel %#=!All Obf%q0; @pemit %#=You are now invisible.}
  &CMD_OBFOFF rls=$+obf/off:@txlevel %#=Real; @pemit %#=You are now visible.
  @@ Note: +obf/on clears all TxLevels before setting the appropiate Obf
  @@ This is necesary, because a character might advance from Obf2 to
  @@ Obf3 and he should be visible /only/ on the Obf3 level.
  @@ +obf/off simply sets the Real Tx level, without clearing the Obf. The
  @@ reason is the Mask. Players with Obf3 or higher who use the Mask should
  @@ +obf/on, then +obf/off after approval and everything is set.
  &CMD_AUSPEXON rls=$+auspex/on:@switch [setr(0, getstat(%#, Auspex))]=0, @pemit %#=You don't have Auspex!, {@rxlevel %#=[iter(lnum(1, %q0), Obf##)]; @pemit %#=Auspex enabled.}
  &CMD_AUSPEXOFF rls=$+auspex/off:@switch [hasrxlevel(%#, Obf1)]=0, @pemit %#= You don't have Auspex enabled!, {@rxlevel %#=[iter(lnum(1, 5), !Obf##)]; @pemit %#=Auspex disabled.}
  &CMD_UMBRAENTER rls=$+umbra/enter:@rxlevel %#=!Real Umbra; @txlevel %#= !Real Umbra; @pemit %#=You are now in the Umbra.
  &CMD_UMBRALEAVE rls=$+umbra/leave:@rxlevel %#=Real !Umbra; @txlevel %#= Real !Umbra; @pemit %#=You left the Umbra.
  &CMD_PEEKON rls=$+peek/on:@switch hastxlevel(%#,Umbra)=1, {@rxlevel %#=Real !Umbra; @pemit %#=You are now peeking in the real world}, {@rxlevel %#=!Real Umbra; @pemit %#=You are now peeking into the Umbra}
  &CMD_PEEKOFF rls=$+peek/off:@rxlevel %#=!Real !Umbra [setinter(Real Umbra, txlevel(%#))]; @pemit %#=You are no longer peeking.

Execscript and external programs and scripts
============================================

Execscript variables
--------------------

Execscript Built in variables
+++++++++++++++++++++++++++++

========================== ===================================================
Variable                   Description
========================== ===================================================
MUSH_PLAYER                player dbref# 
MUSH_CAUSE                 cause dbref#
MUSH_CALLER                caller dbref#
MUSH_OWNER                 owner of player dbref#
MUSH_FLAGS                 space delimited list of flags on player
MUSH_TOGGLES               space delimited list of toggles on player
MUSH_OFLAGS                space delimited list of flags of player owner
MUSH_OTOGGLES              space delimited list of toggles of player owner
MUSHL_VARS                 space delimited list of MUSH attributes from player
                           This is passed from the mush's EXECSCRIPT_VARS attr
========================== ===================================================

Execscript Dynamic variables
++++++++++++++++++++++++++++

========================== =============================================
Variable                   Description
========================== =============================================
MUSHV_<arg>                <arg> variable passed from MUSHL_VARS
                           These are the attributes from EXECSCRIPT_VARS
========================== =============================================

Execscript Register variables
+++++++++++++++++++++++++++++

========================== ============================================================
Variable                   Description
========================== ============================================================
MUSHQ_<arg>                setq registers 0-9 and a-z
MUSHQN_<arg>               labels that are assigned the setq vars
MUSHN_<arg>                The labels that were defined by any register
                           Note: they must be ASCII-7 clean and contain no white spaces
========================== ============================================================


Execsript set object
--------------------

The script executed with execscript() will read in a file with the same name
as the script ending in '.set'.  This is a loader object that will set attributes
and registers back into the mush that you wish to pass from the script. The
fields are SPACE SEPARATED.  The values are NOT evaluated.

Execscript set object field format
++++++++++++++++++++++++++++++++++

Execscript set object Dynamic variables
"""""""""""""""""""""""""""""""""""""""

::

  VARNAME        OWNER        CONTENTS (or leave null to clear)

Execscript set object Dynamic variables Examples
''''''''''''''''''''''''''''''''''''''''''''''''
::

  SEX #123 Male
  DESC #123 %r%tThis is a willow tree of unique description%r%rIt sways in the wind.
  RED #123 This is the color %ch%crred%cn.
  WIPETHISATTR #123
  MULTILINE #123 This is a line
  that continues on
  because of the line feed (a control-M) on each line
  on the lines above

Execscript set object Register variables
""""""""""""""""""""""""""""""""""""""""

::

  REGISTER       Q            CONTENTS (or leave null to clear)

Execscript set object Register variables Examples
'''''''''''''''''''''''''''''''''''''''''''''''''

.. note::

   The last exammple clears register 0


::

  W Q This is stored in register W
  1 Q This is stored in register 1
  0 Q
  foo QN this sets register with label 'foo'


Execscript Example bash script
------------------------------

.. code-block:: bash

  #!/bin/bash
  echo "This was called by player ${MUSH_PLAYER} that is owned by ${MUSH_OWNER}"
  echo "Displaying Registers:"
  regs="0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
  for list in ${regs}
  do
      eval echo "Register ${list}: \${MUSHQ_${list}}"
  done
  echo "Displaying variables:"
  for vars in ${MUSHL_VARS}
  do
      eval echo "Variable ${vars}: \${MUSHV_${vars}}"
  done


Exescript Notes and warnings
----------------------------

While MUSHL_VARS are sanitized on what is allowable as a mush variable, this
is not necessarilly sanitized on what the calling script can fetch as a valid
variable.  Of note, you can not set environment variables that contain an
equals sign.  Be aware of this limitation.

Remember, MUSHL_VARS is the environment variable seen by the script.
This is EXECSCRIPT_VARS on the mush itself, that is the attribute set
on the target that contains the execscript() that is being executed.

Scripts to be used with execscript
----------------------------------

::

  account/                       -- Directory for execscripts relating to account creation
  compile39.sh                   -- Script for patching and compiling RhostMUSH 3.9
  compile.sh                     -- Script for patching and compiling RhostMUSH
  config.sh                      -- Script for setting compile time options for RhostMUSH
  debug.sh                       -- Script for debugging RhostMUSH
  dict.sh                        -- Script for querying a dictionary
  diff.sh                        -- Script for querying differences between two arguments
  fortune.sh                     -- Script for querying fortune program
  fullweather.sh                 -- Script for querying a graphical weather forecast (alternative)
  git.sh                         -- Script for querying git version of RhostMUSH
  hello.sh                       -- Script for teaching execscript for 'Hello World'
  iostat.sh                      -- Script for querying server stats of RhostMUSH
  jsonvalidate.sh                -- Python Script for validating JSON
  logsearch.sh                   -- Script for searching throgh logfiles for RhostMUSH
  math_example.sh                -- Examples of math operations to be used with math.sh
  math.sh                        -- Script for mathematical operations
  memory.sh                      -- Script for querying memory usage of RhostMUSH
  mkindx.sh                      -- Script for indexing RhostMSH helpfiles
  pastebinread.sh                -- Script for reading data from a pastebin URL
  pastebinwrite.sh               -- Script for writing data to a pastebin
  qspell.sh                      -- Script for checking spelling (alternative)
  quota.sh                       -- Script for checking disk quote and usage
  random.sh                      -- Script for getting a random number
  roomlog.sh                     -- Script for viewing logs in roomlog directory
  spell.sh                       -- Script for checking spelling
  stats.sh                       -- Script for querying server and process stats for RhostMUSH
  thes.sh                        -- Script for adding a word to the dictionary for spell scripts
  tinyurl.sh                     -- Script for shortening a URL
  weather.sh                     -- Script for querying a graphical weather forecast
  web.sh                         -- Script for querying an arbitary website

Using printf() for advanced text output
=======================================

The function printf() in Rhost can be used to greatly reduce coding in efforts for outputs,
screens and data display.  It can automatically center, justify and wrap the text parameters given to it.

Printf Example one
------------------

::

  @emit printf(|$-12s|$12s|$^12s$&14s$_12s|,a b c, d e f, g h i, wrap(lnum(20),12, l, |, |), j k l)

  |a b c       |       d e f|   g h i    |0 1 2 3 4 5 |j     k    l|
                                         |6 7 8 9 10  |
                                         |11 12 13 14 |
                                         |15 16 17 18 |
                                         |19          |


Printf Example two
------------------

::

 
   @emit printf($14&s $^4&s $-3&s $15&s,
   iter(Bruised|Hurt|Injured|Wounded|Mauled|Crippled|Incapacitated,##,|,%R),
   iter(|-1|-1|-2|-2|-5|,##,|,%r),iter(lnum(1,7),%[[if(gte(get(%#/damage),##),X,%b)]%],,%r),
   * Aggravated%RX Lethal%R/ Bashing)

            Bruised      [ ]    * Aggravated
               Hurt  -1  [ ]        X Lethal
            Injured  -1  [ ]       / Bashing
            Wounded  -2  [ ]                
             Mauled  -2  [ ]                
           Crippled  -5  [ ]                
      Incapacitated      [ ]  
  
Printf Example three
--------------------

::

    @emit [printf($-10|"'s$-60|"s,a b c d e f g h i j k l m n o p q r s t u v w x y z,
    this is a test a groovy test blah blah blah [repeat(blah%b,100)])]END!

    a b c d e this is a test a groovy test blah blah blah blah blah blah  
    f g h i j blah blah blah blah blah blah blah blah blah blah blah blah 
    k l m n o blah blah blah blah blah blah blah blah blah blah blah blah 
    p q r s t blah blah blah blah blah blah blah blah blah blah blah blah 
    u v w x y blah blah blah blah blah blah blah blah blah blah blah blah 
    z         blah blah blah blah blah blah blah blah blah blah blah blah 
    blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
    blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
    blah blah blah blah blah blah blah                                    END!

======================
Format for image files
======================

The image format goes like this:

========== ========== ==============================================================================================
Data Type  Example    Description
========== ========== ==============================================================================================
INT        3          TYPE: room 0, thing 1, exit 2, player 3, zone 4, garbage 5                                                                           
STRING     Wizard     NAME: of the target.  Verbatum, no quotes surround it
\*INT       123        LOCATION: dbref# of the target.  No prepending '#' used.
\*INT       234        CONTENTS: The first content in a linked list content table (-1 if none)                                                              
\*INT       345        EXITS: The first exit in a linked list exit table (-1 if none)                                                                       
\*INT       0          LINK: This is the 'home' of the object or what it's linked to (-1 for none)                                                          
\*INT       123        NEXT: The next thing after this item for a content holder                                                                            
STRING     #123       LOCK: The boolean string lock if it exists.  (empty if no lock)                                                                      
\*INT       1          OWNER: The dbref# owner of the target.  For players same dbref as player.                                                            
INT        789        PARENT: The parent of the target.  (-1 if none)
\*INT       99999      MONEY: The int value of the money the players has.
INT        194592     FLAGS1: The first word of flags (@set flags) on a player      (see FLAGS)
INT        194222     FLAGS2: The second word of flags (@set flags) on a player     (see FLAGS)
INT        199999     FLAGS3: The third word of flags (@set flags []) on a player   (see FLAGS)
INT        1582958    FLAGS4: The forth word of flags (@set flags []) on a player   (see FLAGS)
INT        159955     TOGGLES1: The first word of toggles (@toggle) on a player    (see TOGGLES)
INT        159958     TOGGLES2: The second word of toggles (@toggle) on a player   (see TOGGLES)
INT        159958     POWER1: The first word of powers (@power) on a player         (see POWERS)
INT        159958     POWER2: The second word of powers (@power) on a player        (see POWERS)
INT        159958     POWER3: The third word of powers (@power) on a player         (see POWERS)
INT        159958     DEPOWER1: The first word of depowers (@depower) on a player  (see DEPOWERS)
INT        159958     DEPOWER2: The second word of depowers (@depower) on a player (see DEPOWERS)
INT        159958     DEPOWER3: The third word of depowers (@depower) on a player  (see DEPOWERS)
INT        -1         ZONE(S): The list of zones starting here and ending with '-1'. (see ZONES)
>STRING    >VA        ATTRIBUTENAME: Attribute name to store, starts with > identifier
STRING     Wheee      ATTRIBUTECONTENTS: Contents of attribute.  Multi-lines seperate with ^M (control-M)
>STRING    >Desc      ATTRIBUTENAME: Another attribute to chain in
STRING     Ugly       ATTRIBUTECONTENTS: Contents of the next attribute
>STRING    \*Password  PASSWORDATTRIB: Special password attribute.  Attribute name is '\*Password'
STRING     $6$xy$xy   PASSWORDCONTENTS: The SHA512 password (if glibc 2.7+ supported on system) (see PASS)
<          <          This is the marker to specify the end of the attribute contents.  This is always the last line
========== ========== ==============================================================================================


.. note::

    Any Data type starting with '*' is ignored when @snapshot/loading.

The structure above with the examples would look like this in the file::

  3
  Wizard
  123
  234
  345
  0
  123
  #123
  1
  789
  99999
  194592
  194222
  199999
  1582958
  159955
  159958
  159958
  159958
  159958
  159958
  159958
  159958
  -1
  >VA
  Wheee
  >Desc
  Ugly
  >*Password
  $6$xy$xy
  <

HELP key indexes for the values
===============================


FLAGS: The following flags are to be used.  They are BITWISE masks that you 
need to add together for the values that you apply

.. code-block:: c

    /* First word of flags */
    #define SEETHRU         0x00000008      /* Can see through to the other side */
    #define WIZARD          0x00000010      /* gets automatic control */
    #define LINK_OK         0x00000020      /* anybody can link to this room */
    #define DARK            0x00000040      /* Don't show contents or presence */
    #define JUMP_OK         0x00000080      /* Others may @tel here */
    #define STICKY          0x00000100      /* Object goes home when dropped */
    #define DESTROY_OK      0x00000200      /* Others may @destroy */
    #define HAVEN           0x00000400      /* No killing here, or no pages */
    #define QUIET           0x00000800      /* Prevent 'feelgood' messages */
    #define HALT            0x00001000      /* object cannot perform actions */
    #define TRACE           0x00002000      /* Generate evaluation trace output */
    #define GOING           0x00004000      /* object is available for recycling */
    #define MONITOR         0x00008000      /* Process ^x:action listens on obj? */
    #define MYOPIC          0x00010000      /* See things as nonowner/nonwizard */
    #define PUPPET          0x00020000      /* Relays ALL messages to owner */
    #define CHOWN_OK        0x00040000      /* Object may be @chowned freely */
    #define ENTER_OK        0x00080000      /* Object may be ENTERed */
    #define VISUAL          0x00100000      /* Everyone can see properties */
    #define IMMORTAL        0x00200000      /* Object can't be killed */
    #define HAS_STARTUP     0x00400000      /* Load some attrs at startup */
    #define OPAQUE          0x00800000      /* Can't see inside */
    #define VERBOSE         0x01000000      /* Tells owner everything it does. */
    #define INHERIT         0x02000000      /* Gets owner's privs. (i.e. Wiz) */
    #define NOSPOOF         0x04000000      /* Report originator of all actions. */
    #define ROBOT           0x08000000      /* Player is a ROBOT */
    #define SAFE            0x10000000      /* Need /override to @destroy */
    #define CONTROL_OK      0x20000000      /* ControlLk specifies who ctrls me */
    #define HEARTHRU        0x40000000      /* Can hear out of this obj or exit */
    #define TERSE           0x80000000      /* Only show room name on look */

    /* Second word of flags */
    #define KEY             0x00000001      /* No puppets */
    #define ABODE           0x00000002      /* May @set home here */
    #define FLOATING        0x00000004      /* Inhibit Floating room.. msgs */
    #define UNFINDABLE      0x00000008      /* Cant loc() from afar */
    #define PARENT_OK       0x00000010      /* Others may @parent to me */
    #define LIGHT           0x00000020      /* Visible in dark places */
    #define HAS_LISTEN      0x00000040      /* Internal: LISTEN attr set */
    #define HAS_FWDLIST     0x00000080      /* Internal: FORWARDLIST attr set */
    #define ADMIN           0x00000100      /* Player has admin privs */
    #define GUILDOBJ        0x00000200      
    #define GUILDMASTER     0x00000400      /* Player has gm privs */
    #define NO_WALLS        0x00000800      /* So to stop normal walls */
    #define REQUIRE_TREES   0x00001000      /* Trees are required on this target for attrib sets */
    /* ----FREE----         0x00002000 */   /* #define OLD_NOROBOT  0x00002000 */
    #define SCLOAK          0x00004000
    #define CLOAK           0x00008000
    #define FUBAR           0x00010000
    #define INDESTRUCTABLE  0x00020000      /* object can't be nuked */
    #define NO_YELL         0x00040000      /* player can't @wall */
    #define NO_TEL          0x00080000      /* player can't @tel or be @tel'd */
    #define FREE            0x00100000      /* object/player has unlim money */
    #define GUEST_FLAG      0x00200000
    #define RECOVER         0x00400000
    #define BYEROOM         0x00800000
    #define WANDERER        0x01000000
    #define ANSI            0x02000000
    #define ANSICOLOR       0x04000000
    #define NOFLASH         0x08000000
    #define SUSPECT         0x10000000      /* Report some activities to wizards */
    #define BUILDER         0x20000000      /* Player has architect privs */
    #define CONNECTED       0x40000000      /* Player is connected */
    #define SLAVE           0x80000000      /* Disallow most commands */

    /* Third word of flags - Thorin 3/95 */
    #define NOCONNECT       0x00000001
    #define DPSHIFT         0x00000002
    #define NOPOSSESS       0x00000004
    #define COMBAT          0x00000008
    #define IC              0x00000010
    #define ZONEMASTER      0x00000020
    #define ALTQUOTA        0x00000040
    #define NOEXAMINE       0x00000080
    #define NOMODIFY        0x00000100
    #define CMDCHECK        0x00000200
    #define DOORRED         0x00000400
    #define PRIVATE         0x00000800      /* For exits only */
    #define NOMOVE          0x00001000
    #define STOP            0x00002000
    #define NOSTOP          0x00004000
    #define NOCOMMAND       0x00008000
    #define AUDIT           0x00010000
    #define SEE_OEMIT       0x00020000
    #define NO_GOBJ         0x00040000
    #define NO_PESTER       0x00080000
    #define LRFLAG          0x00100000
    #define TELOK           0x00200000
    #define NO_OVERRIDE     0x00400000
    #define NO_USELOCK      0x00800000
    #define DR_PURGE        0x01000000      /* For rooms only...internal */
    #define NO_ANSINAME     0x02000000      /* Remove the ability to set @ansiname */
    #define SPOOF           0x04000000
    #define SIDEFX          0x08000000      /* Allow enactor to use side-effects */
    #define ZONECONTENTS    0x10000000      /* Search contents of zonemaster for $commands */
    #define NOWHO           0x20000000      /* Player in WHO doesn't show up - use with @hide */
    #define ANONYMOUS       0x40000000      /* Player set shows up as 'Someone' when talking */
    #define BACKSTAGE       0x80000000      /* Immortal toggle for items on control */

    /* Forth word of flags - Thorin 3/95 */
    #define NOBACKSTAGE     0x00000001      /* Immortal toggle to control no-backstage */
    #define LOGIN           0x00000002      /* Enable player to login past @disable logins */
    #define INPROGRAM       0x00000004      /* Player is inside a program */
    #define COMMANDS        0x00000008      /* Optional define for $commands */
    #define MARKER0         0x00000010      /* TM 3.0 marker flags */
    #define MARKER1         0x00000020
    #define MARKER2         0x00000040
    #define MARKER3         0x00000080
    #define MARKER4         0x00000100
    #define MARKER5         0x00000200
    #define MARKER6         0x00000400
    #define MARKER7         0x00000800
    #define MARKER8         0x00001000
    #define MARKER9         0x00002000
    #define BOUNCE          0x00004000      /* That lovly TM 3.0 Bouncey thingy */
    #define SHOWFAILCMD     0x00008000      /* Show failed $commands defauilt error */
    #define NOUNDERLINE     0x00010000      /* Strip UNDERLINE character from ANSI */
    #define NONAME          0x00020000      /* Target does not display name with look */
    #define ZONEPARENT      0x00040000      /* Target zone allows inheritance of attribs */
    #define SPAMMONITOR     0x00080000      /* Monitor the target for spam */
    #define BLIND           0x00100000      /* Exits and locations snuff arrived/left */
    #define NOCODE          0x00200000      /* Players may not code */
    #define HAS_PROTECT     0x00400000      /* Player target has protect name data */
    #define XTERMCOLOR      0x00800000      /* Extended AnSI Xterm colors */
    #define HAS_ATTRPIPE    0x01000000      /* Attribute piping via @pipe */
    /* 0x02000000 free */
    /* 0x04000000 free */
    /* 0x08000000 free */
    /* 0x10000000 free */
    /* 0x20000000 free */
    /* 0x40000000 free */
    /* 0x80000000 free */


TOGGLES: Toggles are BITWISE masks taht need to be applied for each word like
the flags above.  They are added together for each word type

.. code-block:: c

    /* First word of toggles - Thorin 3/95 */
    #define TOG_MONITOR             0x00000001      /* Active monitor on player */
    #define TOG_MONITOR_USERID      0x00000002      /* show userid */
    #define TOG_MONITOR_SITE        0x00000004      /* show site */
    #define TOG_MONITOR_STATS       0x00000008      /* show stats */
    #define TOG_MONITOR_FAIL        0x00000010      /* show fails */
    #define TOG_MONITOR_CONN        0x00000020
    #define TOG_VANILLA_ERRORS      0x00000040      /* show normal error msg */
    #define TOG_NO_ANSI_EX          0x00000080      /* supress ansi stuff in ex */
    #define TOG_CPUTIME             0x00000100      /* show cpu time for cmds */
    #define TOG_MONITOR_DISREASON   0x00000200
    #define TOG_MONITOR_VLIMIT      0x00000400
    #define TOG_NOTIFY_LINK         0x00000800
    #define TOG_MONITOR_AREG        0x00001000
    #define TOG_MONITOR_TIME        0x00002000
    #define TOG_CLUSTER             0x00004000      /* Object is part of a cluster */
    #define TOG_SNUFFDARK           0x00008000      /* Snuff Dark Exit Viewing */
    #define TOG_NOANSI_PLAYER       0x00010000      /* Do not show ansi player names */
    #define TOG_NOANSI_THING        0x00020000      /* ... things */
    #define TOG_NOANSI_ROOM         0x00040000      /* ... rooms */
    #define TOG_NOANSI_EXIT         0x00080000      /* ... exits */
    #define TOG_NO_TIMESTAMP        0x00100000      /* Do not modify timestamps on target */
    #define TOG_NO_FORMAT           0x00200000      /* Override @conformat/@exitformat */
    #define TOG_ZONE_AUTOADD        0x00400000      /* Automatically add FIRST zone in list */
    #define TOG_ZONE_AUTOADDALL     0x00800000      /* Automatically add ALL zones in list */
    #define TOG_WIELDABLE           0x01000000      /* Marker to specify if object is wieldable */
    #define TOG_WEARABLE            0x02000000      /* Marker to specify if object is wearable */
    #define TOG_SEE_SUSPECT         0x04000000      /* Specify who sees suspect in WHO/MONITOR */
    #define TOG_MONITOR_CPU         0x08000000      /* Specify who sees CPU overflow allerts */
    #define TOG_BRANDY_MAIL         0x10000000      /* Define brandy like mail interface */
    #define TOG_FORCEHALTED         0x20000000      /* The item toggled can @force halted things */
    #define TOG_PROG                0x40000000      /* Can use @program on other people/things */
    #define TOG_NOSHELLPROG         0x80000000      /* Target can not issue commands inside a prog */

    /* Second word of toggles -- Ash */
    #define TOG_EXTANSI             0x00000001      /* Specify if target can used extended ansi naming */
    #define TOG_IMMPROG             0x00000002      /* Only an immortal can @quitprogram them */
    #define TOG_MONITOR_BFAIL       0x00000004      /* Monitor if a failed connect on bad character */
    #define TOG_PROG_ON_CONNECT     0x00000008      /* Reverse logic of program on connect */
    #define TOG_MAIL_STRIPRETURN    0x00000010      /* Strip carrage return in mail combining */
    #define TOG_PENN_MAIL           0x00000020      /* Use PENN style syntax */
    #define TOG_SILENTEFFECTS       0x00000040      /* Silents did_it() functionality on target */
    #define TOG_IGNOREZONE          0x00000080      /* Target is set to @icmd zones */
    #define TOG_VPAGE               0x00000100      /* Target sees alias in pages */
    #define TOG_PAGELOCK            0x00000200      /* Target issues pagelocks as normal */
    #define TOG_MAIL_NOPARSE        0x00000400      /* Don't parse %t/%b/%r in mail */
    #define TOG_MAIL_LOCKDOWN       0x00000800      /* Mortal-accessed mail/number and mail/check */
    #define TOG_MUXPAGE             0x00001000      /* Have 'page' work like MUX */
    #define TOG_NOZONEPARENT        0x00002000      /* Zone Child does NOT inherit parent attribs */
    #define TOG_ATRUSE              0x00004000      /* Enactor can use Attribute based USELOCKS */
    #define TOG_VARIABLE            0x00008000      /* Set exit to be variable */
    #define TOG_KEEPALIVE           0x00010000      /* Send 'keepalives' to the target player */
    #define TOG_CHKREALITY          0x00020000      /* Target checks @lock/user for Reality passes */
    #define TOG_NOISY               0x00040000      /* Always do noisy sets */
    #define TOG_ZONECMDCHK          0x00080000      /* Zone commands checked on target like @parent */
    #define TOG_HIDEIDLE            0x00100000      /* Allow wizards/immortals to hide their idle time */
    #define TOG_MORTALREALITY       0x00200000      /* Override the wiz_always_real setting */
    #define TOG_ACCENTS             0x00400000      /* Accents being displayed */
    #define TOG_PREMAILVALIDATE     0x00800000      /* Pre-Validate the mail send list before sending mail */
    #define TOG_SAFELOG             0x01000000      /* Allow 'clean logging' by the player */
    #define TOG_UTF8                0x02000000      /* UTF8 being displayed */
    /* 0x04000000 free */
    #define TOG_NODEFAULT           0x08000000      /* Allow target to inherit default attribs */
    #define TOG_EXFULLWIZATTR       0x10000000      /* Examine Wiz attribs */
    #ifdef ENH_LOGROOM
    #define TOG_LOGROOMENH          0x20000000      /* Enhanced Room Logging */
    #endif
    #define TOG_LOGROOM             0x40000000      /* Log Room's location/contents */
    #define TOG_NOGLOBPARENT        0x80000000      /* Target does not inherit global attributes */



POWERS:  Powers are handled a bit differently.  They're used as BITWISE shift
markers that you would have to compute the shift then add it after the fact.

.. code-block:: c

    /* First word of power positions.  Each position is 2 bits so the
       number here is how far over to shift the 2 bit pattern         */
    #define POWER_CHANGE_QUOTAS     0
    #define POWER_CHOWN_ME          2
    #define POWER_CHOWN_ANYWHERE    4
    #define POWER_CHOWN_OTHER       6
    #define POWER_WIZ_WHO           8
    #define POWER_EX_ALL            10
    #define POWER_NOFORCE           12
    #define POWER_SEE_QUEUE_ALL     14
    #define POWER_FREE_QUOTA        16
    #define POWER_GRAB_PLAYER       18
    #define POWER_JOIN_PLAYER       20
    #define POWER_LONG_FINGERS      22
    #define POWER_NO_BOOT           24
    #define POWER_BOOT              26
    #define POWER_STEAL             28
    #define POWER_SEE_QUEUE         30

    /* Second word of power positions. */
    #define POWER_SHUTDOWN          0
    #define POWER_TEL_ANYWHERE      2
    #define POWER_TEL_ANYTHING      4
    #define POWER_PCREATE           6
    #define POWER_STAT_ANY          8
    #define POWER_FREE_WALL         10
    #define POWER_EXECSCRIPT        12
    #define POWER_FREE_PAGE         14
    #define POWER_HALT_QUEUE        16
    #define POWER_HALT_QUEUE_ALL    18
    #define POWER_FORMATTING        20
    #define POWER_NOKILL            22
    #define POWER_SEARCH_ANY        24
    #define POWER_SECURITY          26
    #define POWER_WHO_UNFIND        28

    /* Third word of power positions. */
    #define POWER_OPURGE            0
    #define POWER_HIDEBIT           2 
    #define POWER_NOWHO             4
    #define POWER_FULLTEL_ANYWHERE  6
    #define POWER_EX_FULL           8
    #define POWER_API               10
    #define POWER_MONITORAPI        12
    #define POWER_WIZ_IDLE          14
    #define POWER_WIZ_SPOOF         16
    /* 18 free */
    /* 20 free */
    /* 22 free */
    /* 24 free */
    /* 26 free */
    /* 28 free */
    /* 30 free */

DEPOWERS:  like @powers they are handled with a BITWISE offshift that you
will have to calculate then add

.. code-block:: c

    /* First word */
    #define DP_WALL                 0
    #define DP_LONG_FINGERS         2
    #define DP_STEAL                4
    #define DP_CREATE               6
    #define DP_WIZ_WHO              8
    #define DP_CLOAK                10
    #define DP_BOOT                 12
    #define DP_PAGE                 14
    #define DP_FORCE                16
    #define DP_LOCKS                18
    #define DP_COM                  20
    #define DP_COMMAND              22
    #define DP_MASTER               24
    #define DP_EXAMINE              26
    #define DP_NUKE                 28
    #define DP_FREE                 30

    /* Second word */
    #define DP_OVERRIDE             0
    #define DP_TEL_ANYWHERE         2
    #define DP_TEL_ANYTHING         4
    #define DP_PCREATE              6
    #define DP_POWER                8
    #define DP_QUOTA                10
    #define DP_MODIFY               12
    #define DP_CHOWN_ME             14
    #define DP_CHOWN_OTHER          16
    #define DP_ABUSE                18
    #define DP_UNL_QUOTA            20
    #define DP_SEARCH_ANY           22
    #define DP_GIVE                 24
    #define DP_RECEIVE              26
    #define DP_NOGOLD               28
    #define DP_NOSTEAL              30
    /* Third word...and there was much rejoicing */
    #define DP_PASSWORD             0
    #define DP_MORTAL_EXAMINE       2
    #define DP_PERSONAL_COMMANDS    4
    /* 6  free */
    #define DP_DARK                 8
    /* 10 free */
    /* 12 free */
    /* 14 free */
    /* 16 free */
    /* 18 free */
    /* 20 free */
    /* 22 free */
    /* 24 free */
    /* 26 free */
    /* 28 free */
    /* 30 free */


ZONES:  Zones are special.  If there are no zones, the value will be '-1'.

So entering zones if there are no zones::

   -1


Entering zones if it has three zones (#123, #456, and #789)::

   123
   456
   789
   -1

As you see, the last value of the zone *MUST* be -1.  This tells it
that there are no more zones to add.
