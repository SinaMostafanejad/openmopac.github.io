.. _FORCE:

``FORCE and FORCETS``
=====================

A force-calculation is to be run. The Hessian, that is the matrix in
millidynes per Ångstrom) of second derivatives of the energy with
respect to displacements of all pairs of atoms in *x*, *y*, and *z*
directions, is calculated. On diagonalization this gives the force
constants for the molecule. The force matrix, weighted for isotopic
masses, is then used for calculating the vibrational frequencies. The
system can be characterized as a ground state or a transition state by
the presence of five (for a linear system) or six eigenvalues which are
very small (less than about 30 reciprocal centimeters). A transition
state is further characterized by one, and exactly one, negative force
constant.

By default, the geometry is rotated so that the principal moments of
inertia are oriented along the Cartesian axes, *x*, *y*, and *z*. If
this is not wanted, add keyword ```NOREOR`` <noreor.html>`__.

FORCETS
~~~~~~~

Calculating the Hessian for a large system takes a long time, and often
the only reason for running a ``FORCE`` calculation is to verify that
the system is a transition state.  To speed up this calculation,
``FORCETS`` is provided. The ``FORCETS`` calculation builds a Hessian
for the atoms involved in the transition state, that is, all atoms with
optimization flags of "1" or "2" (For the meaning of "2", see
```MINI`` <mini.html>`__).  All atoms used in building the Hessian
matrix must be at the start of the geometry.  This Hessian will be used
in generating vibrations for the transition state.  If the system is a
genuine transition state, then there will be one imaginary vibration,
indicated in the output as a "negative" vibration.  Its value will be
within a few percent of the value that would be obtained if a full
calculation were done. The imaginary vibration should involve the
atom(s) that move during the reaction. All other vibrations should be
positive, but their value is not useful, because they would involve
atoms other than those in the transition state.

Before a ``FORCE`` calculation is run, the gradients are calculated to
see if the geometry is at a stationary point. If it is not, then the
calculation will be stopped, to allow the user to take corrective
action.

Sometimes, the gradient norm at the start of a ``FORCE`` calculation
will be larger than at the end of the geometry optimization which was
used to generate the geometry for the force calculation. This is due to
the ``FORCE`` calculation using a different method, double-sided
derivatives, to calculate the gradients. In order to have the same GNORM
at the end of a geometry optimization as at the start of a ``FORCE``
calculation, use ``PRECISE`` in the geometry optimization. Gradients
calculated with ``PRECISE`` and with ``FORCE`` both use double-sided
derivatives.

At the end of a ``FORCE`` calculation, the force constants for the
coordinates supplied will be printed. If other force constants are
needed, then use ``ISOTOPE`` to save the Hessian. The connectivity can
then be changed, and the job restarted using ``RESTART``. Of course,
care must be taken to ensure that the atoms are in exactly the same
positions in both calculations.

Before a ``FORCE`` calculation is started, a check is made to ensure
that a stationary point is being used. This check involves calculating
the gradient norm (GNORM) and if it is significant, the calculation will
be stopped. See also ``LET and TRANS``. In a ``FORCE`` calculation,
``PRECISE`` will eliminate quartic contamination part of the
anharmonicity). This is normally not important, therefore ``PRECISE``
should not routinely be used. In a ``FORCE`` calculation, the SCF
criterion is automatically made more stringent; this is the main cause
of the SCF failing in a ``FORCE`` calculation.
