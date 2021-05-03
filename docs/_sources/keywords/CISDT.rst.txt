.. _CISDT:

``CISDT``
=========

In configuration interaction calculations, the ground state and all
microstates resulting from single, double, and triple electron
excitations are used if ``CISDT`` is specified. (Read ``CISDT`` as
Configuration Interaction Singles, Doubles, and Triples.)

The number of states considered in a CISDT C.I. involving *n*
doubly-occupied M.O.s and *m* empty M.O.s is:

No. of States = 1 + 2.\ *n.m*  + (*n.m*)\ :sup:`2` +
(*n*\ (*n*-1).*m*\ (*m*-1))/2 +
(*n*\ :sup:`2`\ (*n*-1).*m*\ :sup:`2`\ (*m*-1))/2 +
(*n*\ (*n*-1)(*n*-2).*m*\ (*m*-1)(*m*-2))/18

This represents:

| Ground state
| + (one α electron excited + one β electron excited)
| + (one α electron and one β electron excited)
| + (two α electrons excited + two β electrons excited)
| + (one α electron and two β electrons excited + two α electrons and
  one β electron excited)
| + (three α electrons excited + three β electrons excited)

The first term represents the ground state, the second term represents
number of one-electron excitations, the third and fourth terms represent
the number of two-electron excitations, and the fifth and sixth terms
represent the number of three-electron excitations.
