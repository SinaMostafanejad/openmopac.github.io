.. _ESP:

``ESP``
=======

The electrostatic potential method used in MOPAC is severely
out-of-date.  The use of ESP is strongly discouraged.  A much faster and
easier method is to use keyword ```GRAPHF`` <graph.html>`__.

This is the ElectroStatic Potential calculation of K. M. Merz and B. H.
Besler [`31 <references.html#esp>`__]. ``ESP``\ calculates the
expectation values of the electrostatic potential of a molecule on a
uniform distribution of points. The resultant ESP surface is then fitted
to atom centered charges that best reproduce the distribution, in a
least squares sense. To print out the ESP map, use ``POTWRT``.
