.. _SHIFT:

``SHIFT``
=========

In an attempt to obtain an SCF by damping oscillations which slow down
the convergence or prevent an SCF being achieved, the virtual M.O.
energy levels are shifted up or down in energy by a shift
technique [`49 <references.html#shift>`__]. The principle is that, if
the virtual M.O.s are changed in energy relative to the occupied set,
then the polarizability of the occupied M.O.s will change *pro rata*.
Normally, oscillations are due to autoregenerative charge fluctuations.

The SHIFT method has been re-written so that the value of SHIFT changes
automatically in an attempt to optimize convergence. This can result in
a positive or zero shift of the virtual M.O. energy levels.
