.. _SETUP:

``SETUP``
=========

If, on the keyword line, the word '``SETUP``' is specified, then a line
of keywords will be read from a file with the name SETUP. The file SETUP
or (optionally) SETUP.txt must exist.  As with the normal keyword line,
if "`++ <plusplus.html>`__" is used, the line of keywords can be split
into two or more lines. Keywords in SETUP are put after all keywords in
the data set.

Keywords in the data-set will take precedence over similar keywords in
the SETUP file.  For example, if  "CHARGE=0" is present in the SETUP
file, and the data-set contains "CHARGE=2", then "CHARGE=0" will be
ignored. 

Any keyword in the data-set that is preceded by a minus sign, e.g.,
-PM6, will remove that keyword from the SETUP file before the job
starts.

Any keyword in ``SETUP`` that is preceded by a minus sign, e.g., -PM6,
will remove that keyword from the data-set file before the job starts.

``SETUP`` is particularly useful when running a large number of jobs
that all use the same or similar keywords.  Thus if a set of
calculations involving PM6 are to be run, then the ``SETUP`` file could
contain the keyword PM6.  The run would then produce a set of archive
files, all with the keyword PM6 present.  If, later on, the set of
archive files files needed to be run using PM7, then the ``SETUP`` file
could contain " -PM6 PM7"

The location of the ``SETUP`` file and its name can be changed by use of
``SETUP=<name>``\ or\ ``SETUP=<file location and name>``, e.g.,
``SETUP=protein.txt, SETUP=C:/Users/My_setup.txt,``
or\ ``SETUP="C:/my files/My setup.txt"``\ or by specifying the setup
file directly, in which case the name of the setup file must begin with
the word "SETUP", e.g., SETUP_for_PM6-D3H4.txt. For proteins, a useful
set of keywords to have in the ``SETUP`` file is:
``MOZYME EPS=78.4  T=``\ `2w <t=n.html>`__

Limitations on SETUP names
--------------------------

Setup names must NOT contain keywords.  For example, SETUP="Step 1 -
ADD-H.txt" should not be used because  ADD-H is a keyword. Also, the
string " -" is used to indicate that a keyword in the data-set is to be
ignored.

Use in recursive jobs (`Example <setup.zip>`__)
-----------------------------------------------

A SETUP file can include a SETUP file, for example, if hydrogen atoms
are to be added to a system, and then their positions are to be
optimized, the contents of the SETUP file would be:

ADD-H SETUP="Optimize positions of hydrogen atoms.txt"

The ARC file produced by this job could then be used as a data-set for a
second job in which the positions of the hydrogen atoms were optimized. 
This second job would use the included file "Optimize positions of
hydrogen atoms.txt" and this file would contain the keywords for the
optimization, and, optionally, another SETUP file for use by a
subsequent job.

NOOPT OPT-H SETUP="Optimize all atom positions.txt"

 

 
