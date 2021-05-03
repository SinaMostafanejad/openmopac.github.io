.. _ampersand:

``&``
=====

An '``&'`` means 'turn the next line into keywords'. An '``&'`` on line
1 would mean that a second line of keywords should be read in. If that
second line contained an '``&``', then a third line of keywords would be
read in. If the first line has an '``&``' then the first description
line is omitted; if the second line also has an '``&``', then both
description lines are omitted.

Examples: Use of one '``&``'

::

   VECTORS DENSITY RESTART & NLLSQ T=1H SCFCRT=1.D-8 DUMP=30M
   PM3 FOCK OPEN(2,2) ROOT=3 SINGLET SHIFT=30
   Test on a totally weird system

Use of two '``&``'s

::

   LARGE=-10 & DRC=4.0 T=1H SCFCRT=1.D-8 DUMP=30M ITRY=300 SHIFT=30
   PM3 OPEN(2,2) ROOT=3 SINGLET NOANCI T-PRIORITY=0.5 &
   LET GEO-OK VELOCITY KINETIC=5.0
