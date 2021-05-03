.. _PMEP:

``PMEP``
========

The Parametric Molecular Electrostatic Potential of Wang and
Ford [\ `45 <references.html#pmep1>`__,\ `46 <references.html#pmep2>`__]
is generated. This method is very accurate, but has only been
parameterized for H, C, N, O, F, P, S, Cl, and Br, and only for the AM1
method. By default, the plane used is the X-Y plane at Z=0. Use
``PMEPR`` for other planes. Other keywords, e.g., ``MINMEP`` (to print
the minima) or ``PRTMEP`` (to write data for ``esplot`` to use) *must*
be present.
