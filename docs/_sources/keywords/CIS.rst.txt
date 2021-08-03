.. _CIS:

CIS
===

Restricts the active space to single-electron excitations for configuration interaction calculations (i.e. Configuration Interaction Singles).

The CIS active space is not useful for improving the Hartree-Fock approximation of ground-state properties
such as total energies, forces, vibrational frequencies, and relaxed geometries.
This phenomenon is explained by Koopmans' Theorem :cite:p:`Koopmans:1934`,
which shows that the many-electron Hamiltonian does not couple the Hartree-Fock ground state to singly-excited configurations.
An active space must include configurations with at least two-electron excitations to improve ground-state properties (e.g. :ref:`CISD`).

.. table:: Number of configurations for :math:`n` doubly-occupied orbitals and :math:`m` empty orbitals

  ============================== ===============
  excitation type                # of configs
  ============================== ===============
  none (RHF ground state)        :math:`1`
  1 :math:`\alpha` electron      :math:`m n`
  1 :math:`\beta` electron       :math:`m n`
  ============================== ===============
