.. _GEO-OK:

``GEO-OK``
==========

Normally the program will stop if certain errors occur.  If ``GEO-OK``
is present, the job will continue, but there is an increased probability
that the results will not be meaningful.  The errors that are affected
are:

| If two atoms are within 0.1 Ångstroms of each other.
| In practice, most jobs that terminate due to these checks contain
  errors in data, so caution should be exercised if ``GEO-OK`` is used.

In ``MOZYME`` calculations, if the supplied charge is incorrect and
``GEO-OK`` is present, it will be replaced by the correct charge, and
the calculation allowed to continue. In general, this is not a good
idea: if a charge is supplied, and MOZYME predicts a different charge,
examine the system to find out which is correct; don't simply assume
MOZYME is right!

When `comparing protein
structures <Protein_structure_comparison.html>`__, a special keyword,
``GEO-OK+``, is provided to allow tautomeric hydrogen atoms, i.e.,
hydrogen atoms that are on different atoms in the two structures, to be
used in the comparison.  This is a special case, and should not be used
routinely.
