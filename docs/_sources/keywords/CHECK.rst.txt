.. _CHECK:

``CHECK``
=========

If a job runs to completion, but the calculated Heat of Formation,
ΔH\ :sub:`f,` is very large (over 10,000 kcal/mol) is likely that there
is a fault in the geometry.  If the job is re-run using keyword CHECK,
the interatomic distances will be checked for atom distances of less
than 0.9 Å.  If there are any such short distances, they will be
reported and the job stopped.  If none are found, the run will continue.
