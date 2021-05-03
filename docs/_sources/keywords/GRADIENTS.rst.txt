.. _GRADIENTS:

``GRADIENTS``
=============

In a ``1SCF`` calculation gradients are not calculated by default: in
non-variationally optimized systems this could take a lot of time.
``GRADIENTS`` allows the gradients, in kcal.(Å.mol)\ :sup:`-1`, to be
calculated. Normally, gradients will not be printed if the gradient norm
is less than 2.0. However, if ``GRADIENTS`` is present, then the
gradient norm and the gradients will unconditionally be printed.
Abbreviation: ``GRAD``.
