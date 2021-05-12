.. _T:

``T``
=====

This is a facility to allow the program to shut down in an orderly
manner on computers with execution time cpu limits.

The total cpu time allowed for the current job is limited to *nn*.\ *nn*
seconds; by default this is two days, i.e., 172,800 seconds. If the next
cycle of the calculation cannot be completed without running a risk of
exceeding the assigned time the calculation will write a restart file
and then stop. The safety margin is 100 percent; that is, to do another
cycle, enough time to do at least two full cycles must remain.

If several systems are run in one job, then the time allowed for *all*
the jobs is two days, unless ``T=n.nn`` is used. If ``T=n.nn`` is used,
then the allowed time *for the remainder of the job* is *n*.\ *nn*
seconds. This means that if the allowed time for each system is to be an
hour, then the keyword ``T=1h`` must be specified in each system.

Alternative specifications of the time are ``T=nn.nnM``, which defines
the time in minutes, ``T=nn.nnH``, in hours, ``T=nn.nnD``, in days, and
``T=nn.nnW``, in weeks,  for long jobs.

A job that's running can be instructed to run out of time by issuing the
`SHUT <shut.html>`__ command.  If that is done, then, at the first
opportunity, MOPAC will write out a RESTART file called <file>.res and a
DENSITY file, <file>.den.  These can then be read in to a subsequent job
using ```RESTART`` <restart.html>`__ and ```OLDENS`` <oldens.html>`__.

 
