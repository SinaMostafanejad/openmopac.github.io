.. _SIGMA:

``SIGMA``
=========

When refining transition states, and ``TS`` is *not* wanted, the
McIver-Komornicki gradient norm
minimization [\ `9 <references.html#sigma1>`__,\ `10 <references.html#sigma2>`__]
routines, POWSQ and SEARCH, can be used by including ``SIGMA``. These
are very rapid routines, but do not work for all species. If the
gradient norm is low, i.e., less than about 5 units, then ``SIGMA`` will
probably work; in most cases where ``TS`` does not work, ``NLLSQ`` is
recommended. SIGMA first calculates a Hessian matrix, a slow step, then
works out the direction of fastest descent, and searches along that
direction until the gradient norm is minimized. The Hessian is then
partially updated in light of the new gradients, and a fresh search
direction found. Clearly, if the Hessian changes markedly as a result of
the line-search, the update done will be inaccurate, and the new search
direction will be faulty. ``SIGMA`` should be avoided if at all possible
when non-variationally optimized calculations are being done.

If the Hessian is suspected to be corrupt within SIGMA, it will be
automatically recalculated. This frequently speeds up the rate at which
the transition state is located. If you do not want the Hessian to be
reinitialized--it is costly in CPU time--specify ``LET`` on the keyword
line.
