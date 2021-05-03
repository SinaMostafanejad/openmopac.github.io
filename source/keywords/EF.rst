.. _EF:

``EF``
======

The Eigenvector Following routine [`7 <references.html#ef-ts>`__] is the
default geometry optimization method. For systems with more than 100
variables, the L-BFGS optimizer is the default.  To prevent the L-BFGS
optimizer being used, add keyword ``EF``.  That is, ``EF`` is provided
to allow explicit definition of the optimizer. Alternative geometry
optimizers are the
BFGS [\ `19 <references.html#bfgs1>`__,\ `20 <references.html#bfgs2>`__,\ `21 <references.html#bfgs3>`__,\ `22 <references.html#bfgs4>`__]
and the low-memory method, `L-BFGS <lbfgs.html>`__ . See also ``DDMAX``,
``DDMIN``, ``DMAX``, ``HESS``, ``IUPD``, ``LET``, ``MODE=``, ``NONR``,
``OMIN``, ``PRNT=``, ``RECALC``, ``RMAX``, ``RMIN``, ``RSCAL``.

The current ``EF``, while very reliable, is sometimes slow. To over-ride
some safety checks, specify ``LET``. This will sometimes make the job
run faster.
