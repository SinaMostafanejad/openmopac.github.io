.. _BIGCYCLES:

``BIGCYCLES``
=============

When ``BIGCYCLES=n`` is specified, a maximum of *n* complete geometry
optimizations are allowed. After *n* optimizations, the calculation is
stopped in the same manner as when the allowed time is exceeded.

In a ```DRC`` <drc0.html>`__, ``BIGCYCLES=n`` will run until *n*
complete oscillations have occurred.   ``BIGCYCLES=1`` would allow a
single complete vibration to be generated. In simulated annealing or
heating, see ```DRC=n.nn`` <drc.html>`__, use ``BIGCYCLES=nnn`` as a
guide, in arbitrary units, of how long the run should last.

``BIGCYCLES`` is useful in comparing calculations using different
computers. Different machines run at different speeds, so calculations
based on time should not be used. Instead, by using ``BIGCYCLES``, a
specific number of cycles can be run, regardless of the machine speeds.

See also ``CYCLES`` and ```T=n.nn`` <t=n.html>`__
