.. _LBFGS:

``LBFGS``
=========

Optimize the geometry using the L-BFGS function minimizer. This is based
on the BFGS optimizer, but it does not store the inverse Hessian,
instead it is calculated as needed. Because of this, the L-BFGS method
uses very little storage, and is therefore suitable for optimizing very
large systems.

The L-BFGS optimizer is the default if 100 or more variables are to be
optimized.  For such systems, L-BFGS is more efficient than Baker's
Eigenfollowing, however there is no guarantee that the L-BFGS method
will produce a minimum energy.  In systems where two or more species are
present, and only low-energy interactions bind the species together, the
L-BFGS optimizer sometimes fails to produce a minimum energy system . 
If this happens, or if for any other reason the L-BFGS is not wanted,
add keyword ```EF`` <ef.html>`__ or ```BFGS`` <bfgs.html>`__.  Both
these methods are more reliable for difficult systems.

Note on use of L-BFGS with large systems, particularly proteins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The L-BFGS optimization method does not explicitly minimize the heat of
formation, see below, therefore it is possible for the ΔH\ :sub:`f` to
rise on going from one cycle to the next, particularly near the end of a
geometry optimization run.  As the objective of geometry optimization is
finding the lowest-energy geometry, terminating an optimization with a
structure that is not the lowest-energy calculated is not acceptable. 
This fault most often occurs in large system, especially in proteins,
and to avoid it the optimization procedure has been modified as follows:

During a geometry optimization that uses the L-BFGS optimizer, the
system with the lowest ΔH\ :sub:`f` is stored.  At the beginning of a
job, the ΔH\ :sub:`f` is calculated and it, and the starting geometry,
are stored.  After each subsequent cycle, the ΔH\ :sub:`f` is compared
with the value in the store.  If it is lower (more negative), then the
values in the store are over-written with the current geometry and
ΔH\ :sub:`f`, so that after every cycle the ΔH\ :sub:`f` and geometry in
the store are always the best values calculated.  At the end of the run
the working geometry will be replaced by whatever geometry was in
storage if the ΔH\ :sub:`f` of the working geometry is more positive
than the value for the stored geometry.  If that is done, then the
ΔH\ :sub:`f` of the lowest-energy geometry will be re-evaluated. The
final output will then refer to this geometry.

This workaround is used for all jobs that use the L-BFGS optimizer that
end normally, or if the job runs out of time, or the
`SHUT <http://openmopac.net/manual/shut.html>`__ command is issued. 
Warning: If a large job is restarted using ``RESTART`` and
```1SCF`` <one_scf.html>`__ is specified, then the workaround will not
be used.  For large jobs, if a ``1SCF`` is wanted and there is a risk of
the ΔH\ :sub:`f` in the <file>.RES file not being the lowest calculated,
then use the final geometry from the output file from the previous run. 

The defaults number of cycles for deciding if the ΔH\ :sub:`f` is at a
minimum is 30.  This will be reset to 60 if keyword
```PRECISE`` <precise.html>`__ is used, or to another value if
``LET(nnn)``\ is used. This option is useful when there is a risk of the
optimization stopping too far from the minimum.

For most jobs the final geometry will be the best, and this workaround
would not be used, but if the lowest-energy geometry is not the last
geometry calculated by L-BFGS, then the message: "**CURRENT BEST VALUE
OF HEAT OF FORMATION**" will be printed.

Notes on the L-BFGS optimization method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The L-BFGS optimization procedure is a limited memory variation of the
Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton algorithm.  Rather
than storing the Hessian, the L-BFGS method stores only the gradient
vectors for the the last few geometries calculated.  In MOPAC, a maximum
of 12 gradient vectors are stored.  It then uses this set of vectors to
approximate individual elements of the Hessian as they are needed.  It
is good for large systems, such as proteins and other macromolecules and
solids.  In practice, it also seems to be the best geometry optimizer
for systems of thirty or more atoms.  Go on-line for more detail on the
`L-BFGS method <https://en.wikipedia.org/wiki/Limited-memory_BFGS>`__

It uses the gradient only, by moving the atoms in the system in the
downhill direction. Although the L-BFGS method does not use the
ΔH\ :sub:`f`, for most systems it does minimize the ΔH\ :sub:`f` as a
side effect of minimizing the gradient.  Although it is not explicit in
the algorithm, the L-BFGS method, like the other geometry optimizers in
MOPAC, does optimize the geometry to a ground state.  There has not yet
been a worked example of it optimizing an unconstrained geometry to a
transition state.

Using only the gradient and not the ΔH\ :sub:`f` has advantages, in that
when the L-BFGS method makes a bad step, it uses the results of that
step to work out a better step.  This leads to a more rapid descent to a
stationary point on the Potential Energy Surface.

 

 

 
