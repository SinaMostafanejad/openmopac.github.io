.. _PL:

``PL``
======

A tool for monitoring the behavior of SCF calculations is useful when
they take too long, or even fail altogether.  When keyword ``PL`` is
present, the energy of the system and the rate of change of the
electronic structure can be monitored iteration to iteration.  This
keyword is useful particularly when trying out various combinations of
convergers such as ``PULAY``, ``KING``, ``SHIFT``, and ``DAMP`` to find
the method that works best.

The rate of change in the electronic structure is given by the quantity
PLS in the output.  For example, in the line:

::

   ITERATION   7 PLS= 0.168E-01 0.395E-06 ENERGY      -34.585270 DELTAE   -2.2653063

the alpha wavefunction changed by 0.0168 between iteration 6 and
iteration 7. At the same time, the beta wavefunction changed by
0.000000395. The change in energy over these iterations is -2.265
kcal/mol.

If the calculation uses a restricted Hartree-Fock method, then the line
would look like this:

::

   ITERATION   7 PLS= 0.900E-02 0.000E+00 ENERGY       46.712559 DELTAE   -0.3203785

Now the change in total wavefunction between iteration 6 and 7 would be
0.009.  The second number, here 0.000E+00, is not used and should be
ignored.

The precise meaning of PLS depends on whether the calculation uses
```MOZYME`` <mozyme.html>`__ or the conventional, default, method.

Definition of PLS for conventional SCF calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In conventional methods, PLS is the largest change in any density matrix
element on two successive iterations in the SCF calculation. At
self-consistency, this change drops to zero.  For UHF calculations, both
the alpha and beta density matrices are used, therefore two numbers are
printed.  The total density matrix is used in RHF calculations, and
consequently the second number is not used.

Definition of PLS for MOZYME calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MOZYME calculations do not use a normal density matrix so the definition
used above cannot be used.  Instead, the largest Fock matrix element
connecting an occupied LMO with any virtual LMO is used.  This can be
written as:

PLS = \|<y\ :sup:`occ`\ \|F|y\ :sup:`vir`>\|

Although this definition is fundamentally different from that in
conventional work, in that data from only one iteration is used and the
units are now electron volts and not electrons, the meaning is the same
- at self-consistency all Fock matrix elements connecting occupied and
virtual LMOs are zero. Therefore, from a user's perspective, the
significance of PLS in both conventional and MOZYME calculations is the
same: it is a measure of how far the system is from self-consistency.

 

 
