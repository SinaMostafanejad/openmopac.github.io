.. _PM6-DH2:

``PM6-DH2``
===========

Use the PM6-DH2 procedure of: M. Korth, M. Pitonák, J. Rezác, and P.
Hobza, "A Transferable H-bonding Correction For Semiempirical
Quantum-Chemical Methods",  J. Chem. Theory Comp. 2010, 6, 344–352 and
J. Rezác, J. Fanfrlik, D. Salahub and P. Hobza, " Semiempirical Quantum
Chemical PM6 Method Augmented by Dispersion and H-Bonding Correction
Terms Reliably Describes Various Types of Noncovalent Complexes " J.
Chem. Theory Comp. 2009, 5, 1749-1760. See: 
`Abstract <pm6_dh2_abstract.html>`__.

The PM6-DH2 method was parameterized to reproduce interaction energies
for geometries obtained from high-level quantum mechanical calculations,
see `accuracy <PM6_dh2_accuracy.html>`__. While it is possible to use it
for geometry optimization, please be aware of the following limitation
and that the method should be used with extra care. Users are
recommended to optimize the geometry with the PM6 or other PM6-DXX
methods and calculate the final energy or interaction energy using
PM6-DH2.

**KNOWN LIMITATION OF PM6-DH2:** *  The gradients obtained by the
current implementation of the -H correction do not include the term
containing the derivative of atomic charges with change of the
coordinates. The structure obtained by minimization using this gradient
is not the exact minimum of PM6-DH2 energy. This error is negligible in
the case of weaker H-bonds, but in case of a strongly bound formic acid
dimer, the error is 0.30 kcal/mol. This error can be avoided by using*
```NOANCI`` <noanci.html>`__, *but then the calculations will then take
much longer.*

The PM6-DH2 procedure corrects binding errors in the PM6 method.  It can
be used with geometry optimization or with a single point
(```1SCF`` <one_scf.html>`__) calculation.  Normally, two or three
calculations would be needed to get the binding energy. 

To print the individual components of DH2, add\ ```DISP`` <disp.html>`__

| 
|  

 

 

 
