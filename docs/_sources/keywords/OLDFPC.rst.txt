.. _OLDFPC:

``OLDFPC``
==========

By default, MOPAC uses the CODATA fundamental physical constants. This
means that the results of MOPAC 6 and earlier MOPAC calculations cannot
be duplicated. When ``OLDFPC`` is specified, the fundamental physical
constants used in earlier MOPACs is used. This allows these earlier
calculations to be duplicated using the current MOPAC.

Users are advised to not use ``OLDFPC`` except when comparison or
continuity with earlier MOPACs is necessary, as all future MOPACs will
use the new CODATA constants.
