.. _SEPTET:

``SEPTET``
==========

RHF interpretation: The desired spin-state is a septet: the state with
component of spin M\ :sub:`S` = 3 and spin S = 3. In order to define
this type of calculation other keywords *must* also be used. For a
'simple' septet calculation, use ``C.I.=6``.

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 3 are selected. These
microstates are then used in the construction of states. Because of the
way in which the microstates were chosen, only states of spin equal to
or greater than 3 can be constructed. From this set, only a septet state
can be selected; all other states will be ignored. If ``ROOT=n`` is
present, then the *n*'th septet state will be selected; otherwise, the
first septet state will be chosen.

The septet states are the highest spin states normally calculable using
MOPAC in its unmodified form. If several septets are to be calculated,
say the second or third, then ``C.I.(n1,n2)`` should be used.

See also ```MS=n`` <ms.html>`__, ```SINGLET`` <singlet.html>`__,
```DOUBLET`` <doublet.html>`__, ```TRIPLET`` <triplet.html>`__,
```QUARTET`` <quartet.html>`__, ```QUINTET`` <quintet.html>`__,
```SEXTET`` <sextet.html>`__, ```OCTET`` <octet.html>`__, and
```NONET`` <nonet.html>`__. UHF interpretation: The system will have six
more alpha electrons than beta electrons.
