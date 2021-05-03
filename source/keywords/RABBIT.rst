.. _RABBIT:

``RABBIT``
----------

In a ```LOCALIZE`` <localize.html>`__ calculation, localized M.O.'s
(LMO's) on an atom that has two or three lone pairs are split into one
LMO that is mainly sigma and one or two LMO's that are mainly pi.  When
``RABBIT`` is present, a ``LOCAL`` calculation will be done, and these
LMO's will be replaced with hybrid LMO's that have equal amounts of
sigma character in each M.O. 

 The resulting LMO's are commonly referred to as rabbit-ears because of
their shape, although they really look more like ear-muffs than
rabbit-ears.

All three sets of M.O.'s, canonical, localized, and localized with
``RABBIT``, are equivalent, in that the sets are related to each other
by unitary transforms. Use whichever set best first the current needs.

See also ``LOCAL`` and ``BANANA``

 
