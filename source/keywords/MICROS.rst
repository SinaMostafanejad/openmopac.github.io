.. _MICROS:

MICROS
======

Restricts the active space of configuration interaction calculations to a list of microstates specified in the input file after the geometry and symmetry data.

**SYNTAX:** ``MICROS=n``

The microstate list contains :math:`n` entries.

The list is preceeded by a line containing ``MICROS`` and is separated from the geometry and symmetry data by a blank line.
The remaining :math:`n` lines each contain the specification of one microstate as a string consisting of ``0``'s and ``1``'s.
For :math:`m` active orbitals (specified by ``C.I.=m``, ``C.I.=(m,*)``, or ``OPEN(*,m)``),
each microstate defines the occupation of alpha and beta orbitals with a list of :math:`2m` occupations,
where ``0`` represents unoccupied and ``1`` represents occupied.
The ordering of active orbitals is consistent with MOPAC's output, with all active alpha orbitals ordered by increasing energy
followed by all active beta orbitals ordered by increasing energy.

A simple example of the ``MICROS`` keyword is
::

  C.I.=4 MS=1 MICROS=4
  a polarized carbon atom with a full alpha 2p shell

  C 0.0 0.0 0.0

  MICROS
  01111000
  01110100
  01110010
  01110001

All microstates must contain the same total number of electrons for MOPAC to produce sensible results.
They should also contain the same numbers of alpha and beta electrons, but this isn't strictly necessary.
Differing numbers of alpha and beta electrons correspond to different spin sectors of configuration space that are
not coupled by the many-electron Hamiltonian.

For a configuration interaction calculation to have well-defined spin states,
the list of microstates must be closed under the application of the spin operator, :math:`S^2`.
For example, the microstate ``0110`` should be joined by ``1001`` so that the two states can be combined into well-defined singlet and triplet states.

For a configuration interaction calculation to have well-defined symmetry states,
the list of microstates must be closed under the application of symmetry operators.
For example, the microstate ``100000`` of an atomic p-shell active space should be
joined by ``010000`` and ``001000``.
