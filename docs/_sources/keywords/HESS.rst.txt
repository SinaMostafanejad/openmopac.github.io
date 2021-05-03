.. _HESS:

``HESS=n``
==========

In Baker's Eigenvector Following routine, options exist for deciding how
to construct the initial Hessian matrix. The default is ``HESS=0``.
Options available are:

````

HESS=0

This is the default for geometry optimization (i.e., when ``EF`` is
used). The initial Hessian is set equal to a diagonal matrix, with the
diagonal terms set to 1000 kcal/mol/Å\ :sup:`2` for bond-lengths, 500
kcal/mol/degrees\ :sup:`2` for angles, and 200
kcal/mol/degrees\ :sup:`2` for dihedrals. If Cartesian coordinates are
used, all diagonal elements are set to 200 kcal/mol/Å\ :sup:`2`.

Do *not* specify ``HESS=0`` unless there is a good reason to do so.

````

HESS=1

This is the default for transition-state location (i.e., when ``TS`` is
used). The full Hessian matrix is constructed using single-sided
derivatives, see `Hessian Matrix <Hessian_Matrix.html>`__, using the
same density matrix throughout the entire construction of the Hessian.

````

HESS=2

A rarely used option. The Hessian matrix from an earlier run can be used
to start the current job. In order for this to work, there must be a
one-to-one correspondence of parameters to be optimized. For example, if
a geometry optimization using ``EF`` and ``AM1`` were to be followed by
a similar geometry optimization using ``EF`` and ``PM3``, then the
Hessian from the earlier calculation could be used to start the ``PM3``
job. (A simpler way of achieving this result is to use ``RESTART``, but
note that this will also use the old geometry.)
