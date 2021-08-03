.. _PECI:

PECI
====

Restricts an active space to single-electron and paired double-electron excitations for configuration interaction calculations (i.e. Paired Electron Configuration Interaction).
Paired :math:`\alpha` and :math:`\beta` electrons are excited from a common doubly-occupied orbital to a common empty orbital.

This active space contains only singlet and triplet states.

.. table:: Number of configurations for :math:`n` doubly-occupied orbitals and :math:`m` empty orbitals

  ================================================== ===============
  excitation type                                    # of configs
  ================================================== ===============
  none (RHF ground state)                            :math:`1`
  1 :math:`\alpha` electron                          :math:`m n`
  1 :math:`\beta` electron                           :math:`m n`
  1 pair of :math:`\alpha` & :math:`\beta` electrons :math:`m n`
  ================================================== ===============
