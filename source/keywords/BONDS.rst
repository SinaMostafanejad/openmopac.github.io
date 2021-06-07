.. _BONDS:

``BONDS``
=========

The rotationally invariant bond order [`15 <references.html#bonds>`__]
between all pairs of atoms is printed. In this context a bond is defined
as the sum of the squares of the density matrix elements connecting any
two atoms. For ethane, ethylene, and acetylene, the carbon-carbon bond
orders are roughly 1.00, 2.00 and 3.00 respectively. The diagonal terms
are the valencies calculated from the atomic terms only and are defined
as the sum of the bonds the atom makes with other atoms. In RHF
calculations, the total density matrix (alpha plus beta density
matrices) is perfectly duodempotent, that is, the square of the density
matrix, P, is exactly two times the density matrix, or P*P = 2*P (see
`Bond Orders <bond_orders.html#bonds>`__), and valencies will be
correct.  In UHF and non-variationally optimized wavefunctions the
calculated valency will be incorrect, the degree of error being
proportional to the non-duodempotency of the total density matrix. (In
UHF work, the individual alpha and beta  density matrices are
idempotent, that is, P(alpha)*P(alpha) = 1.0*P(alpha) and
P(beta)*P(beta) = 1.0*P(beta), but, in general, the sum of these two
matrices is not duodempotent, i.e.,
(P(alpha)+P(beta))*(P(alpha)+P(beta)) ≠. 2.0*(P(alpha)+P(beta)).)

The bonding contributions of all M.O.s in the system are printed
immediately before the bonds matrix. The idea of molecular orbital
valency was developed by Gopinathan, Siddarth, and
Ravimohan [`23 <references.html#m_o_valency>`__]. Just as an atomic
orbital has a 'valency', so does a molecular orbital. This leads to the
following relations: The sum of the bonding contributions of all
occupied M.O.s is the same as the sum of all valencies which, in turn is
equal to two times the sum of all bonds. The sum of the bonding
contributions of all M.O.s is zero.

In ```MOZYME`` <mozyme.html>`__ calculations, only bonds of order
greater than 0.01 and those that do not involve hydrogen atoms are
printed.  If ``ALLBONDS`` is present, all bonds of order greater than
0.001, including hydrogen atoms, are printed.

If ``LARGE`` is present, then the Medrano-Bochicchio-Reale population
analysis is printed. For each atom, the following quantities are
generated:

-  The non-shared charge (sometimes called the self or inactive charge).
-  The charge used to form bonds with other atoms (the active charge).
-  The total charge (the sum of the first two terms).
-  The valence (from the bonds matrix).
-  The free valence (the difference of the last two terms).
-  The statistical promotion (total charge minus core charge).
-  The "Mulliken promotion"

Note that the last two terms are expressed in units of the electron, not
the proton charge.

For more information, see
[`24 <references.html#nrm85>`__,\ `25 <references.html#mrb86>`__,\ `26 <references.html#mb89>`__,\ `27 <references.html#rb91>`__],
and also see J. A. Medrano, R. C. Bochicchio, S. G. Das, "The ROHF
Extension of the Statistical Population Analysis of Electron and Spin
Densities", J. Phys. B.

Discarded text from ALLBONDS:

When keyword ``BONDS`` is used in a ``MOZYME`` calculation, only those
bonds with bond orders greater than 0.01 and that do not involve
hydrogen atoms are printed. This is to reduce the size of the output.
When ``ALLBONDS`` is used, all bonds with bond orders greater than 0.001
are printed. This includes bonds involving hydrogen atoms.

This prints the rotationally invariant bond order between atoms that are
near to each other. In this context a bond is defined as the sum of the
squares of the density matrix elements connecting any two atoms. For
ethane, ethylene and acetylene the carbon-carbon bond orders are roughly
1.00, 2.00 and 3.00, respectively. See also  ``BONDS``.

Valencies are calculated from the atomic terms only and are defined as
the sum of the bonds the atom makes with other atoms.
