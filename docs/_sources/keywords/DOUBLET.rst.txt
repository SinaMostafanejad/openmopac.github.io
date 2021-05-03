.. _DOUBLET:

``DOUBLET``
===========

When a configuration interaction calculation is done, all spin states
are calculated simultaneously, either for component of spin=0 or 1/2,
unless other keywords which define the spin are present. When only
doublet states are of interest, then ``DOUBLET`` can be specified, and
all other spin states, while calculated, are ignored in the choice of
root to be used.

Note that while almost every odd-electron system will have a doublet
ground state, ``DOUBLET`` should still be specified if the desired state
*must* be a doublet.

See also ```MS=n`` <ms.html>`__, ```SINGLET`` <singlet.html>`__,
```TRIPLET`` <triplet.html>`__, ```QUARTET`` <quartet.html>`__,
```QUINTET`` <quintet.html>`__, ```SEXTET`` <sextet.html>`__,
```SEPTET`` <septet.html>`__, ```OCTET`` <octet.html>`__, and
```NONET`` <nonet.html>`__.

````

DOUBLET has no meaning in a UHF calculation.
