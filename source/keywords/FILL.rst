.. _FILL:

``FILL=n``
==========

The *n*'th M.O. in an RHF calculation is constrained to be filled. It
has no effect on a UHF calculation. After the first iteration (NOTE:  
not after the first SCF calculation, but after the first iteration
within the first SCF calculation) the *n*'th M.O. is stored, and, if
occupied, no further action is taken at that time. If unoccupied, then
the HOMO and the *n*'th M.O.s are swapped around, so that the *n*'th
M.O. is now filled. In all subsequent iterations the M.O. nearest in
character to the stored M.O. is forced to be filled, and the stored M.O.
replaced by that M.O. This is necessitated by the fact that in a
reaction a particular M.O. may change its character considerably. A
useful procedure is to run ``1SCF`` and ``DENOUT`` first, in order to
identify the M.O.s. The complete job is then run with ``OLDENS`` and
``FILL=nn``, so that the eigenvectors at the first iteration are fully
known. As ``FILL`` is known to give difficulty at times, consider using
using ``C.I.=n`` and ``ROOT=m`` instead.

| 
