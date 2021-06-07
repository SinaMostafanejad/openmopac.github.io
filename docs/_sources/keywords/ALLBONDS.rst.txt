.. _ALLBONDS:

ALLBONDS
========

Similar to the :key:`BOND` keyword, print the bond-order matrix at the final molecular geometry.
This keyword is only available for :key:`MOZYME` calculations, for which :key:`BOND` is pruned to reduce the amount of output.
Compared to ``BOND``, the threshold for significant bond orders is lowered to :math:`\ge 0.001` and bonds involving hydrogen atoms are included.
