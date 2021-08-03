.. _CISDT:

CISDT
=====

Restricts the active space to single-electron, double-electron, and triple-electron excitations
for configuration interaction calculations (i.e. Configuration Interaction Singles, Doubles, and Triples).

.. table:: Number of configurations for :math:`n` doubly-occupied orbitals and :math:`m` empty orbitals

  ===================================================== =================================
  excitation type                                       # of configs
  ===================================================== =================================
  none (RHF ground state)                               :math:`1`
  1 :math:`\alpha` electron                             :math:`m n`
  1 :math:`\beta` electron                              :math:`m n`
  1 :math:`\alpha` electron & 1 :math:`\beta` electron  :math:`m^2 n^2`
  2 :math:`\alpha` electrons                            :math:`m (m-1) n (n-1)/4`
  2 :math:`\beta` electrons                             :math:`m (m-1) n (n-1)/4`
  1 :math:`\alpha` electron & 2 :math:`\beta` electrons :math:`m^2 (m-1) n^2 (n-1)/4`
  2 :math:`\alpha` electrons & 1 :math:`\beta` electron :math:`m^2 (m-1) n^2 (n-1)/4`
  3 :math:`\alpha` electrons                            :math:`m(m-1)(m-2)n(n-1)(n-2)/36`
  3 :math:`\beta` electrons                             :math:`m(m-1)(m-2)n(n-1)(n-2)/36`
  ===================================================== =================================

