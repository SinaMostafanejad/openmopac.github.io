.. _MINI:

``MINI``
========

When very large molecules such as enzymes are modeled, the output can
become very large.  To reduce this, use ``MINI``.  When ``MINI`` is
present, only atoms whose coordinates are flagged with a "2" will be
printed.  During a run, atoms flagged with a "2" will be handled as if
they were flagged with a "1".  That is, the flag "2" will indicate an
atom that is marked for optimization. For reaction paths, the reaction
coordinate is normally "-1", if  ``MINI`` is present then the reaction
coordinate can be "-1" or "-2" ("-2" is obviously more likely). Although
``MINI`` works with all types of calculation, the main use would be for
calculations that involve reaction paths and IRC paths. 

``MINI`` is also useful when animations are involved, for example
mapping out a reaction path or following an IRC or DRC.   If
```HTML`` <html.html>`__ is present, then a HTML document will be
created that can be run using Firefox.  If ``GRAPHF``\ is present in
runs that produce animations then a file, <file>.xyz, will be
generated.  This can be visualized using Jmol.

When ``MINI`` and ``TS`` are both present, a transition state
optimization calculation is run, and only atoms that are flagged with
the symbol "2" will be printed; their positions will be changed during
the optimization run. All nearby atoms that are to be moved during the
optimization should be flagged with a "1", these atoms will not be
printed.  More distant atoms should be flagged with "0" to indicate that
their positions are fixed (frozen); they will not be printed.

``MINI`` and ```FORCETS`` <force.html>`__ can be used with internal or
Cartesian coordinates.  There are two ways to run ``MINI`` - ``FORCETS``
jobs:

(A) Running ``MINI`` and ``FORCETS`` in one job; this is not recommended
for large systems. Use keywords ``HTML FORCETS IRC MINI``  plus others,
to suit.  Set optimization flags to "2" for the atoms to be used in
``FORCETS``, and to "0" for all other atoms. 

(B) Running ``MINI`` and ``FORCETS`` in two jobs; this is the
recommended method for large systems.  In the first job, use keywords
``FORCETS ISOTOPE`` plus any others needed.  Set optimization flags to
"1" for the atoms to be used in ``FORCETS``, and to "0" for all other
atoms.  In a second job, use keywords ``HTML FORCETS IRC MINI RESTART``
plus others to suit. Use the same geometry plus flags as in the first
job.  To add an atom to the set of atoms printed, change its
optimization flags from "0" to "2".  This gives increased flexibility in
that the atoms used in the ``FORCETS``\ calculation need to be as few as
possible, because the ``FORCETS``\ calculation is CPU intensive, but
increasing the number of atoms printed in the ``IRC``\ calculation only
affects the files generated.

When ``MINI`` and ``0SCF``\ are both present then a file, <file>.xyz,
will be generated.

``MINI`` is useful when locating transition states, in ``FORCETS``
calculations, in following reaction paths, and in ```IRC`` <irc.html>`__
and ```DRC`` <DRC.html>`__ trajectories.

If ``PDBOUT`` is present, a PDB file will also be written; this file
will be complete.  So if a complete geometry is wanted, as well as the
minimized geometry, then add ``PDBOUT``. 

‡: Re-written August 2016

 
