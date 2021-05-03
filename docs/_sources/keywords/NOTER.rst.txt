.. _NOTER:

``NOSYM``
=========

By default, symmetry point-groups are automatically assigned, and used
in identifying the irreducible representations of molecular orbitals,
vibrations, and states, and in accelerating the construction of the
Hessian in FORCE calculations.

Sometimes a system almost has the symmetry of a point group higher than
C\ :sub:`1`. Minor deviations from exact symmetry are allowed, but these
sometimes cause difficulties. If that happens, then the job will fail.
To prevent this happening, the symmetry can be re-defined as
C\ :sub:`1`. This effectively disables all the symmetry features, so
some jobs, particularly ```FORCE`` <force.html>`__ calculations, will
take longer to run.

Use ``NOSYM`` if there is any reason to suspect that the point-group
symmetry features are causing problems.

A second type of symmetry can be used by specifying  ``SYMMETRY``.  This
is distinct from the default of using the point-group of the system to
label irreducible representations and to accelerate ``FORCE``
calculations. When ``SYMMETRY`` is used, the symmetry relations between
coordinates are defined by the user.  These can be used for defining the
point-group of a molecule, for example the D\ :sub:`6h` of benzene, but
no point-group theory is used when ``SYMMETRY`` is specified. 
