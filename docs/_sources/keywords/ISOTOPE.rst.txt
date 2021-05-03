.. _ISOTOPE:

``ISOTOPE``
===========

Generation of the `FORCE <force.html>`__ matrix is very time-consuming,
and in isotopic substitution studies several vibrational calculations
may be needed. To allow the frequencies to be calculated from the
(constant)   force matrix, ``ISOTOPE`` is used. When a ``FORCE``
calculation is completed, ``ISOTOPE`` will cause the force matrix to be
stored, regardless of whether or not any intervening restarts have been
made. To re-calculate the frequencies, etc., starting at the end of the
force matrix calculation, specify ``RESTART``.

The two keywords ``RESTART`` and ``ISOTOPE`` can be used together. For
example, if a normal ``FORCE`` calculation runs for a long time, the
user may want to divide it up into stages and save the final force
matrix. Once ``ISOTOPE`` has been used, it does not need to be used on
subsequent ``RESTART`` runs. ``ISOTOPE`` can also be used with ``FORCE``
to set up a ``RESTART`` file for an ``IRC=n`` calculation.
