.. _NOANCI:

NOANCI
======

Use numerical derivatives for configuration interaction calculations and corrections (e.g. open-shell RHF)
instead of Liotard's analytical method :cite:p:`Dewar:1990`, which is the default method.
Numerical derivatives are much slower and should only be used to check the analytical derivatives
if there are concerns about their validity or accuracy.
