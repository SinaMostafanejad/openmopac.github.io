.. _NONET:

``NONET``
=========

RHF interpretation: The desired spin-state is a nonet: the state with
component of spin M\ :sub:`S` = 4 and spin S = 4. In order to define
this type of calculation other keywords *must* also be used. For a
'simple' nonet calculation, use ```C.I.=8``. <ci=n.html>`__

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 4 are selected. These
microstates are then used in the construction of states. Because of the
way in which the microstates were chosen, only states of spin equal to,
or greater than 4, can be constructed. From this set, only a nonet state
can be selected, all other states will be ignored. If ``ROOT=n`` is
present, then the *n*'th nonet state will be selected, otherwise the
first nonet state will be chosen.

The nonet states are the highest spin states normally calculable using
MOPAC in its unmodified form. If several nonets are to be calculated,
say the second or third, then ```C.I.(n1,n2)`` <ci=nm.html>`__ should be
used.

See also ```MS=n`` <ms.html>`__, ```SINGLET`` <singlet.html>`__,
```DOUBLET`` <doublet.html>`__, ```TRIPLET`` <triplet.html>`__,
```QUARTET`` <quartet.html>`__, ```QUINTET`` <quintet.html>`__,
```SEXTET`` <sextet.html>`__, ```SEPTET`` <septet.html>`__, and
```OCTET`` <octet.html>`__.

UHF interpretation: The system will have eight more alpha electrons than
beta electrons.
