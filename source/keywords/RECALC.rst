.. _RECALC:

``RECALC``
==========

``RECALC=n`` calculates the Hessian every *n* steps in the EF
optimization. For small *n* this is costly but is also very effective in
terms of convergence. ``RECALC=10`` and ``DMAX=0.10`` can be useful for
difficult cases. In extreme cases ``RECALC=1`` and ``DMAX=0.05`` will
always find a stationary point, if it exists.
