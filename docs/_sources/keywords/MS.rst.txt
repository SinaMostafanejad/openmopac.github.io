.. _MS:

``MS=n[.0,.5]``
===============

``MS=n`` can be used in defining the spin-state of a system.  Small
values of spin can also be defined using explicit keywords, such as
```SINGLET`` <singlet.html>`__, ```DOUBLET`` <doublet.html>`__,
```TRIPLET`` <triplet.html>`__, ```QUARTET`` <quartet.html>`__,
```QUINTET`` <quintet.html>`__,
```SEXTET`` <sextet.html>`__,\ ``SEPTET, OCTET,`` and ``NONET``. 
Explicit spin-states can be defined using ``MS=n``, for example
``MS=2.5`` is equivalent to ``SEXTET``.  Higher values of ``MS=n`` are
allowed, e.g. ``MS=20``.

RHF:  Use ```RHF`` <rhf.html>`__ when electronic phenomena, such as
excited state energies, transition dipoles, etc. are needed. As with the
explicit spin-state keywords, an open-shell must be defined.  See
```C.I.=``\ n <ci=n.html>`__, ```C.I.=(n,m)`` <ci=nm.html>`__, and
```OPEN(n1,n2)`` <open.html>`__.

UHF: Use ```UHF`` <uhf.html>`__ for chemistry, including geometry
optimization, transition states, reaction paths, etc. If the spin-state
is not possible, an error message will be printed.

 
