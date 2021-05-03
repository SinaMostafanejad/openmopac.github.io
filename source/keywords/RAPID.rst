.. _RAPID:

``RAPID``
---------

When only part of a geometry is being modified, the speed of a
``MOZYME`` SCF calculation can be increased by the use of ``RAPID``.
Thus, if a side-chain on a protein is being optimized, all atoms on the
side-chain would be flagged with " 1 "s, and all other atoms would be
flagged with " 0 "s. An atom is considered as being modified if any one
of the three flags is " 1 ".  ``RAPID`` should not be used if many atoms
are to be optimized and those atoms are not all in one part of the
molecule.  For example, ``RAPID`` should not be used with
``NOOPT OPT-H.``

Because of limitations in ``RAPID``, the termination criterion should be
quite large - say ```GNORM`` <gnorm.html>`__\ =5 or more.  Also, after a
``RAPID`` calculation, a conventional ``MOZYME`` calculation should be
run, in order to get a more correct heat of formation.

If the following conditions are used, the optimization will run
smoother:

| 1. Use Cartesian coordinates.
| 2. Before using ``RAPID``, a useful step is to optimize the whole
  system.

 The effort to set up a system with ``RAPID`` is well worth while,
particularly if only a few (up to 10-20%) of the atoms are flagged.

As an example of the effect of using  ``RAPID``, for a decapeptide
containing 143 atoms, with the coordinates of the atoms of the last
residue being optimized, the times required for 10 cycles of geometry
optimization are as follows:

.. raw:: html

   <div align="center">

+-----------------------------------+-----------------------------------+
| Method                            | Time (s)                          |
+-----------------------------------+-----------------------------------+
| Using conventional MOPAC          | 19.4                              |
+-----------------------------------+-----------------------------------+
| Using MOZYME                      | 5.5                               |
+-----------------------------------+-----------------------------------+
| Using MOZYME with RAPID           | 2.8                               |
+-----------------------------------+-----------------------------------+

.. raw:: html

   </div>

See also ```OPT("Label"=n.nn)`` <opt_label.html>`__
