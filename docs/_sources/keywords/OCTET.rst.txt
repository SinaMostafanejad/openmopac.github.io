.. _OCTET:

``OCTET``
=========

RHF interpretation: The desired spin-state is an octet: the state with
component of spin M\ *S = 7/2 and spin S = 7/2. In order to define this
type of calculation other keywords must also be used. For a 'simple'
octet calculation, use ``C.I.=7``. When the configuration interaction
calculation is done, all microstates having a component of spin, M\ S,
equal to 7/2 are selected. These microstates are then used in the
construction of states. Because of the way in which the microstates were
chosen, only states of spin equal to, or greater than 7/2, can be
constructed. From this set, only an octet state can be selected, all
other states will be ignored. If ``ROOT=n`` is present, then the n'th
octet state will be selected: otherwise the first octet state will be
chosen. If several octets are to be calculated, say the second or third,
then ``C.I.(n1,n2)`` should be used.*

See also ```MS=n`` <ms.html>`__, ```SINGLET`` <singlet.html>`__,
```DOUBLET`` <doublet.html>`__, ```TRIPLET`` <triplet.html>`__,
```QUARTET`` <quartet.html>`__, ```QUINTET`` <quintet.html>`__,
```SEXTET`` <sextet.html>`__, ```SEPTET`` <septet.html>`__, and
```NONET`` <nonet.html>`__. UHF interpretation: The system will have
seven more alpha electrons than beta electrons.
