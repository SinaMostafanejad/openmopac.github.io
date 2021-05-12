.. _ALLBONDS:

``ALLBONDS``
============

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
