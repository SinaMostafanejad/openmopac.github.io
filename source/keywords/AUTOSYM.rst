.. _AUTOSYM:

AUTOSYM
=======

Automatically detects and imposes a subset of the coordinate constraints available with the :ref:`SYMMETRY` keyword.
Specifically, the type 1, 2, 3, and 14 Z-matrix constraints are applied to bond lengths that are within :math:`0.0001 \AA`
and bond or dihedral angles that are within :math:`0.0057^\circ`.
Constraints are not applied to unoptimized coordinates whose optimization flags are set to ``0``.

When the ``AUTOSYM`` keyword is used, the tail of the ``.arc`` file includes a list of coordinate constraints that can be used by an input file
if the ``AUTOSYM`` keyword is replaced by the ``SYMMETRY`` keyword.
