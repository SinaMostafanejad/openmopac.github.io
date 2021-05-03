.. _RESTART:

``RESTART``
===========

When a job has been stopped, for whatever reason, and intermediate
results have been stored, then the calculation can be restarted at the
point where it stopped by specifying ``RESTART``. The most common cause
of a job stopping before completion is its exceeding the time allocated.
A saddle-point calculation has no restart, but the output file contains
information which can easily be used to start the calculation from a
point near to where it stopped.

The restart file contains all the geometry data: current geometry, cycle
number, gradient and Hessian information, if calculated, etc.  It does
not contain information on the atoms, so the restart data set has to
have a normal geometry just like a non-restart data set.  This is used
only for supplying the atom-types and number of atoms.. 

Example: If the following data set is run, it will stop after three
geometry optimization cycles, and output a message indicating that
restart files have been created.

| cycles=3
| Ethanol
| C2H5OH
| O
| C 1.5 1 0 0 0 0 1
| C 1.5 1 120 1 0 0 2 1
| H 1.0 1 120 1 90 1 1 2 3
| H 1.0 1 109 1 120 1 2 1 3
| H 1.0 1 109 1 240 1 2 1 3
| H 1.0 1 109 1 0 1 3 2 1
| H 1.0 1 109 1 120 1 3 2 1
| H 1.0 1 109 1 240 1 3 2 1

| By adding the word "RESTART" to the original data set, and
  re-submitting the job, the calculation can be continued.  In this
  example, "cycles=3" has been deleted; this allows the job to run to
  completion.
| restart
| Ethanol
| C2H5OH
| O
| C 1.5 1 0 0 0 0 1
| C 1.5 1 120 1 0 0 2 1
| H 1.0 1 120 1 90 1 1 2 3
| H 1.0 1 109 1 120 1 2 1 3
| H 1.0 1 109 1 240 1 2 1 3
| H 1.0 1 109 1 0 1 3 2 1
| H 1.0 1 109 1 120 1 3 2 1
| H 1.0 1 109 1 240 1 3 2 1
|  

It is not necessary to change the geometric data to reflect the new
geometry, although this can be done, if desired. When ``RESTART`` is
used, the <file>.res file contains all the geometric data, and this will
immediately over-write the geometry supplied by the data set.  Note,
however, that the data set must have a geometry because the <file>.res
file does not contain the atom types. A convenient way to monitor a long
run is to specify ``1SCF`` and ``RESTART``; this will give a normal
output file at very little cost.

Note: Two restarts exist in the IRC calculation. If an IRC calculation
stops while in the FORCE calculation, then a normal restart can be done.
If the job stops while doing the IRC calculation itself then the keyword
``IRC=n`` should be changed to ``IRC``, or it can be omitted if ``DRC``
is also specified. The absence of the string "``IRC=``" is used to
indicate that the ``FORCE`` calculation was completed before the restart
files were written.

See also ```OLDENS`` <oldens.html>`__.
