.. _QUINTET:

``QUINTET``
===========

RHF interpretation: The desired spin-state is a quintet: that is, the
state with component of spin M\ :sub:`S` = 2 and spin S = 2. In order to
define this type of calculation other keywords *must* also be used. For
a 'simple' quintet calculation, use ``C.I.=4``.

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 2 are selected. These
microstates are then used in the construction of states. Because of the
way in which the microstates were chosen, only states of spin equal to
or greater than 2 can be constructed. From this set, only a quintet
state can be selected; all other states will be ignored. If
``ROOT=n``\ is present, then the *n*'th quintet state will be selected;
otherwise, the first quintet state will be chosen.

See
also\ ``MS=n, SINGLET, DOUBLET, TRIPLET, QUARTET, SEXTET, SEPTET, OCTET,``
and ``NONET``.

UHF interpretation: The system will have four more alpha electrons than
beta electrons.
