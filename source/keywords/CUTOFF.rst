.. _CUTOFF:

``CUTOFF``
==========

| ```MOZYME`` <mozyme.html>`__ calculations run faster when some NDDO
  interactions are ignored.  By default, all NDDO interactions are
  included between atoms separated by 9.9 Ångstroms or less, and all
  polarization functions between atoms separated by 10 Ångstroms or
  less.  For rough work, such as optimizing a structure that is far from
  a minimum, if ``CUTOFF=n.nn`` is used, then only point charge
  interactions beyond *n.nn* Ångstroms are used.  A suitable value for
  *n.nn* is 6.0.  This will give a large increase in speed.
| Before using\ ``CUTOFF`` to increase speed, first try using
  ``CUTOFP.``

If ``CUTOFF=6`` is used, then ``GNORM=20`` is recommended.  Once the
geometry is optimized using ``GNORM=20``, the ``CUTOFF`` should be
removed, and ``GNORM`` reduced to, e.g., ``GNORM=10``.

The effect of ``CUTOFF`` on times and accuracy of prediction of geometry
can be investigated by examining the statistics for the optimization of
the positions of hydrogen atoms in Crambin, a small 642 atom, 46 residue
protein with formula
C\ :sub:`202`\ H\ :sub:`315`\ N\ :sub:`55`\ O\ :sub:`64`\ S\ :sub:`6`,
see Table I.  For a larger system, hexokinase, 2E2O, a medium-sized
protein of 5717 atoms and 299 residues,
C\ :sub:`1448`\ H\ :sub:`3073`\ N\ :sub:`375`\ O\ :sub:`810`\ S\ :sub:`11`,
results for a 1SCF calculation are shown in Table II.  Hexokinase
contains 375 molecules of water.

.. raw:: html

   <div align="center">

Table I: Crambin

.. raw:: html

   </div>

 

 

Table II: Hexokinase

Cutoff

Time (s)

Ratio

Distortion (Å)

Distortion (Å)

Energy (Kcal/mol)

| Relative
| energy

 

 

Cutoff

Time (s)

Ratio

Energy (Kcal/mol)

| Relative
| energy

Default

1328

1.00

49.5

0.0

-3342.2

0.0

 

 

Default

774

 

-45095.0

0.0

7.0

746

0.56

50.0

1.7

-3342.5

-0.3

12.0

796

-45095.0

0.0

6.0

889

0.76

49.6

1.3

-3342.1

+0.1

11.0

746

-45095.1

-0.1

5.0

599

0.45

46.3

8.8

-3334.5

+7.7

10.0

685

-45095.1

-0.1

4.0

348

0.26

51.7

5.0

-3315.8

+26.4

9.0

599

-45095.2

-0.2

3.0

119

0.09

34.9

26.7

-2952.1

+390.1

8.0

546

-45095.6

-0.4

no-opt

-

 

0.0

49.5

-2963.6

N/A

7.0

490

-45096.7

-1.7

6.0

343

-45093.3

+1.7

5.0

309

-50783.8

-5688.8

4.0

252

-44949.3

+145.7

For the rare occasions when finer control is needed, use ``CUTOF1`` and
``CUTOF2``.

``CUTOF1=n.nn``
---------------

In ``MOZYME`` calculations, `the cutoff distance for polarization
functions <distance_cutoffs.html>`__ is set by ``CUTOF1=n.nn``. Beyond
that distance, electrostatic interactions are considered only as point
charges. At distances less than that given by ``CUTOF1``, electrostatic
interactions are represented by a point-charge and three polarization
functions. Default: For systems of less than 30 atoms, ``CUTOF1`` is
1000 Ångstroms; for systems of 30 or more atoms, ``CUTOF1`` is 10
Ångstroms.

``CUTOF2=n.nn``
---------------

In ``MOZYME`` calculations, `the cutoff distance for two-electron two
center and one-electron two center integrals <distance_cutoffs.html>`__
is set by ``CUTOF2=n.nn``. Below that distance, the interaction between
two atoms is represented by the exact NDDO approximation. Above that
distance, one-electron integrals that depend on the overlap are ignored,
and two-electron integrals are simplified. Instead of using all 100
two-electron integrals between two heavy atoms, only seven are used.
These represent the terms <*ss*\ \|\ *ss*>, <*ss*\ \|\ *sx*>,
<*ss*\ \|\ *sy*>, <*ss*\ \|\ *sz*>, <*sx*\ \|\ *ss*>, <*sy*\ \|\ *ss*>,
and <*sz*\ \|\ *ss*>.  At still greater distances, beyond ``CUTOF1``,
only the <*ss*\ \|\ *ss*> term is used. Default: for systems of less
than 30 atoms, ``CUTOF2`` is 1000 Ångstroms; for systems of 30 or more
atoms, ``CUTOF2`` is 9.9 Ångstroms.

 
