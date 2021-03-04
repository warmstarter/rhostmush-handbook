--------------------------------------------------------------------------------
What FLAGS, TOGGLES, POWERS, and DEPOWERS mean in RhostMUSH
--------------------------------------------------------------------------------

Flags
-----

Flags are pretty much exactly the same as any other mush.  It's a flag
that you set or unset on a target which then enables/disables or 
alters something that target can do.  There's help on all the flags 
in help and wizhelp.  

Toggles
-------

Toggles were designed as a single point flag that immediately enables
or disables a set ability or condition, thus a 'toggle'.  It works 
exactly like a flag and was originally designed for two reasons.  To
distinguish from the multi-meaning of a 'flag', and because frankly
we ran out of flag space :)

@power
------

A power is similar to a power on other mushes, but unlike them, our
powers are multi-tier.  This means that they can be customized to
empower something at a given bitlevel.  You may empower something
from guildmaster up to councilor level.  There are some powers 
with a power level of N/A meaning they are a toggle power granting
an absolute power level as specified in the help for that power.
This requires the INHERIT flag for non-players to inherit powers,
however, a specific object can be granted a power as well.

@depower
--------

This is the anti-thesis of @power.  Also, depowers do not require
inheritance.  They also have priority over flags, toggles, and
powers.  You can use depower to remove or lower abilities and
control from a target, even a full wizard (royalty) can be 
depowered.
