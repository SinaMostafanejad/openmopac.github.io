.. _HCORE:

``HCORE``
=========

Print all parameters used in the calculation, the one-electron matrix,
and two electron integrals .  This keyword should normally only be used
with ``1SCF``, otherwise the output can be very large.

Two electron integrals are in the order: All integrals for atoms 1 with
1, 1 with 2, 2 with 2, 1 with 3, 2 with 3, 3 with 3, etc.  Within an
atom-pair, the integrals are, in order:

<ss|ss> <ss|sx> <ss|xx> <ss|sy> <ss|xy> <ss|yy> ... <sx|ss> ...
<(xy)(xy)|(xy)(xy)>

`Atomic orbitals <real_spherical_harmonics.html>`__ are, in order: s x y
z (x2-y2) (xz) (z2) (yz) (xy)

The number of two-electron integrals can be quite large; for two atoms
with d-orbitals (l = 2)  there are 2025  = 45\ :sup:`2` =
((9*10)/2):sup:`2` = ((l + 1)\ :sup:`2`\ \*((l + 1)\ :sup:`2` +
1)/2)\ :sup:`2` distinct integrals.

``HCORE`` is useful in diagnostic work - understanding how SCF methods
work and in finding bugs in the program.
