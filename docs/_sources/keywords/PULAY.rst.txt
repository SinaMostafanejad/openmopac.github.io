.. _PULAY:

``PULAY``
=========

The default converger in the SCF calculation is to be replaced by
Pulay's procedure [`48 <references.html#diis>`__] as soon as the density
matrix is sufficiently stable.   A considerable improvement in speed can
frequently be achieved by the use of ``PULAY``, particularly for excited
states. If a large number of SCF calculations are envisaged, a sample
calculation using ``1SCF`` and ``PULAY`` should be compared with using
``1SCF`` on its own, and if a saving in time results, then ``PULAY``
should be used in the full calculation. ``PULAY`` should be used with
care in that its use will prevent the combined package of convergers
(SHIFT, PULAY and the CAMP-KING convergers) from being used
automatically in the event that the system fails to go SCF in (ITRY-10)
iterations.

PULAY does *not* work with ```MOZYME`` <mozyme.html>`__

The combined set of convergers very seldom fails.
