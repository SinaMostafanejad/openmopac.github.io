.. _PM7-TS:

``PM7-TS``
==========

Barrier heights can be calculated with increased accuracy by using
``PM7-TS``.  The PM7-TS method was parameterized to reproduce high-level
*ab-initio* barrier heights, given a ``PM7`` reaction geometry and a
transition state geometry.  (The reaction geometry is the geometry of
the system before ascending the activation barrier.)

For ``PM7-TS`` to work, the reaction geometry must be first calculated
using ``PM7``. The transition state must also be located and refined
using ``PM7``. To use ``PM7-TS``, run one calculation using the reaction
geometry, and one calculation using the transition state geometry, then
the barrier height is obtained by subtracting the heat of formation of
the reaction geometry system from that of the transition state geometry
system.
