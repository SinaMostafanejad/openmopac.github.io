.. _REORTHOG:

``REORTH``
----------

During a ``MOZYME``\ run, the steady accumulation of small errors (for
example, roundoff, and more important, the elimination of atoms from
LMOs) will result in the LMOs becoming non-orthogonal. These errors can
be eliminated almost completely by re-orthogonalizing the LMOs. If
``REORTH`` is present, then the LMOs will be re-orthogonalized at the
end of every 10th SCF calculation, starting with the first SCF.

In practice, a better strategy is to allow the job to run for ~500
cycles or 1-2 CPU days, then shut it down and restart it using
```RESTART`` <restart.html>`__, but without using keyword
```OLDENS`` <oldens.html>`__.  That will cause the LMO's to be
recalculated, and job to resume starting with the geometry at the end of
the previous run.
