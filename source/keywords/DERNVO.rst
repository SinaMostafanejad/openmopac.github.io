.. _DERNVO:

``DERNVO``
==========

Print some of the working in subroutine DERNVO. DERNVO works out
contributions to the gradients of the Cartesian  coordinates arising
from the open-shell RHF wavefunction.  Quantities printed are:

| \*  CARTESIAN DERIVATIVES DUE TO FROZEN CORE: This is RO-UHF
  equivalent to the material printed by ``DCART``.
| \*  RESIDUAL ERROR: If the Cartesian derivatives are calculated
  correctly, then the sum of the gradients in "x", "y", and "z" will be
  zero  The difference from zero is a measure of the error in the
  Cartesian derivatives due to the frozen core.

| \*  CARTESIAN DERIVATIVES DUE TO RELAXING CORE: This is the
  contribution to the Cartesian derivatives arising from the C.I. terms
  only.
| \*  RESIDUAL ERROR: If the Cartesian derivatives due to the relaxing
  core are calculated correctly, then the sum of the gradients in "x",
  "y", and "z" will be zero  The difference from zero is a measure of
  the error in the Cartesian derivatives due to the relaxing core.

| \*  CARTESIAN DERIVATIVES FROM ANALYTICAL C.I. CALCULATION The sum of
  the frozen plus relaxing contributions (the total derivative due to
  the wave-function)
| \*  RESIDUAL ERROR: The errors in the calculation of the sum of the
  frozen plus relaxing contributions to the total derivative due to the
  wave-function.  Ideally, these should be zero.
