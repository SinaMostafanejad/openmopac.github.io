.. _RHF:

RHF
===

Requests a restricted Hartree-Fock (RHF) Hamiltonian that forces the two electrons of opposite spin in an electron pair to have the same spatial orbital.

This is the default behavior for even-electron systems and for MOPAC features that do not support unrestricted orbitals (e.g. :ref:`MECI` calculations).
For supported features, unrestricted orbitals (:ref:`UHF`) are the default behavior for odd-electron systems (i.e. radicals, open shells).

RHF is slower than UHF for the geometry optimization of radicals but avoids the problem of spin contamination.

Open-shell RHF calculations in MOPAC use Dewar's approach of statistically distributing electrons over :math:`\alpha` and :math:`\beta` spins :cite:p:`Dewar:1968`
rather than the conventional approach of minimizing the Hartree-Fock energy of a Slater determinant with constrained orbitals.
These two approaches produce similar but not strictly identical orbitals and total energies.
For the same set of orbitals, these two approaches would produce the same total energy.
