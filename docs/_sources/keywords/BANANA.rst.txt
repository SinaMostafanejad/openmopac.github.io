.. _BANANA:

``BANANA``
==========

In a ```LOCALIZE`` <localize.html>`__ calculation, localized M.O.'s
(LMO's) in double and triple bonds and on atoms with two or three lone
pairs are split into one LMO that is mainly sigma and one or two LMO's
that are mainly pi.  For example, a triple bond would consist of a sigma
LMO and two pi LMO's.

When either ``RABBIT`` or ``BANANA`` is present in a ``LOCALIZE``
calculation, these LMO's would be replaced with hybrid LMO's that have
equal amounts of sigma character in each M.O.  In the case of double and
triple bonds, the resulting LMO's are commonly referred to as
banana-bonds because of their shape, although they look more like
éclairs than bananas.    In the case of two lone pairs on an atom, e.g.,
oxygen in a water molecule, the resulting LMO's are commonly referred to
as rabbit-ears because of their shape, although they look make like
ear-muffs than rabbit-ears. Other LMO's that cannot be mixed without
changing their localization properties, such as sigma LMO's in single
bonds and LMO's that represent a lone pair on an atom that has only one
lone pair, are not affected when ``RABBIT`` or ``BANANA`` is present.   

All three sets of M.O.'s, canonical, localized, and localized with
RABBIT or BANANA, are equivalent, in that the sets are related to each
other by unitary transforms. Use whichever set best first the current
needs.
