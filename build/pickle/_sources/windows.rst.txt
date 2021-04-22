.. _windows-requirements:

===============================
 Requirements if Using Windows
===============================

* (BETA ONLY) cygwin under Windows.  It requires the entire base development set and Requirements below.

----------------------------------
Installing on Windows 10 with BASH
----------------------------------

Rhost can be compiled and run under the new Bash on Ubuntu on Windows.
This has been tested with the Preview build 14342.

#. After installing Bash you will need to install the following packages:

   - gcc
   - git
   - make
   - libpcre3 (optional)
   - libpcre3-dev (optional)
   - openssl (optional)

#. When configuring rhost (using confsource) select the Disable Debugmon 
option.

---------------------------------
Installing on Windows with Cygwin
---------------------------------

Rhost does work under windows using the cygwin package.

#. When you do install cygwin, the following packages must be added:

   - bash
   - crypt
   - gcc
   - gdbm
   - git
   - make
   - openssl (optional)

#. The src/Makefile has to manually have the CYGWIN line uncommented.

----------------------------
Startig RhostMUSH on Windows
----------------------------

When you issue Startmush, you must pass it the -cyg option.
