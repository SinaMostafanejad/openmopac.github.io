.. _CISD:

``CISD``
========

In configuration interaction calculations, the ground state and all
microstates resulting from single and double electron excitations are
used if ``CISD`` is specified. (Read ``CISD`` as Configuration
Interaction Singles and Doubles.)

The number of states considered in a CISD C.I. involving *n*
doubly-occupied M.O.s and *m* empty M.O.s is:

No. of States = 1 + 2.n.m  + (n.m):sup:`2` + (n(n-1).m(m-1))/2

This represents:

| Ground state
| + (one α electron excited + one β electron excited)
| + (one α electron and one β electron excited)
| + (two α electrons excited + two β electrons excited)

The first term represents the ground state, the second term represents
number of one-electron excitations, and the third and fourth terms
represent the number of two-electron excitations.
