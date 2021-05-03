.. _CIS:

``CIS``
=======

In configuration interaction calculations, the ground state and
microstates resulting from single electron excitations are used if
``CIS`` is specified. (Read ``CIS`` as Configuration Interaction
Singles.)

In a configuration interaction involving an active space in which *n*
levels are doubly occupied and *m* levels are empty, the number of
states considered in the C.I. would be (1 + *2.n.m*).  By `Koopmans'
theorem <references.html#koopmans>`__, the ground microstate does not
interact with any microstates resulting from one-electron excitation;
this means that the lowest state resulting from the C.I. consists of the
doubly occupied microstate only. It is included in the C.I. so that the
relative energies are relative to the ground state.  Because the C.I.
cannot affect the lowest root, a CIS ground-state calculation should not
be used in runs that affect the geometry, e.g. geometry optimization or
vibrational frequency calculations.
