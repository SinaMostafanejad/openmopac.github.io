.. _DISEX:

``DISEX=n.nn``
==============

Used for the COSMO method (see ``EPS``). In units of mean segment
diameter, *n*.\ *nn* is the distance up to which the interactions of two
segments is calculated as the sum of fine grid interactions. The default
value is 2.0.

``DISEX`` should not be altered unless there are problems with precision
(note: precision applies to the mathematics, and not to the accuracy.)
To increase the precision given by ``DISEX``, set ``DISEX`` to a smaller
number. If, after running a job with ``DISEX`` set smaller, e.g.
``DISEX=1.8``, the results have changed significantly, then reduce
``DISEX`` again, and re-run the job.
