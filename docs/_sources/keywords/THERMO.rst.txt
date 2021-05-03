.. _THERMO:

``THERMO(nnn,mmm,lll)`` or ``THERMO=(nnn,mmm,lll)``
===================================================

Similar to ``THERMO(nnn,mmm)``, except now three numbers are supplied,
the starting temperature, *nnn*, the step-size, *mmm*, and the ending
temperature, *lll*.   If desired, the step-size can be *lll* and the
ending temperature *mmm*.

 

The step-size cannot be less than 1K. Examples:

 

 ``THERMO=(300,20,700)`` Start at 300K, end at 700K, and use a step-size
of 20K.\ ``THERMO=(300,700,20)`` Start at 300K, end at 700K, and use a
step-size of 20K.

 

See also: ```THERMO`` <thermo00.html>`__.
