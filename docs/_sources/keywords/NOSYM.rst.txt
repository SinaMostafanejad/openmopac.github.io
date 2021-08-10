.. _NOSYM:

NOSYM
=====

Suppress the automatic detection of point-group symmetry and set the system's point group to be :math:`C_1`.

By default, point-group symmetry is used to identify the irreducible representations
of molecular orbitals, atomic vibrations, and many-electron excitations,
and to accelerate the construction of the Hessian in :ref:`FORCE` calculations.
However, symmetric geometries are allowed small numerical deviations from perfect symmetry,
which can sometimes cause errors and premature termination of a calculation.

``NOSYM`` is useful for verifying that point-group symmetries are functioning correctly,
but some calculations will take longer to run and calculated states will no longer have symmetry labels.
