.. _CHARST:

``CHARST``
==========

Print details of the working of CHARST.  CHARST calculates the symmetry
characters of the state functions, that is:

c = <Φ|Operator|Φ>

where Φ is a state function, that is, a linear combination of
microstates, Ψ.  Each microstate is an antisymmetrized product of
molecular orbitals, and each M.O. is a linear combination of atomic
orbitals, which, in turn, are represented by Slater orbitals.  Only
information on the first state is printed; the quantities printed are:

Symmetry operation in CHARST: the 3x3 Euler rotation matrix representing
the operation.  This is a rotation, mirror plane, or a product of the
two.

Transform of M.O.s: The result of the operation on the M.O.s  The effect
of the operation is to convert each M.O. of the active space into a
linear combination of the M.O.s of the active space.

State Transform for State *i* under Operation *j*:  As the name
suggests, this is the result of operating on state \|Φ\ :sub:`i`> with
operator \|Operator\ :sub:`j`, i.e.:

\|Operator\ :sub:`j`\ \|Φ\ *i*>

The state is then converted into a linear combination of states.

For ``CHARST`` to work ``DEBUG`` must also be present.  Adding
``SYMOIR`` will give the characters of the operations for all states.

See `States <states.html>`__ for more information
