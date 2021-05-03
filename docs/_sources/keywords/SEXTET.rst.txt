.. _SEXTET:

``SEXTET``
==========

RHF interpretation: The desired spin-state is a sextet: the state with
component of spin M\ :sub:`S` = 5/2 and spin S = 5/2. In order to define
this type of calculation other keywords *must* also be used. For a
'simple' sextet calculation, use ``C.I.=5``.

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 5/2 are selected.
These microstates are then used in the construction of states. Because
of the way in which the microstates were chosen, only states of spin
equal to or greater than 5/2 can be constructed. From this set, only a
sextet state can be selected; all other states will be ignored. If
``ROOT=n`` is present, then the *n*'th sextet state will be selected;
otherwise, the first sextet state will be chosen.

If several sextets are to be calculated, say the second or third, then
``C.I.(n1,n2)`` should be used.

See also ```MS=n`` <ms.html>`__, ```SINGLET`` <singlet.html>`__,
```DOUBLET`` <doublet.html>`__, ```TRIPLET`` <triplet.html>`__,
```QUARTET`` <quartet.html>`__, ```QUINTET`` <quintet.html>`__,
```SEPTET`` <septet.html>`__, ```OCTET`` <octet.html>`__, and
```NONET`` <nonet.html>`__. UHF interpretation: The system will have
five more alpha electrons than beta electrons.
