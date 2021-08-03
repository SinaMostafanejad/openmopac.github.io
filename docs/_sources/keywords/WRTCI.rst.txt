.. _WRTCI:

WRTCI
=====

Limits the number of excited states that are printed in an :ref:`INDO` calculation.

**SYNTAX:** ``WRTCI=n``

Print up to :math:`n` excited states with the lowest excitation energies.
The default value is 500.

In general, this value should be no more than 1/4 to 1/3 of :ref:`MAXCI`.
Otherwise, some of the excited states that are printed may have energies that depend noticeably on the choice of ``MAXCI``.
