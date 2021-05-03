.. _QUARTET:

``QUARTET``
===========

RHF interpretation: the desired spin-state is a quartet, i.e., the state
with component of spin M\ :sub:`S` = 3/2 and spin S = 3/2. In order to
define this type of calculation other keywords *must* also be used. For
a 'simple' quartet calculation, use ``C.I.=3``. If the quartet state
consists of three half-filled degenerate M.O.s, then ``OPEN(3,3)``
should be used.

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 3/2 are selected.
These microstates are then used in the construction of states. Because
of the way in which the microstates were chosen, only states of spin
equal to or greater than 3/2 can be constructed. From this set, only a
quartet state can be selected; all other states will be ignored. If
``ROOT=n`` is present, then the *n*'th quartet state will be selected;
otherwise, the first quartet state will be chosen. See also
```MS=n`` <ms.html>`__,
``SINGLET, DOUBLET, TRIPLET, QUINTET, SEXTET, SEPTET, OCTET,`` and
``NONET``. UHF interpretation: The system will have three more alpha
electrons than beta electrons.
