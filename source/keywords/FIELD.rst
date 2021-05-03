.. _FIELD:

``FIELD=(n.nn,m.mm,l.ll)``
==========================

An external electric field of intensity *n*.\ *nn* volts/Ångstrom in the
*x*-direction, *m*.\ *mm* volts/Ångstrom in the *y*-direction, and
*l*.\ *ll* volts/Ångstrom in the *z*-direction is to be applied. The
potential arising from the field is zero at the origin of Cartesian
space, i.e. *V*\ =0 at (*x*\ =0.0, *y*\ =0.0, *z*\ =0.0). At any other
point, (*x,y*,\ *z)*, the effect of ``FIELD=(n.nn,m.mm,l.ll)`` is to
produce a potential equal to *V* = (*x.n.nn+y.m.mm+z.l.ll)* volts.\ ````

The effect on a molecule depends on the orientation of the molecule
relative to the field.  Thus a hydrogen molecule would be polarized
slightly by a field parallel to the axis, but unaffected by a field
perpendicular to the axis.  The polarization would be to produce a small
positive charge on the hydrogen in the (relatively) negative part of the
field, and a small negative charge in the positive part of the field. 
Any polarization would, of course, result in the energy being lowered.

Because molecules have no net charge, the effect of an applied field is
independent of the location of the molecule.  That is, if the field is
defined by FIELD=(1.0,0.0,0.0), the energy of a molecule centered at
(+100,0,0) would be the same as that at (-100,0,0) and the same as that
at (0,0,0). Put another way, the energy would be unaffected by motion in
any direction, including in the direction of the field.

The geometries of small molecules are only slightly affected by fields
in the order of 1 volt per Angstrom.  This is because such a molecule
is, of its nature, small.  The change in potential from one end of such
a molecule to the other would only be a few volts.  Larger systems are
affected much more - a system that extends over 20A, say, would
experience a potential change of 20 volts, if the field were along that
axis.  Macroscopic changes, such as Zener breakdown, are the result of
ions being accelerated by the field.  When these ions collide with
neutral molecules, the molecules become ionized, e.g. e\ :sup:`-` +
N\ :sub:`2` => 2e\ :sup:`-` +N\ :sub:`2`\ :sup:`+`.

On the other hand, an ion will be strongly affected by such a field. For
example, F\ :sup:`-1` at coordinates 1.00, 0.00, 0.00, would be
stabilized by 1.0eV if a field were to be applied by specifying
``FIELD=(1.0,0.0,0.0)``. This is a direct consequence of the net charge
on the system interacting with the electric field: a charge of +\ *x* at
a point in space where the potential is *y* volts would have an energy
due to the potential of *x.y* eV.  This is the origin of the term
electron-volt.

A useful exercise is to monitor the behavior of an ion in an electric
field, using the ``DRC``:

Let the field be FIELD=(1,0,0), let the ion be F\ :sup:`-`,  and have a
mass of 19 amu.  The data set:

| DRC LARGE T-PRIO=0.1 CHARGE=-1 FIELD=(1,0,0) GNORM=0 CYCLES=75
| Fluoride ion
| In An Electric Field
| F 0.0 0 0.0 0 0.0 0

would be suitable here.  After about 63fs, the ion would have moved
through 1 Angstrom, and the potential energy would have dropped by 23.06
kcal/mol.  Conservation of energy requires that the kinetic energy
equals 23.06 kcal/mol. Using E=(1/2)MV\ :sup:`2`,  implies that the
velocity is:

V = (2*4.184*10:sup:`10`\ \*23.06/19) cm/sec = 3.19*10\ :sup:`5` cm/sec
= 3.19 km/sec.

| The 4.184*10\ :sup:`10` is the `conversion <fun_con.html>`__ from
  kcal/mol to ergs per mol. 
| All other quantities, such as the acceleration (5.06x10:sup:`18`
  cm/sec\ :sup:`2` or 5.06x10\ :sup:`13` km/sec\ :sup:`2`), follow
  simply. 
| Used in this way, the ``DRC``\ is useful for modeling ion
  implantation.
