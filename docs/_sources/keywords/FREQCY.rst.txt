.. _FREQCY:

``FREQCY``
==========

Print out the symmetrized Hessian matrix in a ``FORCE`` calculation.

Symmetry is used to accelerate the construction of the Hessian matrix,
and also to symmetrize the Hessian, once it is constructed.  The effect
of symmetrization is to make the resulting eigenvectors (normal
coordinates) irreducible representations of the associated point group.
If this is not done, then there is the potential for the normal
coordinates to be unrecognizable as irreducible representations.

To turn off the use of symmetry, add ``NOSYM.``
