.. _OLDGEO:

``OLDGEO``
==========

If multiple geometries are to be run, and the final geometry from one
calculation is to be used to start the next calculation, ``OLDGEO``
should be specified. Example: If MNDO, AM1, and PM3 calculation, were to
be done on one system, for which only a rough geometry was available,
then after the MNDO calculation, the AM1 calculation could be done using
the optimized MNDO geometry as the starting geometry, by specifying
``OLDGEO``. After the AM1 calculation was done, then a PM3 calculation
could also be done, starting with the old AM1 geometry, by again
specifying ``OLDGEO``.

When an ``OLDGEO`` calculation is started, none of the keywords from the
previous calculation are assumed to be present.  Thus, if the first
calculation had keywords ``PM3 ROOT=4 CIS C.I.=4``, none of these
keywords would be used by the ``OLDGEO`` calculation, unless they were
explicitly present in the ``OLDGEO`` keyword line.
