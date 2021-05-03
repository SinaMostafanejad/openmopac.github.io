.. _P:

 

``P=n.nn`` 
-----------

The effect of an applied pressure on a solid can be simulated by
``P=n.nn``, where ``n.nn`` is the pressure in Newtons per square meter,
or ``P=n.nnGpa``, where ``n.nn`` is the pressure in Gigapascals.

Typical bulk moduli are in the order of 10 - 700 GPa (gigapascals), and
typical pressures should be ``n.nn`` = 1.D\ :sup:`9` to ``n.nn``
=1.D\ :sup:`10` NM\ :sup:`-2`. In general, solids are subjected to
compression only, not tension, therefore the sign of ``n.nn`` should
normally be positive, e.g. ``P=2.D9`` or ``P=2.0GPa,`` however, for
mechanically strong solids, negative pressures, even quite large
pressures, can be used.

As the pressure rises, the calculated heat of formation will become more
positive because energy must be used in generating the volume of the
solid under pressure. Geometry optimization minimizes the total heat of
formation =ΔH\ :sub:`f` of the solid + energy due to volume. The final
geometry is then the optimized geometry at equilibrium with that
pressure.

Bulk moduli, B, in Pascals, can be calculated from the change in unit
cell volume at zero pressure (Vol(0)) to the unit cell volume under a
pressure of ``P=n.nn`` (Vol(``n.nn`` ) from:

B=n.nn*Vol(0)/(Vol(0)-Vol(n.nn))

For polymers, the applied strain is in units of Newtons per mole. That
is, for one mole of polymer chains, stacked side by side, the applied
force is ``n.nn`` Newtons. Suitable values for ``P=n.nn`` are in the
order of 10\ :sup:`13` Newtons. In general, polymers are subjected to
tension only, not compression, therefore the sign of ``n.nn`` should
normally be negative, e.g. ``P=-2.D13`` .

Useful conversion factors are:

1 GPa = 10\ :sup:`9`\ N.M\ :sup:`-2` =
10\ :sup:`10`\ dynes.cm\ :sup:`-2` = 10\ :sup:`16`\ erg.m\ :sup:`-3`

1 GPa = 6.0221367/(4.184*10)kcal.mol\ :sup:`-1`.Angstrom\ :sup:`-3` =
0.14393kcal.mol\ :sup:`-1`.Angstrom\ :sup:`-3`.

so a unit cell of  100A\ :sup:`3` under 1 GPa would have an energy
equivalent of 14.39 kcal.mol\ :sup:`-1`.
