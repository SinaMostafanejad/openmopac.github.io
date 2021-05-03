.. _MAXCI:

``MAXCI=n``
===========

Available for INDO-based CI calculations only. Include a maximum of *n*
electron configurations in the CI matrix. The default value is 2000; it
may be increased to ~7000 before running into memory constraints. If
more than *n* excitations are generated (see
```C.I.`` <ci=n.html>`__,\ ``C.A.S.,and C.I.D.``), the *n* lowest energy
excitations are included in the CI matrix.
