.. _OPEN:

``OPEN(n1,n2)``
===============

**RHF description:** The M.O. occupancy during the SCF calculation can
be defined in terms of doubly occupied, empty, and fractionally occupied
M.O.s. By default, RHF SCF calculations are run using doubly occupied
M.O.s, with, at most, one singly occupied M.O.  For some systems, the
symmetry of the M.O.s can be preserved only if two or more M.O.s have
fractional occupancies. Such fractional occupancies can be defined using
``OPEN(n1,n2)``, where *n*\ :sub:`1` = number of electrons in the
open-shell manifold, and *n*\ :sub:`2` = number of open-shell M.O.s; 
The ratio of *n*\ :sub:`1` to *n*\ :sub:`2` is restricted to  *2 > 
n*\ :sub:`1`/*n*\ :sub:`2`  > 0.  Example: if ``OPEN(3,4)``\ were used
then the occupancy near the HOMO-LUMO gap would be ...2, 2, 2, 0.75,
0.75, 0.75, 0.75, 0, 0, 0, ...

The two π M.O.s in  molecular oxygen would not be degenerate if a
closed-shell SCF were run.  In order to maintain the degeneracy,
``OPEN(2,2)`` would need to be used.

Do *not* use ``OPEN(n1,n2)`` for ground-state systems *except* for high
symmetry systems with open shells, such as twisted (D:sub:`2\ d`)
ethylene or molecular oxygen O\ :sub:`2`, or if there is a very small
band-gap (such as in metal clusters).

Examples of ``OPEN(n1,n2)`` are given in the Table. ``OPEN(1,1)`` will
be assumed for odd-electron systems unless an ``OPEN`` keyword is used.
Errors introduced by use of fractional occupancy are automatically
corrected [`136 <references.html#136>`__] in a MECI calculation when
``OPEN(n1,n2)`` is used. See also ``C.I.=n``.

Notes:

-  OPEN(\ *n*\ :sub:`1`,\ *n*\ :sub:`2`) cannot be used instead of
   ``C.I.=n2``. ``OPEN(n1,n2)`` modifies the SCF calculation, but
   ``C.I.=n2`` does not modify the SCF calculation. Both keywords cause
   a C.I. calculation to be done.
-  Be careful to ensure that *n*\ :sub:`1` is odd if the system has an
   odd number of electrons, and even if the system has an even number of
   electrons.

**UHF description:** The M.O. occupancy during the SCF calculation can
be defined in terms of singly occupied, empty, and fractionally occupied
M.O.s. By default, UHF SCF calculations are run using singly occupied
M.O.s. When ``OPEN(n1,n2)`` is present, the highest *n\ 2* α molecular
orbitals are each given a population of *n*\ :sub:`1`/*n\ 2* electrons. 
To use ``OPEN(n1,n2)`` in a UHF calculation, ```UHF`` <uhf.html>`__ must
also be present.  Because fractional electrons are used, small errors in
energy, on the order of 1-2 kcal/mol, are introduced when
``OPEN(n1,n2)``\ is used.  These errors are *not* corrected by C.I.,
however they are small and should not affect the results significantly.

Because ``OPEN`` only applies to the α electrons, care must be exercised
in defining the number of α and β electrons.  For example, if the cation
of tetrahedral methane were to be calculated, the keywords needed would
be "``OPEN(2,3)MS=-0.5  UHF CHARGE=1" If MS=-0.5`` was not present, then
there would be four α and three β electrons, instead of the required
three α and four β electrons.

The main use of ``OPEN(n1,n2)`` in UHF calculations is to mimic the
dynamic Jahn-Teller effect in transition metal complexes.  Without
``OPEN(n1,n2)``\ an octahedral complex  system that could undergo
Jahn-Teller distortion would be distorted.  However, in many X-ray
structures, systems that should Jahn-Teller distort do not in fact
distort and instead retain high symmetry, typically O\ :sub:`h`.  This
high symmetry can be regarded as a dynamic J-T effect. Transition metal
complexes are, as their name suggests, complicated, and correctly
defining the various J-T states is also complicated.  The following set
of examples is provided to illustrate how to define keywords for various
octahedral systems.  These systems are assumed to have a three-fold
degenerate set of "d" M.O.s, with dominant contributions from the
*d*-orbitals *d\ xy*, *d\ yz*, *d\ xz*, that can be related to the
*t\ 2g* set of point group O\ :sub:`h`, and a two-fold degenerate set,
composed mainly of the other two *d*-orbitals; these are equivalent to
the * eg* set of point group O\ :sub:`h`.

| *d*\ :sup:`0`: No keyword needed - closed shell, i.e.,
  :sup:`1`\ A\ :sub:`1g`.\ *
  d*\ :sup:`1`: keywords: "``UHF OPEN(1,3)``"  One α *d* electron in a
  * t2g* set of M.O.s.  The resulting state is :sup:`2`\ T\ :sub:`2g`.
| *d*\ :sup:`2`: keywords: "``UHF OPEN(2,3) MS=1``"  Two α *d* electrons
  in a * t2g* set of M.O.s.  The resulting state is
  :sup:`3`\ T\ :sub:`1g`.
| *d*\ :sup:`3`: keywords: "``UHF MS=1.5``"  The state is
  :sup:`4`\ A\ :sub:`2g`.
| *d*\ :sup:`4`: keywords for low spin: ``"UHF OPEN(1,3)MS=-1``" 
  Because ``OPEN(n1,n2)``, applies only to α electrons, and because
  there are four electrons in a * t2g* set of M.O.s, the only way to
  have a fractional population of the α set of M.O.s is to have the β
  set filled, i.e., α\ :sup:`1`\ β\ :sup:`3` . By using "``MS=-1``" the
  number of  β electrons is defined as being two more than the number of
  α electrons  The resulting state is :sup:`3`\ T\ :sub:`1g`.\ *
  d*\ :sup:`4`: keywords for high spin: ``"UHF OPEN(1,2) MS=2``"  In
  high-spin *d*\ :sup:`4` complexes, there are three α electrons in the
  *t\ 2g*  set of M.O.s, and a single α electron in the two-fold
  degenerate *e\ g* M.O.  "``MS=2``" results in there being four more α
  than β electrons.  The resulting state is :sup:`5`\ E\ :sub:`g`.
| *d*\ :sup:`5`: keywords for low spin: ``"UHF OPEN(2,3) MS=-0.5``"  See
  *d*\ :sup:`4` low spin. This gives rise to a  :sup:`2`\ T\ :sub:`2g`
  state.\ *
  d*\ :sup:`5`: keywords for high spin: "``UHF MS=2.5``"  The state is
  :sup:`6`\ A\ :sub:`1g`.
| *d*\ :sup:`6`: No keyword needed - closed shell, i.e.,
  :sup:`1`\ A\ :sub:`1g`.\ *
  d*\ :sup:`6`: keywords for high spin\ ``: "UHF OPEN(1,3) MS=-2``"* *
  The resulting state is :sup:`5`\ T\ :sub:`2g` = A\ :sub:`2g` (from the
  β\ :sup:`2` of e\ :sub:`g` symmetry)*A\ :sub:`2g` (from the
  β\ :sup:`3` of t\ :sub:`2g` symmetry)*T\ :sub:`2g` (from the
  α\ :sup:`1` of t\ :sub:`2g` symmetry).
| *d*\ :sup:`7`: keywords for low spin: ``"UHF OPEN(1,2)``"  As with
  *d*\ :sup:`1`, the extra electron has, by default, α spin, and so the
  keyword "``MS=0.5``" is unnecessary.  The resulting state is
  :sup:`2`\ E\ :sub:`g`.\ *
  d*\ :sup:`7`: keywords for high spin: ``"UHF OPEN(1,2) MS=-1.5``" 
  With seven d-electrons and  ``MS=-1.5`` there are three more α than β
  electrons, i.e., α\ :sup:`2`\ β\ :sup:`5`.  The resulting state is 
  :sup:`4`\ T\ :sub:`1g`.
| *d*\ :sup:`8`: keywords: ``"UHF MS=1``"   The resulting state is 
  :sup:`3`\ A\ :sub:`2g`.
| *d*\ :sup:`9`: keywords: ``"UHF OPEN(1,2)``"   The resulting state is 
  :sup:`2`\ E\ :sub:`g`.
| *d*\ :sup:`10`: No keyword needed - closed shell, i.e.,
  :sup:`1`\ A\ :sub:`1g`.

A similar exercise could be done with the T\ :sub:`d` complexes. As this
is simple, albeit tedious, it is left as an exercise.

.. raw:: html

   <div align="center" style="float: left">

**Table:** Use of ``OPEN(n,m)``

.. raw:: html

   </div>

UHF Keywords

RHF Keywords

Example

Number of M.O.s

No. of Electrons

State

``MS=1``

````

OPEN(2,2)

Twisted Ethylene

2

2

:sup:`3`\ A\ :sub:`2`

``OPEN(1,2)``

````

OPEN(1,2)

O\ :sub:`2`\ :sup:`+`

2

1

:sup:`2`\ π\ :sub:`g`

````

MS=-0.5 OPEN(2,3)

````

OPEN(5,3)

CH\ :sub:`4`\ :sup:`+`

3

5

:sup:`2`\ T\ :sub:`2`

``MS=1.5``

``OPEN(3,3)``

[Cr:sup:`III`\ F\ :sub:`6`]\ :sup:`3-`

3

3

:sup:`4`\ A\ :sub:`2g`

``MS=2.5``

``OPEN(5,5)``

[Mn:sup:`II`\ (H2O):sub:`6`]\ :sup:`2+`

5

5

:sup:`6`\ A\ :sub:`1`

``MS=-0.5 OPEN(2,3)``

``OPEN(5,3)``

[Fe:sup:`III`\ (CN):sub:`6`]\ :sup:`3-`

3

5

:sup:`2`\ T\ :sub:`2g`

 

.. raw:: html

   <div align="left">

+--+
|  |
+--+

.. raw:: html

   </div>
