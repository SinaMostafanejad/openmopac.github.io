.. _MS:

MS
==

The total electronic spin, which specifies the spin state of a system.
The default spin state is a singlet state for Hartree-Fock calculations and the lowest-energy integer-spin state for configuration interaction calculations.

**SYNTAX:** ``MS=x``

The total spin value :math:`x` must be an integer multiple of :math:`1/2`.
For example, ``MS=0`` corresponds to a singlet state, ``MS=0.5`` corresponds to a doublet state, and ``MS=1`` corresponds to a triplet state.
Many standard spin states also have their own keywords as convenient synonyms,
such as :ref:`SINGLET`, :ref:`DOUBLET`, and :ref:`TRIPLET`.
Negative :math:`x` values are also allowed and corresponds to an excess of beta electrons over alpha electrons.

The ``MS`` keyword targets a specific set of spin states within an MECI or :ref:`INDO` calculation.
MECI calculations are not spin-adapted, therefore all integer or half-integer spin states are calculated simultaneously.
:ref:`INDO` calculations are spin-adapted, and untargetted spin states are not calculated.

Non-zero spin multiplicity is directly compatible with UHF calculations unless the specified spin state is not physically accessible.
Spin-polarized UHF calculations are suitable for studying potential energy surfaces and performing geometry optimizations.

For open-shell RHF calculations, a compatible open shell must be defined using either the :ref:`CdotIdot` or :ref:`OPEN` keywords.
Electrons are statistically distributed over alpha and beta spins in the open-shell RHF Hamiltonian,
and the total energy is corrected by a post-SCF configuration interaction calculation to recover the correct spin state.
Spin-polarized RHF calculations are suitable for studying electronic excited states through configuration interaction calculations.

The simplest ways to specify a compatible active space for open-shell RHF calculations are either ``C.I.=2x`` or ``OPEN(2x,2x)``.

.. note::
  Most quantum chemistry software specifies spin states using spin multiplicity, which has a different offset and scaling than the spin value used in MOPAC.
  For example, a singlet state has a multiplicity of 1, a doublet state has a multiplicity of 2, and a triplet state has a multiplicity of 3.
