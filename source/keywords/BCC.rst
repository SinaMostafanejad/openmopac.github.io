.. _BCC:

``BCC``
=======

````

BCC is not used by MOPAC at all, but instead is used to inform programs
`MAKPOL <makpol.html>`__ and `BZ <Program_BZ.html>`__ about the nature
of the solid being studied.

````

BCC should be specified if all odd unit cells are omitted, e.g. unit
cells (0,0,1), (1,2,4), and (3,2,2) are excluded, but (0,0,0), (1,3,2),
and (2,2,2) are included. An example is provided by diamond where the
unit cell consists of two atoms.  ``BCC`` is used during the generation
of Large Unit Cells using program MAKPOL  and also used in *k*-space or
Brillouin zone work using program BZ.  This applies only to layer and
solid systems.
