.. _ROOT:

ROOT
====

Target an excited state in a configuration interaction calculation.
This keyword can be combined with :ref:`MS` to target a state based on spin, energy, and optionally symmetry.

**SYNTAX:** ``ROOT=n``

Target the :math:`n`th eigenstate ordered by increasing energy.
The default value is ``ROOT=1``, which corresponds to the lowest energy state.

When combined with the ``MS`` keyword, only the specified spin states are considered in this selection process.

For example, ``ROOT=2`` targets the first excited state.
When combined with ``MS=1``, it targets the triplet state with the second lowest energy among all triplet states.

**SYNTAX:** ``ROOT=symbol``

Target an eigenstate corresponding to a combined quantum number and symmetry label, ``symbol``.
``symbol`` is a string concatenating quantum numbers (``Q.N.``) and symmetry labels as printed by MOPAC.

When multiple spin states have the same quantum number and symmetry label, the lowest-energy spin state will be targeted.
Again, the ``MS`` keyword can be used to target a specific spin state.

For example, ``ROOT=2T2g`` targets the second-lowest energy state having T2g symmetry.
When combined with ``MS=1``, it targets the second-lowest energy that is both a triplet state and has T2g symmetry.

.. note::

  For symmetries that induce energy degeneracies, the subspace of energy-degenerate eigenstates are counted and printed
  by MOPAC as a single state. State labels are skipped to account for and denote this degeneracy.
  Thus, ``ROOT=n`` may not target the state labeled by ``n`` if there are any degenerate subspaces of lower energy.

  When a degenerate subspace of states is targeted, the reference state becomes a statistical superposition
  over the degenerate states so that geometry optimization is able to preserve symmetries.
  To target a specific state in a degenerate subspace so as to break symmetry in the geometry optimization (i.e. Jahn-Teller distortion),
  the :ref:`NOSYM` keyword should be used to suppress the detection and use of point-group symmetry.
