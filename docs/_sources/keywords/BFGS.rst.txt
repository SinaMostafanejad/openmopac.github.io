.. _BFGS:

``BFGS``
========

 

When ``BFGS`` is present, the the
Broyden-Fletcher-Goldfarb-Shanno [\ `19 <references.html#bfgs1>`__,\ `20 <references.html#bfgs2>`__,\ `21 <references.html#bfgs3>`__,\ `22 <references.html#bfgs4>`__]
procedure is used for geometry optimization. This is now an almost
obsolete optimizer because other more modern methods are more
efficient.  For small systems, up to about 30 atoms or 100 variables the
default ``EF`` method is faster, and for larger systems the L-BFGS
method - see keyword ```LBFGS`` <lbfgs.html>`__ is both faster and uses
a much smaller memory.

 

Use ``BFGS`` for testing ideas on geometry optimization or for the very
rare case where the default optimizers are not wanted.
