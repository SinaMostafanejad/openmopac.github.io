.. _CdotIdot:

C.I.
====

Defines an active space for multi-electron configuration interaction (MECI) calculations from orbitals near the chemical potential.
By default, this keyword defines a complete active space, but the active space can be further restricted to specific classes of excitations
with the keywords :ref:`CIS`, :ref:`CISD`, and :ref:`CISDT`.

**SYNTAX:** ``C.I.=n``

Activate the :math:`\lceil n/2 \rceil` orbitals at or below the chemical potential and the :math:`\lfloor n/2 \rfloor` orbitals above the chemical potential.

**SYNTAX:** ``C.I.=(n,m)``

Activate the :math:`n` orbitals closest to the chemical potential containing :math:`m` electron pairs.
This accounting ignores the unpaired electron in systems with an odd number of electrons.

MOPAC constructs and diagonalizes the active-space Hamiltonian as a dense matrix,
which becomes prohibitive in cost around ``C.I.=8`` if the active space is not restricted in size with other keywords.

.. table:: Number of configurations in MECI active spaces

  =========== ============== =================== ================== ============ =================== ================== ============
  Keyword                    Even number of electrons                            Odd number of electrons
  -------------------------- --------------------------------------------------- ---------------------------------------------------
  1 variable  2 variables    # of :math:`\alpha` # of :math:`\beta` # of configs # of :math:`\alpha` # of :math:`\beta` # of configs
  =========== ============== =================== ================== ============ =================== ================== ============
  ``C.I.=1``  ``C.I.=(1,1)`` 1                   1                  1            1                   0                  1
  ``C.I.=2``  ``C.I.=(2,1)`` 1                   1                  4            1                   0                  2
  ``C.I.=3``  ``C.I.=(3,2)`` 2                   2                  9            2                   1                  9
  ``C.I.=4``  ``C.I.=(4,2)`` 2                   2                  36           2                   1                  24
  ``C.I.=5``  ``C.I.=(5,3)`` 3                   3                  100          3                   2                  100
  ``C.I.=6``  ``C.I.=(6,3)`` 3                   3                  400          3                   2                  300
  ``C.I.=7``  ``C.I.=(7,4)`` 4                   4                  1225         4                   3                  1225
  ``C.I.=8``  ``C.I.=(8,4)`` 4                   4                  4900         4                   3                  3920
  =========== ============== =================== ================== ============ =================== ================== ============

.. note::
  :ref:`INDO` calculations use this keyword to specify the active orbitals for single-electron excitations,
  either from a Hatree-Fock reference state (:ref:`CIS` or :ref:`CISD`) or from a complete active space (:ref:`MRCI`).
  By default, all orbitals are active for this purpose.
