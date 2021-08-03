.. _CISD:

CISD
====

Restricts the active space to single-electron and double-electron excitations for configuration interaction calculations (i.e. Configuration Interaction Singles and Doubles).

.. table:: Number of configurations for :math:`n` doubly-occupied orbitals and :math:`m` empty orbitals

  ==================================================== =========================
  excitation type                                      # of configs
  ==================================================== =========================
  none (RHF ground state)                              :math:`1`
  1 :math:`\alpha` electron                            :math:`m n`
  1 :math:`\beta` electron                             :math:`m n`
  1 :math:`\alpha` electron & 1 :math:`\beta` electron :math:`m^2 n^2`
  2 :math:`\alpha` electrons                           :math:`m (m-1) n (n-1)/4`
  2 :math:`\beta` electrons                            :math:`m (m-1) n (n-1)/4`
  ==================================================== =========================

.. note::
  :ref:`INDO` calculations can also use this keyword to request double-electron excitations in :ref:`MRCI` calculations.
