.. _PRECISE:

``PRECISE``
===========

Non-LBFGS jobs:  The criteria for terminating all optimizations,
electronic and geometric, are to be increased by a factor, normally 100.
This can be used where more precise results are wanted. If the results
are going to be used in a ``FORCE`` calculation, where the geometry
needs to be known quite precisely, then ``PRECISE`` is recommended; for
small systems the extra cost in CPU time is minimal. ``PRECISE`` is not
recommended for experienced users; instead, ``GNORM=n.nn`` and
``SCFCRT=n.nn`` or ``RELSCF=n.nn`` are suggested. ``PRECISE`` should
only rarely be necessary in a ``FORCE`` calculation: all it does is
remove quartic contamination, which only affects the trivial modes
significantly, and is very expensive in CPU time. 

LBFGS jobs: In the ```LBFGS`` <lbfgs.html>`__ procedure, if  ``PRECISE``
is present then the number of cycles used in identifying the
lowest-energy system is increased from 30 to 60. 

See also ```LET`` <let.html>`__.
