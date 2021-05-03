.. _DERIV:

``DERIV``
=========

Print some of the working in subroutine DERIV.  Quantities printed are:

| (A) The geometry using in the derivative calculation.
| (B) The gradients of the coordinates flagged for optimization. Units:
  kcal/mol/Angstrom and kcal/mol/radian (for angles and dihedrals) 
  These are the complete gradients, that is, the gradients of the SCF
  energy plus any post-SCF quantities such as dispersion and hydrogen
  bonding.
|   These are the values that will be passed back from subroutine DERIV.
| (C) The  values of the coordinates flagged for optimization. Units:
  Angstroms and radians.

Some of the working in subroutines within DERIV can be printed, see
```DCART`` <Dcart.html>`__ and ```DERNVO`` <dernvo.html>`__,
