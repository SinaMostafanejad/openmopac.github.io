.. _WRTCONF:

WRTCONF
=======

Adjusts the CI coefficients and configurations of excited states that are printed in an :ref:`INDO` calculation.

**SYNTAX:** ``WRTCONF=x``

Print configurations with CI coefficients greater than :math:`x` in magnitude.
The default value is 0.04.
Smaller values give a more precise view of the composition of the CI states, but can make the output files large.
