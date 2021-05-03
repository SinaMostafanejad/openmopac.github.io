.. _TS:

``TS``
======

Within the Eigenvector Following
routine [`7 <references.html#ef-ts>`__], the option exists to optimize a
transition state. To do this, use ``TS``. Preliminary indications are
that the TS method is much faster and more reliable than either
```SIGMA`` <sigma.html>`__ or ```NLLSQ`` <nllsq.html>`__. ``TS`` appears
to work well with Cartesian coordinates. In the event that ``TS``\ does
not converge on a stationary point, try adding
```RECALC=5`` <recalc.html>`__ to the keyword line.

Caution: When a transition state is optimized, and some optimization
flags are not set for optimization, the optimized structure might have a
significant gradient.  This usually happens when the fixed atoms are not
in their optimized positions.
