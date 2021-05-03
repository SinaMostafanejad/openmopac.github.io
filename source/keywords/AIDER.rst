.. _AIDER:

``AIDER``
=========

``AIDER`` allows MOPAC to optimize an *ab initio* geometry. To use it,
calculate the *ab initio* gradients using, e.g.,
Gaussian [`14 <references.html#gaussian_92>`__]. Supply MOPAC with these
gradients, after converting them into kcal/mol. The geometry resulting
from a MOPAC run will be nearer to the optimized *ab initio* geometry
than if a single step were taken using the geometry optimizer in
Gaussian.
