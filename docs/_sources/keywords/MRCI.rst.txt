.. _MRCI:

MRCI
====

Requests an active space of few-electron excitations from a complete active space (i.e. Multi-Reference Configuration Interaction) for an :ref:`INDO` calculation.

The default MRCI active space is single-electron excitations from a complete active space spanning the HOMO and LUMO orbitals.
The default single-electron excitations corresponds to using the :ref:`CIS` keyword,
and double-electron excitations can be requested using the :ref:`CISD` keyword.
The complete active space can be adjusted using the :ref:`CdotAdotSdot` keyword,
the number of single-electron excitations can be adjusted using the :ref:`CdotIdot` keyword,
and the number of single-electron excitations can be adjusted using the :ref:`CdotIdotDdot` keyword.
