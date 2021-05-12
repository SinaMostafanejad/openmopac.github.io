.. _DISP:

``DISP``
========

Although post-SCF hydrogen bonding and dispersion energy contributions
are calculated, they are not normally printed.  To print these
contributions, add keyword ``DISP``.

If a list of hydrogen bonds is wanted, use ``DISP(n.nn)``, where n.nn is
the value of the cutoff for printing hydrogen bonds.  If ``DISP(1.0)``
is used, all hydrogen bonds with a strength of 1.0 or more
kcal.mol\ :sup:`-1` will be printed.  This is the common cutoff for
hydrogen bonds.
