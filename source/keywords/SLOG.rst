.. _SLOG:

``SLOG``
========

The line-search mechanism in the `L-BFGS <lbfgs.html>`__ geometry
optimization is replaced with a constant step size. This prevents large
steps that could waste time or even cause a failure to achieve an SCF.
If ``SLOG`` is used, changes individual coordinate parameters are
limited to 0.20 Å, otherwise if ``SLOG=n.nn`` is used, the limit is
*n*.\ *nn* Å.
