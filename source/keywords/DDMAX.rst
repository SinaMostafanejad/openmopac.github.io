.. _DDMAX:

``DDMAX=n.nn``
==============

The maximum value of the trust radius in ``EF`` and ``TS`` is set to
*n*.\ *nn*. The largest geometry change on any cycle is ``DDMAX``. Use
this keyword to limit the rate of change of the geometry. If ``DDMAX``
is *not* set, a default of 0.3 is used in ``TS``, and 0.5 is used in
``EF``.
