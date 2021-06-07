.. _1SCF:

1SCF
====

Requests that MOPAC exit after converging the first self-consistent field (SCF) cycle, just before initiating geometry relaxation.
This keyword is useful for calculating electronic properties of a specific molecular geometry,
including vertical excitation energies (i.e. Franck-Condon transitions).
By default, forces are not calculated if ``1SCF`` is specified, but they can be requested using the :ref:`GRADIENTS` keyword.
