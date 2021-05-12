.. _CYCLES:

``CYCLES``
==========

When ``CYCLES=n`` is specified, a maximum of *n* distinct geometry
cycles are allowed. After *n* cycles, the calculation is stopped in the
same manner as when the allowed time is exceeded. Geometry cycles are
(A) cycles of optimization in ``EF, SIGMA, NLLSQ``, and ``BFGS``, (B)
steps in a ``FORCE`` calculation, and (C) points calculated in an
``IRC`` or ``DRC`` calculation.

``CYCLES`` is intended to be an alternative to the ``T=n.nn`` keyword,
when platforms of different speeds are being used, particularly in
porting. See also ``BIGCYCLES``.
