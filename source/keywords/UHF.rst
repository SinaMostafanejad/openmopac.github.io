.. _UHF:

UHF
===

Requests an unrestricted Hartree-Fock Hamiltonian that allows the two electrons of opposite spin in an electron pair to have different spatial orbitals.

For supported features, this is the default behavior for odd-electron systems (i.e. radicals).
A UHF calculation can be requested for even-electron systems, but it should produce the same results as a spin-restricted calculation (:ref:`RHF`).

UHF calculations often contain unphysical spin contamination.
In the absence of external magnetic fields,
a many-electron wavefunction should be an eigenstate of the z-axis spin operator, :math:`S_z`, and the total spin operator, :math:`S^2`.
The additional orbital relaxations allowed by an RHF calculation breaks the overall spin symmetry,
which enables the wavefunction to lower its total energy by deviating from an eigenstate of :math:`S^2`.
