.. _AIGOUT:

``AIGOUT``
==========

The ARCHIVE file contains a data-set suitable for submission to MOPAC.
If, in addition to this data-set, the Z-matrix for Gaussian input is
wanted, then ``AIGOUT`` (*ab initio* geometry output), should be used.

The Z-matrix is in full Gaussian form. Symmetry, where present, will be
correctly defined. Names of symbolics will be those used if the original
geometry was in Gaussian format, otherwise 'logical' names will be used.
Logical names are of form ``<t><a><b>[<c>][<d>]`` where ``<t>`` is  'r'
for bond length, 'a' for angle, or 'd' for dihedral, ``<a>`` is the atom
number, ``<b>`` is the atom with which ``<a>`` is related, ``<c>``, if
present, is the atom number to which ``<a>`` makes an angle, and
``<d>``, if present, is the atom number to which ``<a>`` makes a
dihedral.
