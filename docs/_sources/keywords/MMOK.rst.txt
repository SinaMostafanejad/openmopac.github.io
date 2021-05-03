.. _MMOK:

``MMOK``
========

Recently, July 2013, a Molecular Mechanics correction was added to RM1,
PM6, and PM7.  MM corrections have been available for MNDO, AM1, and PM3
for a long time.  Because of the recent change to RM1, PM6, and PM7,
keyword ``MMOK`` must be used if the molecular mechanics correction is
wanted.  ``MMOK`` is only needed if peptide bonds are present.
Eventually ``MMOK`` will become the default, and the keyword will become
redundant.

If the molecular mechanics correction is not wanted, then
```NOMM`` <nomm.html>`__ should be used.

If the system contains a peptide linkage, then when a molecular
mechanics correction is made the barrier to rotation about the peptide
bond is increased (to 14.00 kcal/mol in N-methyl acetamide).

The peptide linkage consists of the group -CO-NH-.  In most instances
the O=C-N-H torsion or dihedral angle is near to 180° and in a few
instances the angle is roughly 0°, in other words, most peptide bonds
are more-or-less flat.  In proteins, because of environmental effects,
the deviation of the angle from these ideal angles can be greater.   The
most important deviations from planarity occur when a peptide bond
changes from cis to trans or vice versa.  During such reactions the
torsion angle goes through 90°.  In the case of N-methyl-acetamide, the
barrier to rotation has been calculated, using highly accurate ab-initio
methods, to be about 14 kcal/mol.  Semiempirical methods predict a
smaller barrier.  To correct this fault, a small molecular mechanics
correction is added to the calculated heat of formation; this correction
has the form:

ΔH\ :sub:`f`' = ΔH\ :sub:`f` +c.sin(θ)\ :sup:`2`

where c is a constant depending on the semiempirical method, and f is
the O=C-N-H torsion angle.  Obviously, if the torsion angle is 180° or
0°, i.e., the default peptide bond angle, then no correction will be
made, but for all other angles there is an energy penalty that biases
the peptide bond towards planarity.

In practice, this MM correction to the peptide bond produces an
insignificant bias towards planarity in proteins, because most peptide
bonds in proteins are almost planar anyhow, and a significant change in
barrier heights when reactions involving twisting a peptide bond are
modeled.
