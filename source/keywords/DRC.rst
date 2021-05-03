.. _DRC:

``DRC=n.nnn``
=============

In a DRC calculation, the 'half-life' for loss of kinetic energy is
defined as *n*.\ *nnn* femtoseconds. This is equivalent to the system
cooling down. If the 'half-life' is negative, energy will be added to
the system. This is equivalent to heating it up. If *n*.\ *nnn* is set
to zero, infinite damping simulating a very condensed phase is obtained.

 

Here is an example of simulated annealing:

::

    DRC=50 bigcycles=1000 T-priority
   Formaldehyde, starting with the C=O bond stretched by ~0.2 Angstroms
    
     O     0.0 +0    0.0 +0    0.0 +0                      
     C     1.4 +1    0.0 +0    0.0 +0     1     0     0      
     H     1.1 +1  121.0 +1    0.0 +0     2     1     0      
     H     1.1 +0  121.0 +0  180.0 +0     2     1     3        

As usual, the plus "+" signs are optional, the optimization flags will
be ignored, and the coordinates will be converted to Cartesian at
run-time.

DRC=50 - The half-life for cooling is 50 fs.

`bigcycles <bigcycles.html>`__\ =1000 - Restrict the run. If this
keyword is not present, the job will produce a very large output.

`T-priority <t-priority.html>`__ - There are two common styles for
monitoring a DRC, time and motion.  In this case time is used.

See also: `X-priority <x-priority.html>`__,
`H-priority <h-priority.html>`__
