----------------------------------------------------------------------------------------------------------
What may need to be modified to get softcode from PennMUSH, TinyMUSH2, TinyMUSH3, or MUX2 to work on Rhost
----------------------------------------------------------------------------------------------------------

RhostMUSH, for the most part, will work out of the box with most softcode gotten
from other codebases.  There are, however, exceptions.  Most of these exceptions
will be minor code differences between how ANSI is processed, the variences
of arguments or switches to commands or functions, or required flags.

Most changes will revolve around the ones listed in this document.

Problematic functions between codebases
---------------------------------------

lsearch()/search(), align()/printf(), *attrval()

Problematic features between codebases
--------------------------------------

named variables for regexp patterns in $commands are not supported.
@aliases on non-players are not supported.  Frankly I find them redundant.

Problematic commands
--------------------

@mapsql, hardcoded required comssytem commands (some are redundant)

SIDEFX flag
-----------

    Anything that uses sideeffects --DIRECTLY-- requires this flag.
    Sideeffects are like set(), pemit(), and so forth.  list(), while a 
    side-effect, does not require this flag as it is considered passive and safe.

Variable exits
--------------

    Rhost handles them slightly different.  You do not link
    exits to #-4.  That's an invalid destination.  I always found it, frankly,
    stupid to save any data in the database that was literally invalid.  So,
    you link the exit as you normally would, then @toggle the exit variable.
    At that point you use @exitto like you would any other codebase.

Zones
-----

    Zones actually can work near exactly as you would expect them to
    work on TinyMUSH, MUX, or Penn.  Either at once or at different times.
    We recognize multiple zones, zone masters, zone inheritance, zone 
    parenting, zone command processing, and the ability to bypass zones
    entirely.  There's a ton of flexbility with this.  However, the syntax
    for adding/removing zones is different so the commands will have to be
    ported to Rhost.

@powers
-------

    Powers work a bit differently in Rhost and they're named
    differently, which should not be that big a surprise as they're different
    between all the codebases anyway.  The big difference is our powers are
    tiered, meaning the can be limited or grown to a given bitlevel and are
    not just toggle powers like the other codebases.  We also have @depower
    that is the anti-thesis of @power

Attribute length
----------------

    While we have 64 character attribute capabilities like
    most other codebases, PennMUSH allows 1024 attribute length attributes.
    Why you need one that long boggles the mind, but if you do use attribs
    that long you need to make sure they are cut down to the proper length.

Attribute contents
------------------

    You'll be happy to know that Rhost allows upwards
    to 64,000 bytes of data to be assigned an LBUF.  We strongly recommand
    to cap at 32,000 however as the various TCP socket protocols play nicer
    with that value.

256 color
---------

Yup!  We got it.

Unicode/UTF8
------------

    Yup!  We got this too.  Not quiet yet in the main branch,
    but download Kage's branch, you won't be dissapointed.  We will have
    UTF8 in Rhost 4.0 when released.

Attributes per object
---------------------

    This is configurable with the VLIMIT @admin
    command, however, it is absolutely hard-limited at 10000 maximum.
    This is to avoid any DoS type situation and because frankly there
    should never be a reason to exceed that.  If you need more, use 
    @clusters.

Destroying
----------

    @nuke only works on players.  @destroy works on non-players.
    Never the two will meet.  We also have a built in recycle bin meaning
    anything destroyed will not be automatically recycled.  If you want it
    recycled, you have to @purge it.  Yes, if you use  Myrddin's CRON, it
    has a built in entry to auto-purge anything older than 30 days.  This
    also means you can on-line recover anything destroyed before that 30 
    days.  Groovy, eh?

object id's
-----------

Yup, we got them.  Even in searches, and, well, everything.

lsearch() and search()
----------------------

    lsearch() in Penn is not syntacically similar to non-Penn search().
    This will have to be altered.  In addition, search() in non-penn games
    have to have special consideration for escaping out the evaled args.

@locks can be different
-----------------------

    We have many more lock capabilities and options
    so this should be a non-issue.

Customer user-locks
-------------------

    We do not have custom user-locks like Penn.  We do, however, have the way
    to set encapsulated lock data into an attribute to fetch and compare
    against which I find more useful and far more flexible.  
    See: lockencode(), lockdecode(), and lockcheck()

Attribute trees
---------------

    Unlike Penn, we don't really have attribute trees.  We do support the
    basic capabilities of it for compatibility if you load in softcode that
    uses it, but it doesn't have the advanced features of attribute trees.
    Please see 'help attribute tree' for more information.

Prefix permission locking
-------------------------

    We do allow prefix permission locking, and some very advanced abilities
    of it.  Please see wizhelp on @aflags for more information.
    - wizhelp @aflags
    - wizhelp atrperms_max
    - wizhelp atrlock
    - wizhelp atrperms

align() and printf()
--------------------

    We do not have align().  Most of the code that uses align() will have to
    be converted to our printf() (which is compatible but has different syntax)

MySQL
-----

    While we support MySQL, we do not have an async method like MUX2.  This
    is just not possible, sorry.

Mail System
-----------

    There are mail wrappers to mimic MUX/TM3 and Penn mail systems.

Comsystem
---------

    The softcoded comsystem mimics MUX/TM3 and Penn's comsystem.

Various Functions
-----------------

    There is a 'softcode.minmax' in the Mushcode directory that loads up a slew
    of @function wrappers that will emulate various functions that MUX, Penn, or
    TM3 has.  We have the functionality for nearly all of them, but either our
    functions have different syntax, or we have different named functions that
    duplicate the functionality.  It would be far better to recode it to use
    the native functions, but the @function wrappers are there for lazyness :)

Empty Attributes
----------------

    Penn allows you to have empty attributes.  Non-penn codebases do not.  
    Thus, hasattrval and the like are not needed and should likely just point
    to hasattr instead.

Player Stats
------------

    MUX has some built in ways for player stats.  We do as well but they're 
    either done via functions or attribute contents.  Code that requires this
    will have to be recoded.

Percent Substitutions
---------------------

    Some percent substitutions may differ between codebases.  Luckily, Rhost
    allows the ability to remap or creaete new ones if this is a problem.

Switches
--------

    Some switches may not exist in Rhost that do in other codebases, in such
    a case, Rhost does allow the ability to @hook a command to define your own
    softcoded switch to a hardcoded command and work around the limitation.

Flags
-----

    Some flags may be missing.  If it's a dummy flag, feel free to use the
    marker flags MARKER0 to MARKER9 to set them.  If it's an existing flag
    that does similar features, feel free to flag_alias it or just flag_name
    it to the other name if you want.  

Aliases
-------

    Multiple aliases are supported via @protect.
