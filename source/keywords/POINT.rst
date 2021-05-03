.. _POINT:

``POINT(S)=n``
==============

The number of points to be calculated on a reaction path is specified by
``POINT=n``. Used only with ``STEP`` in a path calculation. ``POINT`` or
``POINTS`` can be used.

``POINT``\ is under user control.  Use the smallest number that will
provide the path you want.  For the CH\ :sub:`3`\ CL stretch example
below, 40 points were used.  If you use more than the smallest number,
it should still run okay, but the run will take longer, because the path
will be longer.

Example: Stretching a C-Cl bond in CH\ :sub:`3`\ Cl. In this example,
the C-Cl bond length starts at 1.5 Ångstroms, and stretches by 0.02
Ångstroms at a time to 2.3 Ångstroms.

::

      step=0.02  point=40 
    CH3Cl Stretching the C-Cl bond

    Cl    0.00000000  0    0.0000000  0    0.0000000  0    0    0    0     
     C    1.50000000 -1    0.0000000  0    0.0000000  0    1    0    0      
     H    1.10153604  1  108.0234648  1    0.0000000  0    2    1    0      
     H    1.10231454  1  108.0092176  1  120.0000000  1    2    1    3      
     H    1.10177640  1  107.8415102  1 -120.0000000  1    2    1    3      

For a graphical representation of rotating a torsion angle in
*n*-butane, see
`GUI <Individual%20JSmol%20paths/n-Butane/n-butane.html>`__.  To
reproduce this example, download the
`ZIP <Individual%20JSmol%20paths/n-Butane/n-Butane.zip>`__ file.

For an alternative way of defining points on a path, that produces an
output similar to the conventional output, see `alternative
points <Optimization_flags.html#explicit_points>`__.
