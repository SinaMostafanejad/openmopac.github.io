.. _STEP:

``STEP``
========

In a reaction path, if the path step is constant, ``STEP`` can be used
instead of explicitly specifying each point. The number of steps is
given by ``POINT``.

The ``STEP``\ size is under user control.  Use a value that will allow
the potential energy surface to be drawn without having it look too
jerky.  For the CH\ :sub:`3`\ CL stretch example below, the step-size
was 0.02 Ångstroms.  This gives a nice PES.  If a smaller step-size is
used, it should still run okay, but the run will take longer, because
the number of points needed will be larger.

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

 

For an alternative way of defining points on a path, that produces an
output similar to the conventional output, see `alternative
points <Optimization_flags.html#explicit_points>`__.
