.. _NOGPU:

````

NOGPU
=====

When a Graphical Processor Unit (GPU), such as an Nvidia Fermi or Kepler
chip, is present, versions of MOPAC labeled "CPU+GPU" will use that chip
to accelerate the calculations.  If MOPAC should not use a GPU, then add
``NOGPU``.  

For details of the acceleration when a GPU chip is present, see
`GPU <gpu.html>`__

See also ``THREADS=n``
