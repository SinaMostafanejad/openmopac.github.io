.. _ALLBONDS:

ALLBONDS
========

Similar to the :ref:`BONDS` keyword, prints the bond-order matrix at the final molecular geometry.
This keyword is only available for :ref:`MOZYME` calculations, for which ``BONDS`` is pruned to reduce the amount of output.
Compared to ``BONDS``, the threshold for significant bond orders is lowered to :math:`\ge 0.001` and bonds involving hydrogen atoms are included.
