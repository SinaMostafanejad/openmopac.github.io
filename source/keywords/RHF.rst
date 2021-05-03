.. _RHF:

``RHF``
=======

The Restricted Hartree-Fock Hamiltonian is to be used.

This is the default for even-electron systems and for odd-electron
systems that use keywords such as ```MECI`` <meci.html>`__ that imply an
RHF calculation.  For odd electron (radical) systems, the
```UHF`` <uhf.html>`__ method is used by default, because geometry
optimization using UHF runs faster than when ``RHF`` is used. 

If RHF methods are to be used on odd electron systems, add keyword
``RHF``.

RHF methods are needed if configuration interaction is used, see
```MECI`` <meci.html>`__.
