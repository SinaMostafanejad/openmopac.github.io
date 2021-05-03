.. _STATIC:

``STATIC``
==========

The static polarizability is calculated. An electric field gradient is
applied to the system, and the response is calculated. The dipole and
polarizability are calculated two different ways, from the change in
ΔH\ :sub:`f` and from the change in dipole. A measure of the imprecision
of the calculation can be obtained by comparing the two quantities.
Greater precision can be obtained by increasing the precision of the SCF
(``RELSCF=0.1`` or ``RELSCF=0.01``).

In 2004, the polarizability volume reported was modified by the use of
`additive corrections <additive_corrections.html>`__.

In ``STATIC``, 37 or 38 SCF calculations are involved. The
polarizability involves 36 calculations, one for each electric field.
The fields are +X, -X, +2X, -2X, +Y, -Y, +2Y, -2Y, +X+Y, -X+Y, -X-Y,
+X-Y, +2X+2Y, -2X+2Y, -2X-2Y, +2X-2Y, +Z, -Z, +2Z, -2Z, +X+Z, -X+Z,
-X-Z, +X-Z, +2X+2Z, -2X+2Z, -2X-2Z, +2X-2Z, +Y+Z, -Y+Z, -Y-Z, +Y-Z,
+2Y+2Z, -2Y+2Z, -2Y-2Z, and +2Y-2Z. These are used in the construction
of a three by three secular matrix, which is then diagonalized, giving
the orthogonal polarizabilities.

See also ```POLAR`` <polar.html>`__
