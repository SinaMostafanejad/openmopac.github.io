.. _SINGLET:

``SINGLET``
===========

When a configuration interaction calculation is done, all spin states
are calculated simultaneously, either for component of spin = 0 (for
even electron systems) or 1/2 (for odd electron systems). When only
singlet states are of interest, then ``SINGLET`` can be specified, and
all other spin states, while calculated, are ignored in the choice of
root to be used.

Note that while almost every even-electron system will have a singlet
ground state, ``SINGLET`` should still be specified if the desired state
*must* be a singlet.

See also ```MS=n`` <ms.html>`__, ```DOUBLET`` <doublet.html>`__,
```TRIPLET`` <triplet.html>`__, ```QUARTET`` <quartet.html>`__,
```QUINTET`` <quintet.html>`__, ```SEXTET`` <sextet.html>`__,
```SEPTET`` <septet.html>`__, ```OCTET`` <octet.html>`__, and
```NONET`` <nonet.html>`__.

If the ``UHF`` method is used, then if ``SINGLET`` is present, the
system will be checked to verify that the number of electrons is even. 
If it is, then ``SINGLET`` will be ignored, otherwise the calculation
will be stopped, and an error message printed.

 
