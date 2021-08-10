.. _SNAP:

SNAP
====

Snap a bond or torsion angle in a Z-matrix geometry to the nearest value of the form
:math:`\arccos(\sqrt{a/b}) + 180 c` degrees for integers :math:`a`, :math:`b`, and :math:`c`
if they match to within approximately 2 to 3 decimal places.
Angles of this form are common in high-symmetry geometries, and ``SNAP`` is a convenience
that avoids having to type all of the significant figures of an irrational number to double precision.

Snapped angles are printed in the output file, and users should check that enough precision was provided for the desired snapping to occur.

Auto-detection is limited to :math:`|a| \le 7`.
