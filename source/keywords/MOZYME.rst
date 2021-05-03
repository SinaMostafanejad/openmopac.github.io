.. _MOZYME:

````

MOZYME
------

The keyword ``MOZYME`` replaces the standard SCF procedure with a
localized molecular orbital (LMO) method.  MOZYME was developed to allow
very large organic compounds, specifically enzymes, to be easily
calculated. The time required for a SCF calculation increases
approximately linearly with the size of the system, see `literature on
MOZYME <../MOZYME_literature.html>`__ and `Modeling
proteins <Modeling_proteins.html>`__.  MOZYME jobs do not run faster
when a GPU chip is used.

 

Notes, warnings and cautions concerning MOZYME calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although a job that uses the MOZYME technique should give results that
are the same as conventional SCF calculations, in practice there are
differences.  Most of these differences are small, but in some jobs the
differences between MOZYME and conventional SCF calculations,
particularly the calculation of ΔH\ :sub:`f`, can be significant.  A
single point calculation using MOZYME and conventional methods would
produce essentially the same ΔH\ :sub:`f`, and for the purposes of this
discussion the results of a single SCF calculated by both methods can be
regarded as being identical.  The problem with different ΔH\ :sub:`f`
occurs when multiple SCF calculations are performed, this is the
situation in a geometry optimization or reaction path calculation.  In
such calculations, the LMOs that result from an SCF calculation are used
as starting LMOs in the next SCF calculation.  In the first SCF
calculation, the starting LMOs are exact - they form rigorously
orthonormal sets, one for the occupied and one for the virtual sets.  At
the end of the SCF, small errors arising from truncation of the LMOs and
incomplete pairwise rotations give rise to a small degradation of the
orthonormal nature of the LMOs.  In a single SCF, this degradation is
unimportant, but when many SCF calculations are done, the loss of
orthonormality increases steadily.  This manifests itself as an error in
the calculated ΔH\ :sub:`f` and to a much smaller extent in the
gradients, and therefore, by implication, in the geometry.  The loss of
orthonormality could be corrected by re-orthogonalizing the LMOs, but
the CPU cost of this is great, and re-othogonalization is not done by
default, although it can be done if desired using
```REORTHOG`` <reorthog.html>`__.  Fortunately, a very simple procedure
exists to completely correct this error:  After any long run involving
many MOZYME SCF calculations, use the final geometry generated as the
starting point for a 1SCF calculation, and then use the ΔH\ :sub:`f`
from that calculation.  This strategy should be used:

(A) In global optimizations.

(B) In transition state location runs.

(C) At the end of IRC runs.

Do not use ```OLDENS`` <oldens.html>`__ as that would re-use the
now-inaccurate sets of LMOs, and thus defeat the purpose of doing the
1SCF calculation.  As mentioned above, the errors in the gradient are
small, so the geometry is essentially unaffected by the loss of
orthonormality.  However, it is still a good practice to optimize
geometries in three or more separate runs, if only to provide an
opportunity to check that the calculation is proceeding as intended.

During geometry optimizations, the error in  ΔH\ :sub:`f` caused by the
deterioration of the LMOs can result in the energy rising near the end
of the run.  If this happens, the lowest energy structure will be
output, instead of the last structure calculated.

By default, the M.O.s printed are LMOs.  If canonical M.O.s are needed,
use keyword ``EIGEN. EIGEN`` uses a large amount of memory and might not
work if the system is too large.  Even if it does work, it might take a
lot of CPU time, so ``EIGEN`` should only be used with ``1SCF``.

**Memory considerations:**  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With 1Gb of RAM, systems of up to 10,000 atoms can be run without
paging.  Above about 11,000 atoms, paging becomes severe, and jobs take
longer than necessary.  With 2Gb of RAM, systems of up to 18,500 atoms
can be run without significant paging.  A system of 36,774 atoms ran
successfully using 8.2Gb of memory, but each geometry optimization cycle
took about two hours.

If polarizabilities are required, use ``STATIC``.  If keyword ``POLAR``
is used, then ``STATIC`` will be used instead.

The total charge on the system must be correct. If it’s not, the charge
will be changed to that predicted by the `Lewis
structure <Lewis_structures.html>`__.  To prevent the charge being
changed, use ```CHARGE=n`` <charge.html>`__, even in cases where the
system is neutral, i.e., ``CHARGE=0``. If ``CHARGE=n`` is present, then
any mistake made by MOZYME will be trapped and reported as soon as the
job starts.  If ``CHARGE=n`` is not present, then the charge predicted
by the Lewis structure will be used.

Limitations of MOZYME
~~~~~~~~~~~~~~~~~~~~~

-  Only closed shell RHF calculations are allowed. This means that
   ``MOZYME`` calculations are limited to species in their ground state.
   Radicals and electronic excited states cannot be run.  Ions that are
   definitely open-shell, such as Cr(III), cannot be run.  Only pre-set
   oxidation states are allowed, e.g. C\ :sup:`IV` and Au\ :sup:`I`. 
   Oxidation states of metals can be changed using the
   ```METAL`` <metal.html>`__ keyword, e.g. ``METAL=(Au(+3))``. 
-  The results are not so precise, so for runs that need high precision
   (such as ``FORCE`` calculations), ``MOZYME`` is discouraged.  For
   proteins in particular, use a larger gradient norm criterion, e.g.
   ```GNORM=5``, <gnorm.html>`__ this will reduce the possibility of
   convergence failure.
-  For large systems, the recommended geometry optimizer is ``LBFGS``.
   This is a modified BFGS optimizer designed to minimize memory usage,
   and is the default for systems of 2000 parameters or more. If
   ``LBFGS`` is not wanted for any reason, then use ``BFGS``, although
   it uses a lot more memory. The default optimizer, ``EF``, uses a
   large amount of memory, and should therefore not be used in
   optimizing the geometry of large systems. In addition, because it
   uses a matrix inversion, it becomes very time consuming for large
   systems.  
-  Electrostatic Potentials cannot be calculated, that is ``ESP`` cannot
   be used, however the Parametric Molecular Electrostatic Potential, 
   ``PMEP``, can be used.

In some cases, the MOZYME SCF solution is incorrect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some very specific cases, the MOZYME method can give rise to an
incorrect SCF, specifically the MOZYME SCF solution corresponds to an
electronic excited state.  None of these cases ever occur in protein
chemistry, unless severe errors are made, but users should be aware of
their existence.   The commonest incorrect SCF solutions are obtained
when the system should not be represented by a Lewis structure.  A much
rarer type of error is found in some helical buckytubes when periodic
boundary conditions are imposed.  In cases of this type, the Lewis
structure generator simply fails to make the correct Lewis structure,
and instead attempts to correct a faulty structure by assigning charges
to two or more carbon atoms.  In all instances where incorrect SCF
solutions are found, the correct solution can be obtained by the
appropriate use of ``CVB`` or ``SETPI.``

Recommended use of MOZYME
~~~~~~~~~~~~~~~~~~~~~~~~~

``MOZYME`` can be used for simple geometric calculations, such as
geometry optimization, transition state location, and intrinsic and
dynamic reaction coordinates, and for the calculation of polarizability.
For these calculations, ``MOZYME`` can be run as a "stand alone"
calculation. If a partial geometry optimization is run, then the use of
keyword ``RAPID`` should be considered.

For calculation of vibrational frequencies, frequency-dependent
polarizability, and electronic excited states, ``MOZYME`` should be run
first, to optimize the geometry, then a conventional ``MOPAC``
calculation run.

Another effective strategy is to run a ``MOZYME`` job, followed by a
``MOPAC`` job, using the ``OLDGEO`` feature. When geometry optimizations
are being run, a ``MOZYME`` job can be run for a time, then a ``MOPAC``
job run, using ``RESTART``. That is, the ``RESTART`` function will work
when a geometry optimization or transition state location calculation is
run, regardless of the method used in generating the SCF.

`Examplex of calculations involving proteins <Protein_calculations.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
|  

| 
|  
