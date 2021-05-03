.. _EPS:

``EPS=n.nn``
============

Sets the dielectric constant for the solvent to *n*.\ *nn*. Presence of
this keyword will cause the `COSMO <cosmo.html>`__ (Conductor-like
Screening Model) method [`30 <references.html#cosmo>`__] to be used to
approximate the effect of a solvent model surrounding the molecule.
Solvents with low dielectric constant are not likely to work well in
this model. A `test <cosmo_validation.html>`__ is provided to allow
COSMO to be validated.

To alter the Van der Waals radius, use ``VDW``.

See also ``RSOLV, DISEX, COSWRT, and NSPA``.
