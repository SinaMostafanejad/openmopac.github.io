.. _OPT:

``OPT, OPT-X``
==============

Turn on all optimization flags for atoms of type X.  This keyword is
useful for partial geometry optimizations.  If "-X'" is missing, turn on
all optimization flags. If  ``NOOPT-X``  is present, optimization flags
can be turned off before ``OPT`` is run, so to optimize the positions of
hydrogen atoms while freezing the positions of all other atoms, use
"``NOOPT OPT-H``".
