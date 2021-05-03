.. _INVERT:

``INVERT``
==========

When ``INVERT`` is present, all optimization flags are reversed.  That
is, if an optimization flag is "1", it will be set to "0", and if it is
"0", it will be set to "1"

Refinement of a transition state for a large system runs faster when
only the atoms near to the transition state are used in gradient
minimization, and the rest are used in energy minimization. ``INVERT``
is useful for calculations of this type.  The optimization flags for all
atoms in the gradient minimization are set to "1", the rest are set to
"0".  In one calculation, a normal gradient minimization is run, in a
second calculation a geometry optimization is run, with keyword
``INVERT`` present. 

The two calculations can be combined into one job.  For example, the
first data set, for the gradient minimization, can be followed by a
second data set consisting of keywords "```OLDGEO`` <oldgeo.html>`__"
and "``INVERT``" plus any other keywords needed for the job.

Alternatively, make two complete data sets, one for gradient
minimization and one for energy minimization.  Run these data sets on
different computers.  Then edit the resulting ARC files to make up a new
data set.  This saves time, because the jobs run twice as fast.

 

 
