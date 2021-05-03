.. _RE-LOCAL:

``RE-LOCAL``
------------

The LMOs used by ```MOZYME`` <mozyme.html>`__ in the SCF are not fully
localized. At the start they are, but as the SCF proceeds, they become
increasingly delocalized. At the end of a calculation, the LMOs may be 5
or 10 percent less than fully localized. To generate localized M.O.s of
the type that MOPAC makes, ``RE-LOCAL`` should be used.

``RE-LOCAL`` will give results slightly different to those from MOPAC
because of two reasons:

(1) Sets of LMOs that could be resolved into banana bonds or rabbit ears
are not resolved.  This means that such LMOs are ill-defined, however
this would never be significant in reactions.

(2) The unitary rotation of the occupied set will not allow atoms to be
created.  So if one LMO has a specific atom that is not present in
another LMO, then rotation of the two LMOs will result in the loss of
wavefunction in the second LMO.  This is also never important but in
this case because the loss only occurs in the tails of the LMOs.

 

 

 

 
