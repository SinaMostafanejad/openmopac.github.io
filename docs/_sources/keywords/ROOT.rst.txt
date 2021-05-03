.. _ROOT:

``ROOT=n``
==========

In a configuration interaction calculation, a specific state can be
requested by specifying the state name and the quantum number of that
state.  The lowest state of each type has the quantum number 1, the next
is 2 and so on.  To see the quantum numbers and state names, run a 1SCF
calculation for the desired configuration interaction.  The normal way
to define the C.I. is to use the keywords ```C.I.=n`` <ci=n.html>`__.
and ```MECI`` <meci.html>`__ (to print out the state information). Two
ways of defining the desired state are provided: ``ROOT=n``, where *n*
is an integer, and ``ROOT=n<text>``, where *n* is an integer and <text>
is a text string.

``ROOT=``\ n

The *n*'th root of a C.I. calculation is to be used in the calculation.
If a keyword specifying the spin-state is also present, e.g. ``SINGLET``
or ``TRIPLET``, then the *n*'th root of that state will be selected.
Thus ``ROOT=3`` and ``SINGLET`` will select the third singlet root. If
``ROOT=3`` is used on its own, then the third root will be used,
regardless of the states' name.  This might be a triplet, the third
singlet, or the second singlet (the second root might be a triplet). If
the state selected is degenerate, all components of that state will be
selected.

``ROOT=``\ n<text>

The *n*'th root of a C.I. calculation that has the symmetry <text> is to
be used in the calculation.  If a keyword specifying the spin-state is
also present, e.g. ``SINGLET`` or ``TRIPLET``, then the *n*'th root of
that state that has the symmetry <text> will be selected. Thus, in an
octahedral system, ``ROOT=3T2g`` and ``SINGLET`` will select the third
singlet T2g root. If ``ROOT=3T2g`` is used without any spin-state being
specified, then the third T2g root will be used, regardless of spin. If
the state selected is degenerate, all components of that state will be
selected.

See also ```C.I.=n`` <ci=n.html>`__ .

To see how these different forms behave, consider the following states
of a d\ :sup:`6` transition metal complex:

+-----------------+-----------------+-----------------+-----------------+
| STATE           | Q.N.            | Spin            | Symmetry        |
+-----------------+-----------------+-----------------+-----------------+
| 1               | 1               | TRIPLET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 4               | 1               | SINGLET         | A1g             |
+-----------------+-----------------+-----------------+-----------------+
| 5               | 1               | SINGLET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 8               | 1               | TRIPLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 11              | 1               | QUINTET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 14              | 1               | SEPTET          | A1g             |
+-----------------+-----------------+-----------------+-----------------+
| 15              | 1               | QUINTET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 18              | 2               | TRIPLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 21              | 3               | TRIPLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 24              | 2               | SINGLET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 27              | 2               | TRIPLET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 30              | 1               | TRIPLET         | A2g             |
+-----------------+-----------------+-----------------+-----------------+
| 31              | 1               | SINGLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 34              | 3               | TRIPLET         | T2g             |
+-----------------+-----------------+-----------------+-----------------+
| 37              | 4               | TRIPLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 40              | 1               | TRIPLET         | Eg              |
+-----------------+-----------------+-----------------+-----------------+
| 42              | 2               | SINGLET         | T1g             |
+-----------------+-----------------+-----------------+-----------------+
| 45              | 1               | SINGLET         | Eg              |
+-----------------+-----------------+-----------------+-----------------+
| 47              | 1               | QUINTET         | Eg              |
+-----------------+-----------------+-----------------+-----------------+

``ROOT=14`` would select the 14th state, the 1\ :sup:`7`\ A\ :sub:`1g`
state. No spin being specified, ``ROOT`` applies to the STATE column.

``ROOT=7`` and ``QUINTET`` would select the 47th and 48th states, the
1\ :sup:`5`\ E\ :sub:`g`  state. This is the 7th quintet state, the
states 1-6 being T1g, T1g, T1g, T2g, T2g, and T2g. That these states are
degenerate is not important, because ``ROOT=n`` specifies the n'th
state, without regard to symmetry.

``ROOT=2T2g`` and ``TRIPLET`` would select the 27th, 28th, and 29th
states, the 2\ :sup:`3`\ T\ :sub:`2g` state. This is the preferred
method of specifying states. When ``ROOT=``\ n<text> is used then the
state specified will not change if the state moves up or down the list
of states. If the system has no symmetry, ``ROOT=nA`` can be used.

When a geometry is to be optimized, symmetry should be used, if
present.  This is particularly important in octahedral transition metal
complexes. If the state has orbital degeneracy, e.g. if it is of type E,
T, G, or H, then Jahn-Teller effects might cause a loss of symmetry.
High symmetry is automatically detected, so, if present, it will be
conserved. However, during a normal unconstrained geometry optimization,
minor excursions from high symmetry are allowed, and these might confuse
the high-symmetry detector.  To prevent this, use symmetry.  In the case
of a simple octahedral complex, MX\ :sub:`6`, the data set might look
like this:

``ROOT=1T2g QUINTET  OPEN(5,5) MECI  SYMMETRY Generic octahedral complex  M 0.0 0   0 0   0 0 0 0 0 X 2.0 1   0 0   0 0 1 0 0  X 2.0 0  90 0   0 0 1 2 0  X 2.0 0  90 0  90 0 1 2 3 X 2.0 0  90 0 180 0 1 2 3  X 2.0 0  90 0 -90 0 1 2 3  X 2.0 0 180 0   0 0 1 2 3   2 1 3 4 5 6 7``
 
