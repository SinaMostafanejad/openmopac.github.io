.. _OPEN:

OPEN
====

Defines the distribution of electrons over partially occupied orbitals for open-shell Hartree-Fock calculations.

**SYNTAX:** ``OPEN(m,n)``

Distribute :math:`m` electrons uniformly over :math:`n` orbitals.

In an open-shell :ref:`RHF` calculation, the total number of electrons minus :math:`m` must be an even number
so that they can doubly occupy the lowest-energy orbitals.
The remaining :math:`m` electrons are uniformly spread over the :math:`n` lowest-energy unoccupied orbitals
with an occupation of :math:`m/n` per orbital.
These fractional orbital occupations represent a statistical superposition over alpha and beta spins,
with an independent :math:`m/(2n)` probability of the orbital containing an alpha and beta electron.
For valid occupation probabilities, :math:`m \le 2n` must be satisfied.

The ``OPEN`` keyword in an ``RHF`` calculation also expands the set of active orbitals to include the partially occupied orbitals.
The active space can be further expanded using the :ref:`C.I.` keyword, but the new active space must contain all partially occupied orbitals
or MOPAC will report an error.

In a :ref:`UHF` calculation, the total number of alpha minus :math:`m` fully occupy the lowest-energy alpha orbitals.
The remaining :math:`m` alpha electrons are uniformly spread over the :math:`n` lowest-energy unoccupied alpha orbitals with an occupation over :math:`m/n` per orbital.
For valid occupation probabilities, :math:`m \le n` must be satisfied.
Fractional occupations can also be applied to minority-spin electrons by using negative values of :ref:`MS` (alpha becomes the minority spin type).
Unlike in ``RHF`` calculations, MOPAC is unable to correct the Fock exchange penalties in ``UHF`` calculations with fractional occupations,
and their potential energy surfaces can only be directly compared to other ``UHF`` calculations with the same ``OPEN`` settings.

The primary uses of the ``OPEN`` keyword are to approximate spin states in open-shell ``RHF`` calculations
and to mimic the dynamic Jahn-Teller effect in ``UHF`` calculations.
Jahn-Teller distortions open energy gaps within a set of degenerate orbitals that are partially occupied,
inducing a subset of fully-occupied, lower-energy orbitals and a subset of unoccupied, higher-energy orbitals.
By spreading electrons uniformly over these degenerate orbitals, the Jahn-Teller distortion can be suppressed.

For the use of ``OPEN`` to be physically meaningful in a ground-state calculation,
the fractionally occupied orbitals should maintain an orbital energy degeneracy.
Otherwise, with fractional occupations over orbitals of different energies,
the ground-state energy could be further lowered by shifting occupations towards the lower-energy orbitals.
