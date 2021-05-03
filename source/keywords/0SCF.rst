.. _0SCF:

``0SCF``
========

The data can be read in and then printed, but no actual calculation is
performed when this keyword is used. This is useful as a check on the
input data. All obvious errors are trapped, and warning messages
printed. A second use is to convert from one format to another. The
input geometry is printed in various formats in a ``0SCF`` calculation.
Normally, only the Cartesian coordinate and MOPAC Z-matrix geometries
are printed, however other geometries can also be printed if other
keywords are used, e.g. ``AIGOUT``.
