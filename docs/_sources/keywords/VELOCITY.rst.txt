.. _VELOCITY:

``VELOCITY``
============

The user can supply the initial velocity vector to start a
`DRC <DRC_IRC_description_2.html>`__ calculation. For obvious reasons,
the input geometry should be in Cartesian coordinates. If internal
coordinates must be used, add ``GEO-OK``.

Put the velocity vector after the geometry as three data per line,
representing the *x*, *y*, and *z* components of velocity for each atom.
The units of velocity are centimeters per second.

If `KINETIC=n.n <kinetic.html>`__ is also specified, the velocity vector
will be scaled to equal the velocity corresponding to *n*.\ *n*
kcal/mol. This allows the user to define the direction of the velocity
vector; the magnitude is given by ``KINETIC=n.n``.
