.. _CdotIdot:

``C.I.``
========

``C.I.=(n,m)``

In addition to specifying the number of M.O.s in the active space, the
number of electrons can also be defined. In ``C.I.=(n,m)``, *n* is the
number of M.O.s in the active space, and *m* is the number of doubly
filled (that is, not empty or partially filled) levels to be used (see
Table). If ``OPEN(n1,n2)`` is present, then the number of electrons may
be increased.

| 

.. raw:: html

   <div align="CENTER">

Table: Use of ``C.I.=(n,m)``

Keywords

.. raw:: html

   </div>

No. of M.O.s

| No. of
| Electrons\*

````

C.I.=2

2

2 (1)

````

C.I.=(2,1)

2

2 (3)

````

C.I.=(3,1)

3

2 (3)

````

C.I.=(3,2)

3

4 (5)

| 
| \* Odd electron systems given in parentheses.
