.. _DMAX:

``DMAX=n.nn``
=============

In the EF routine [`7 <references.html#ef-ts>`__], the starting value
for the trust radius is set to *n*.\ *nn*. After the first geometry
optimization cycle, ``DMAX`` is changed by ``EF``, and can increase by a
factor of 2.0 on every cycle. If ``DMAX`` is *not* set, the default of
0.20 is used. (Try to avoid using this keyword.)
