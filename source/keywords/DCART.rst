.. _DCART:

``DCART``
=========

The Cartesian derivatives which are calculated in DCART for
variationally optimized systems are printed if the keyword ``DCART``\ is
present. The derivatives are in units of kcals/Ångstrom, and the
coordinates are displacements in *x*, *y*, and *z*.

Only the derivatives of the closed-shell SCF wavefunction are printed,
that is, any post-hoc corrections such as the effects of pressure,
dispersion, etc. are not included at this point. To include the post-hoc
corrections, add ```DERIV`` <deriv.html>`__.  For the equivalent
open-shell RHF gradients, see ```DERNVO`` <dernvo.html>`__.
