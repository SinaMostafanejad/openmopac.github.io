.. _CdotAdotSdot:

C.A.S.
======

Adjust the active orbitals that define a Complete Active Space (CAS) in an :ref:`INDO` calculation.

**SYNTAX:** ``C.A.S.=n``

Activate the :math:`\lceil n/2 \rceil` orbitals at or below the chemical potential and the :math:`\lfloor n/2 \rfloor` orbitals above the chemical potential.

**SYNTAX:** ``C.A.S.=(n,m)``

Activate the :math:`n` orbitals closest to the chemical potential containing :math:`m` electron pairs.
This accounting ignores the unpaired electron in systems with an odd number of electrons.

A CAS contains all spin-adapted configurations of electrons rearranged within the active orbitals.

By default, 2 orbitals are actived when :ref:`MRCI` is specified (equivalent to ``C.A.S.=2``).

If the ``C.A.S.`` keyword is combined with other keywords related to active spaces
(:ref:`MRCI`, :ref:`CIS`, :ref:`CISD`, :ref:`CdotIdot`, :ref:`CdotIdotDdot`),
the CAS is further expanded by applying single-electron or double-electron excitations to its configurations.

Note that the size of CAS grows exponentially with :math:`n`.
Only a small number of orbitals can be activated before the computational costs becomes prohibitive.
This is particularly true if the active space is further expanded by additional few-electron excitations.
