.. _DEBUG:

``DEBUG``
=========

Certain keywords have specific output control meanings, such as
``FOCK``, ``VECTORS`` and ``DENSITY``. If they are used, only the final
arrays of the relevant type are printed. If ``DEBUG`` is supplied, then
all arrays are printed. This is useful in debugging the subroutine ITER.
``DEBUG`` can also increase the amount of output produced when certain
output keywords are used, e.g. ``COMPFG``.

When ``DEBUG`` is present, unrecognized keywords are noted, but the job
is not stopped.  There are many undocumented keywords that are useful in
testing MOPAC.
