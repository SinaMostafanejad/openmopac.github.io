.. _MODE:

``MODE``
========

``MODE`` is used in the EF routine. Normally the default ``MODE=1`` is
used to locate a transition state, but if this is incorrect, explicitly
define the vector to be followed by using ``MODE=n``. (``MODE`` is not a
recommended keyword). If you use the ``FORCE`` option when deciding
which mode to follow, set all isotopic masses to 1.0. The normal modes
from FORCE are normally mass-weighted: this can mislead. Alternatively,
use ``LARGE`` with ``FORCE``: this gives the force constants and vectors
in addition to the mass-weighted normal modes.
