.. _VECTORS:

``VECTORS``
===========

The eigenvalues, in eV, and eigenvectors are to be printed. In UHF
calculations both alpha and beta eigenvectors are printed; if
```ALLVEC`` <allvec.html>`__ is specified, in all cases the full set,
occupied and virtual, are output. By default, the nine highest occupied
and the seven lowest unoccupied levels are printed. The eigenvectors are
normalized to unity: that is, the sum of the squares of the coefficients
is exactly one. If ```DEBUG`` <debug.html>`__ is specified, then the
eigenvectors on *every* iteration of every SCF calculation will be
printed. This is useful in a learning context, but would normally be
undesirable.

A set of *n* eigenvectors around the HOMO-LUMO gap can be printed by
using ``VECTORS=(n)``.  To print the *n* highest occupied and *m* lowest
unoccupied M.O.s, use ``VECTORS=(n,m)``.

If ```LOCAL`` <localize.html>`__ is used, the localized molecular
orbitals will be printed

If ```MOZYME`` <mozyme.html>`__ is used, then the localized molecular
orbitals will be printed.  If the eigenvectors are wanted, then
```EIGEN`` <eigen.html>`__ must also be present.
