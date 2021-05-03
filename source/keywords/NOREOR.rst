.. _NOREOR:

``NOREOR``
==========

When the symmetry of a molecule is being worked out, the molecule is
orientated by default. If ``NOREOR`` is specified, the molecule will
*not* be reorientated. The main reason to not reorientate the molecule
is to allow a lower point-group to be used, and to allow the *x* and *y*
axes in Abelian groups to be defined by the user.

When ```GEO_REF`` <geo_ref.html>`__ is used, the default is that the
reference geometry is rotated and translated to give the maximum overlap
with the data-set geometry. This operation will be suppressed when
``NOREOR`` is present.

In a ```FORCE`` <force.html>`__ calculation, ``NOREOR`` will prevent the
molecules being reoriented to line up the moment of inertia axes with
the Cartesian axes.
