.. _DISP:

DISP
====

Prints individual post-SCF corrections to the heat of formation,
including hydrogen-bond and dispersion energies.

**SYNTAX:** ``DISP(cutoff)``

Additionally prints a list of individual hydrogen bonds with a binding energy larger
than the specified ``cutoff`` energy in units of kcal/mol.
For example, a reasonable cutoff for detecting standard hydrogen bonds is 1 kcal/mol, specified by ``DISP(1.0)``.
