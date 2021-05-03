.. _NOSWAP:

``NOSWAP``
==========

 

When ```GEO_REF`` <geo_ref.html>`__ is used, the reference geometry is
rotated and translated to give the maximum overlap with the data-set
geometry.  In some systems, a further increase in overlap can be
obtained by swapping pairs of atoms in the reference data-set.  An
example would be to swap around two hydrogen atoms attached to the same
atom, e.g., in a methylene or amine group.  This operation is done
automatically.  To prevent automatic swapping, add ``NOSWAP``.
