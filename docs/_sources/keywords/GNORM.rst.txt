.. _GNORM:

``GNORM=n.nn``
==============

The geometry optimization termination criteria (see
`Criteria <Geometry_criteria.html>`__) in both gradient minimization and
energy minimization can be over-ridden by specifying a gradient norm
requirement. For example, ``GNORM=20`` would allow the geometry
optimization to exit as soon as the gradient norm dropped below 20.0
kcal/mol/Ångstrom, the default being 1.0.

For proteins and solids, i.e., large systems, ``GNORM=10`` should be
used.  Lower values might work, but there is an increased risk of the
heat of formation not decreasing, and all that happens is that CPU time
is wasted.

For small system high-precision work, ``GNORM=0.0`` is recommended.
Unless ``LET`` is also used, the ``GNORM`` will be set to the larger of
0.01 and the specified ``GNORM``. Results from ``GNORM=0.01`` are easily
good enough for all high-precision work.

N.b.: Do not confuse ``GNORM``, the keyword, with GNORM, the value of
the scalar of the calculated gradient. The keyword ``GNORM`` defines the
criterion for an optimized geometry,  GNORM is the value calculated
during a geometry optimization, and is printed in the output at the end
of each cycle.  When  GNORM, drops below the level set by
``GNORM=n.nn``, the geometry optimization will terminate.
