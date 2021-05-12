.. _MERS:

``MERS``
========

``MERS=(n1) ``  or ``  MERS=(n1,n2)``    or   `` MERS=(n1,n2,n3)``

When keyword ``MERS``\ is present, information on a one-dimensional
polymer, a two-dimensional layer structure or a full three-dimensional
solid is written to a file for use by the band-structure program
`BZ <Program_BZ.html>`__. The integers *n*\ :sub:`1`, *n*\ :sub:`2`, and
*n*\ :sub:`3` define the number of fundamental unit cells in each
dimension in a cluster. For a polymer, only *n*\ :sub:`1`, is used, for
a layer structure ``n1`` and\ ``n2`` are used, and all three integers
are used for true 3-D solids.

Making a data-set "by hand" that would allow band-structures to be
generated is very difficult. Don't do it!  However, an option is
provided in the utility `MAKPOL <makpol.html>`__ that writes the MOPAC
data-set for band-structure work.  Use MAKPOL!

The definition of a 'mer' might be of interest. In a polymer or other
extended system, the fundamental repeating unit is the mer. For some
simple polymers, such as polyethylene, the mer can also be identified
with the monomer, in that both the mer and the monomer have the same
formula. In other polymers, the mer is not the same as the
monomer--condensation polymers are a good example, where the monomer
looses water on forming the polymer. In order to be general, therefore,
the unit of a polymer is not the monomer, but instead is the mer.

See also `BCC <bcc.html>`__
