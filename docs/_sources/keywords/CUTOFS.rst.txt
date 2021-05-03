.. _CUTOFS:

``CUTOFS=n.nn``
===============

```MOZYME`` <mozyme.html>`__ calculations run somewhat faster when some
overlap integrals are ignored.  By default, all overlap integrals
involving atoms separated by 7.0 Ångstroms or more are ignored. For
rough work, such as optimizing a structure that is far from a minimum,
if ``CUTOFS=n.nn`` is used, then overlap integrals involving atoms
separated by *n.nn* Ångstroms or more will be ignored.

A significant increase in speed and reduction in memory can be obtained
using ```CUTOFP=`` <cutofp.html>`__\ *n.nn*.

.

 
