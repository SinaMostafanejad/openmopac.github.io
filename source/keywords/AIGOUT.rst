.. _AIGOUT:

AIGOUT
======

Prints the final molecular geometry to the MOPAC archive file (``.arc``) in :ref:`Gaussian_Zmatrix_format`.
All symmetry-inequivalent bond distances and angles are assigned symbols.
Any symbols used in the input file are preserved, otherwise a new symbol is automatically assigned.
The new symbols begin with ``r`` for bond lengths, ``a`` for bond angles, and ``d`` for dihedral angles,
followed by a list of numbers denoting the atoms involved in the particular geometric quantity.
Bond lengths are specified by two atoms, bond angles are specified by three atoms,
and dihedral angles are specified by four atoms.
