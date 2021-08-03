.. _INDO:

INDO
====

Use the INDO/S (a.k.a. ZINDO/S) semiempirical model :cite:p:`Ridley:1973` instead of the default model, PM7 :cite:p:`Stewart:2013`.
This INDO-based model is fit for spectroscopic applications,
whereas all the other models available in MOPAC are based on the MNDO form :cite:p:`Dewar:1977` and fit for thermochemistry applications.
A wide range of excited-state properties have been implemented in MOPAC's INDO functionality :cite:p:`Gieseking:2020`,
and it shares some features and keywords with the Multi-Electron Configuration Interaction capabilities of MOPAC.
Ground-state properties (e.g. total energies, forces, vibrational frequencies, geometry optimization) are not available for INDO-based calculations.

The INDO-form Hamiltonian can be used with other parameters besides the default INDO/S model through the :ref:`EXTERNAL` keyword.

INDO-based calculations require the specification of an active space.
The INDO/S model was originally fit for use with an active space of single-electron excitations (:ref:`CIS`).
MOPAC's implementation also allows for the use of double-electron excitations (:ref:`CISD`) and more general multi-reference active spaces (:ref:`MRCI`)
to enable more accurate modeling of excited states with multi-electron excitation character.

INDO calculations in MOPAC are compatible with the COSMO solvation model :cite:p:`Klamt:1993`,
which enables the calculation of solvachromatic shifts.
INDO calculations in MOPAC are incompatible with unrestricted orbitals (:ref:`UHF`)
but compatible with restricted open-shell orbitals (:ref:`RHF`).
Hoowever, the SCF convergence of open-shell RHF calculations may be poor.

The number of active configurations can be adjusted using :ref:`MAXCI`, :ref:`C.I.`, :ref:`C.I.D.`, and :ref:`C.A.S.`.
The electron configurations used in INDO calculations are spin-adapted,
and higher-spin states can be selected with their appropriate keyword (:ref:`MS`, :ref:`DOUBLET`, :ref:`TRIPLET`, etc.).
