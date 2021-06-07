.. _BAR:

BAR
===

**no value**

**1 real value**

real value

1 value:

1. The maximum fraction

**SYNTAX** : ``BAR=x``

===== ==== ===============================================================
``BAR=x``
--------------------------------------------------------------------------
name  type description
===== ==== ===============================================================
``x`` real maximum fractional geometric change per iteration in ``SADDLE``
===== ==== ===============================================================


In the ``SADDLE`` calculation [`18 <references.html#saddle>`__], the
distance between the two geometries is steadily reduced until the
transition state is located. Sometimes, however, the user may want to
alter the maximum rate at which the distance between the two geometries
reduces. BAR is a ratio, normally 0.01, or 1 percent. This represents a
maximum rate of reduction of the bar of 1 percent per step. Alternative
values that might be considered are ``BAR=0.005`` or ``BAR=0.001``,
although other values may be used. See also ``SADDLE``.

If CPU time is not a major consideration, use ``BAR=0.001``.
