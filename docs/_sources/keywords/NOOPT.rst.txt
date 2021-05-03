.. _NOOPT:

``NOOPT, NOOPT-X``
==================

Turn off all optimization flags for atoms of type X.  This keyword is
useful for partial geometry optimizations.  If "-X'" is missing, turn
off all optimization flags. If \ ``OPT-X``  is present, optimization
flags can be turned on after ``NOOPT`` has been run, so to optimize the
positions of hydrogen atoms while freezing the positions of all other
atoms, use "``NOOPT OPT-H``".

If  ``OPT("label"=n.nn)``\ is present, then this will be run first, then
``NOOPT`` will turn off all optimization flags for atoms containing the
label "label".
