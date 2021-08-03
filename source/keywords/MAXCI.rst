.. _MAXCI:

MAXCI
=====

The maximum number of configurations in an :ref:`INDO` calculation.

**SYNTAX:** ``MAXCI=n``

The maximum number is set to :math:`n`.
Configurations are sorted by energy, and the :math:`n` lowest-energy excitations are retained.
By default, this value is set to 2000.
It can be increased to :math:`\approx 7000` before running into memory constraints.
