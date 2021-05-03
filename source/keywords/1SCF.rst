.. _1SCF:

``1SCF``
========

When users want to examine the results of a single SCF calculation of a
geometry, ``1SCF`` should be used. ``1SCF`` can be used in conjunction
with ``RESTART``, in which case a single SCF calculation will be done,
and the results printed.

When ``1SCF`` is used on its own (that is, ``RESTART`` is not also
used), then derivatives will only be calculated if ``GRAD`` is also
specified.

````

1SCF is helpful in a learning situation. MOPAC normally performs many
SCF calculations, and in order to minimize output when following the
working of the SCF calculation, ``1SCF`` is very useful. See `An SCF
Calculation <SCF_calcn.html#1scf>`__ for a worked example of an SCF.  

When calculating the energies required to form electronic excited
states, to avoid geometry reorganization, ``1SCF`` must be used (see
`Frank Condon Considerations <meci_Franck_Condon.html#FC>`__). This
allows the vertical transition energies to be calculated (the
Franck-Condon transitions).
