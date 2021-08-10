.. _SYMMETRY:

SYMMETRY
========

Impose direct coordinate constraints to reduce the number of independent geometric degrees of freedom and enforce symmetries.
Different sets of constraints are available for geometries specified in Z-matrix format and Cartesian coordinates.

The ``SYMMETRY`` keyword can reduce the cost of calculations involving derivatives because some derivatives
can be inferred from constraints instead of being computed explicitly.
Also, small numerical deviations in symmetry can be prevented by constraints,
which eliminates some error components in geometry optimization.

If the ``SYMMETRY`` keyword is specified, then a list of coordinate constraints must also be specified immediately after the geometry,
with one constraint per line of the input file.
A blank line is required to signify the end of the geometry specification and the beginning of the constraint list.
All but one constraint type is a space-separated list of integers with the syntax,

::

  reference type constrained1 constrained2 ... constrainedN

where ``reference`` is the index of the atom used to specify the constraint,
``type`` is the index of the constraint type,
and each ``constrained#`` is the index of an atom being constrained.
All atoms are indexed by their location in the geometry specification (i.e. 1 is the first atom, 2 is the second atom),
and up to 38 atoms can be constrained at a time.

Constraint type 19 for the Z-matrix format additionally requires a real-valued ``multiplier`` to be specified between ``type`` and ``constrained1``.
Similar to the behavior of the :ref:`SNAP` keyword, the ``multiplier`` is snapped to the closest irrational number of the form
:math:`\sqrt{a/b}` for integers :math:`a` and :math:`b` with :math:`b \in \{ 3, 6, 8, 12 \}` if they match to within approximately 3 decimal places.
For verification, the snapped value is printed in the output file.
Many constraint multipliers are of this form in typical high-symmetry geometries.

``SYMMETRY`` constraints have priority over the geometry information specified in the input file.
Any specified coordinate that violates a constraint is replaced by the value that satisfies the constraint.

It is possible to mix Z-matrix and Cartesian constraints in a single input file with a mixed geometry format.
A Z-matrix constraint must only contain atoms with coordinates specified in Z-matrix format,
and a Cartesian constraint must only contain atoms with coordinates specified in Cartesian format.

The following two tables specify all available ``SYMMETRY`` constraints,
where a :math:`c` subscript denotes a coordinate of a constrained atom
and an :math:`r` subscript denotes a coordinate of the reference atom.

.. table:: Z-matrix constraints (:math:`R` = bond length, :math:`\theta` = bond angle, :math:`\phi` = dihedral angle)

  ==== =================================== ==== =================================== ==== ============================================
  Type Formula                             Type Formula                             Type Formula
  ==== =================================== ==== =================================== ==== ============================================
  1    :math:`R_c = R_r`                   8    :math:`\phi_c = 180^\circ - \phi_r` 15   :math:`R_c = R_r/2`
  2    :math:`\theta_c = \theta_r`         9    :math:`\phi_c = 180^\circ + \phi_r` 16   :math:`\theta_c = \theta_r/2`
  3    :math:`\phi_c = \phi_r`             10   :math:`\phi_c = 240^\circ - \phi_r` 17   :math:`\theta_c = 180^\circ - \theta_r`
  4    :math:`\phi_c = 90^\circ - \phi_r`  11   :math:`\phi_c = 240^\circ + \phi_r` 18   not used
  5    :math:`\phi_c = 90^\circ + \phi_r`  12   :math:`\phi_c = 270^\circ - \phi_r` 19   :math:`R_c = \mathrm{multiplier} \times R_r`
  6    :math:`\phi_c = 120^\circ - \phi_r` 13   :math:`\phi_c = 270^\circ + \phi_r`
  7    :math:`\phi_c = 120^\circ + \phi_r` 14   :math:`\phi_c = - \phi_r`
  ==== =================================== ==== =================================== ==== ============================================

.. table:: Cartesian coordinate constraints (:math:`X`, :math:`Y`, :math:`Z`)

  ==== =================== ==== =================== ==== ===================
  Type Formula             Type Formula             Type Formula
  ==== =================== ==== =================== ==== ===================
  1    :math:`X_c = X_r`   7    :math:`X_c = Y_r`   13   :math:`X_c = Z_r`
  2    :math:`Y_c = Y_r`   8    :math:`Y_c = Z_r`   14   :math:`Y_c = X_r`
  3    :math:`Z_c = Z_r`   9    :math:`Z_c = X_r`   15   :math:`Z_c = Y_r`
  4    :math:`X_c = - X_r` 10   :math:`X_c = - Y_r` 16   :math:`X_c = - Z_r`
  5    :math:`Y_c = - Y_r` 11   :math:`Y_c = - Z_r` 17   :math:`Y_c = - X_r`
  6    :math:`Z_c = - Z_r` 12   :math:`Z_c = - X_r` 18   :math:`Z_c = - Y_r`
  ==== =================== ==== =================== ==== ===================
