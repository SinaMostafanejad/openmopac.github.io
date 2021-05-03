.. _AIGIN:

``AIGIN``
=========

If the geometry (Z-matrix) is specified using the Gaussian
format [`14 <references.html#gaussian_92>`__], then this will normally
be read in without difficulty. In the event that it is mistaken for a
normal MOPAC-type Z-matrix, the keyword ``AIGIN`` is provided. ``AIGIN``
will force the data-set to be read in assuming Gaussian format. This is
necessary if more than one system is being studied in one run.
