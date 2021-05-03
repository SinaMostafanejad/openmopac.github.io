.. _ANGSTROMS:

``A0`` or\ ``ANGSTROMS``
========================

For most geometries, the choice of units is unambiguous.  Standard
`MOPAC <geometry_specification.html>`__ and `Gaussian 
input <gaussian_z.html>`__ is in Ångstroms, 
`TURBOMOLE <TURBOMOLE_geometry.html>`__ input is in atomic units. In
these cases, do not use ``A0`` or ``ANGSTROMS``.

If  ``A0`` is present, the input geometry will be regarded as being in
atomic units.

If ``ANGSTROMS``\ is present, the input geometry will be regarded as
being in Ångstroms.

If neither ``A0`` nor ``ANGSTROMS`` are present, then the default will
be used.
