.. _SPARKLE:

``SPARKLE``
===========

The lanthanides can be represented by their fully ionized 3+  sparkles. 
That is, they have no basis set, and therefore cannot have a charge
different from +3.000.  To use these sparkles, add keyword ``SPARKLE``.

See also `SPARKLES <sparkles.html>`__ These entities do not need keyword
``SPARKLE``.

If ``SPARKLE`` is present, and it's not needed, it will be ignored.

The geometries of the lanthanides are reproduced with good accuracy, but
the heats of formation and electronic properties are not accurate.

To specify Dysprosium 3+ ion, use ``SPARKLE``, and symbol Dy at the
appropriate point in the Z-matrix.

"f" Orbitals
------------

Lanthanides 3+ ions have partially filled "f" shells, with the number of
"f" electrons ranging from 0 (lanthanum) to 14 (lutetium).  These
electrons are important in the spectroscopy of Ln\ :sup:`3+` complexes,
where their excited states are represented in the UV-Vis spectra by
quite sharp lines.  That the lines are quite sharp indicates that the
"f" electrons do not contribute significantly to covalent bonding.
Therefore, in semiempirical methods, lanthanide ions are represented by
an unpolarizable core consisting of the nucleus, all the electrons up to
Xenon, and zero or more "4f" electrons.  Only Ln\ :sup:`3+` ions are
available using the sparkle model, so the configurations used are
La\ :sup:`3+`: [Xe]4f:sup:`0`; Ce\ :sup:`3+`: [Xe]4f:sup:`1`; ...
Lu\ :sup:`3+`: [Xe]4f:sup:`14`.  Although not used in semiempirical
theory, the ground states of these ions can be thought of as
La\ :sup:`3+`: 1S\ :sub:`g`; Ce\ :sup:`3+`: 2F\ :sub:`u`; Pr\ :sup:`3+`:
3H\ :sub:`g`; Nd\ :sup:`3+`: 4I\ :sub:`g`; ... Gd\ :sup:`3+`:
8S\ :sub:`u`;... Lu\ :sup:`3+`: 1S\ :sub:`g`, but for computational
convenience the ground states should be regarded as undefined, simply
[Xe] plus zero, one, two or more "f" electrons. For this reason, when
modeling Ln\ :sup:`3+` complexes, ignore the atomic configuration of the
Ln\ :sup:`3+` ions, instead pay attention only to the electronic state
of the rest of the system.  For most simple organics, such as `lanthanum
trisacetylacetonate <http://openmopac.net/PM7_accuracy/data_molecules/La(III)O8%20(AQACAL)_Jmol.html>`__,
CSD entry AQACAL, this will be the Singlet; almost all others will be
Doublets.  For these sets, explicit keywords are not needed - they will
be automatically recognized by default.  Only for exotic systems, such
as Triplet or excited states would keywords defining the state be
needed.

 

 

 
