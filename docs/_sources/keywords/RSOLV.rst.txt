.. _RSOLV:

``RSOLV``
=========

Used by the  `COSMO <cosmo.html>`__  method to set the effective radius
of the solvent molecule to *n*.\ *nn*. The default value (1.3) is
appropriate for water.

This quantity should be altered for each solvent. One way to get
``RSOLV`` is to try several values for ``RSOLV``, and see which one
gives the best solvation energies when compared with experimental
results.

Dr Klamt suggests: For COSMO-RS, use a solvent radius which is
independent of the solvent, e.g. R_solv = R_hydrogen = 1.3 Angstrom.  Do
not use a large solvent radius for large solvents, because the solvent
is not probing the solute globally but locally. It is the local
curvature which is relevant here, and a general value of 1.3 Angstrom is
normally reasonable.
