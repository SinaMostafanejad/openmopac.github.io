.. _CUTOFP:

``CUTOFP=n.nn``
===============

In polymers and solids, a cutoff distance, in Ångstroms, is needed in
order to ensure that every atom has a correct electric environment. If
no cutoff is set, then equivalent atoms would experience different
electric fields. The ``CUTOFP`` distance is set, by default, to 30
Ångstroms. In calculating the potential due to distant atoms, atoms
separated by more than ``CUTOFP`` are treated as if they were at
distance ``CUTOFP``.

```MOZYME`` <mozyme.html>`__ calculations run faster when smaller values
of ``CUTOFP`` are used  A suitable value for *n.nn* is somewhere between
10.0 and 15.0.  This will give a large increase in speed. But first, run
a test calculation to verify that the results don't change much.

When ``CUTOFP`` is less than the default, the number of two-electron
integrals is reduced.  This can allow larger systems to be run.
