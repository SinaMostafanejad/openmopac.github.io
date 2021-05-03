.. _KINETIC:

``KINETIC=n.nnn``
=================

In a DRC calculation *n*.\ *nnn* kcal/mol of excess kinetic energy is
added to the system.  At the start of a DRC calculation, the atoms are
initially at rest.  So kinetic energy cannot be added to the system. 
When KINETIC=n.nn is used, the DRC is first run for a few steps until
the atoms have a significant velocity.  This is when the kinetic energy
amounts to 0.2 kcal/mol.  When that happens, the kinetic energy is
increased suddenly by *n.nn* kcal/mol.  The next few steps will show
errors in the output as the energy is added to the system.  The use of
0.2 kcal/mol is arbitrary - any small number could be used.

If a system starts off with an energy of -100 kcal/mol, and KINETIC=10
is used, the DRC will be run with a total (kinetic plus potential) of
-90 kcal/mol.

| In an IRC=1 or IRC=-1 calculation, at the start of the run, the
  geometry is shifted by an amount proportional to *n*.\ *nnn.* Try
  using 20 to begin with, in the direction of the reaction normal
  coordinate. A sufficiently large value will ensure that the IRC will
  follow the correct path, but an excessively large value will distort
  the shape of the top of the reaction barrier.
|  

See `VELOCITY <velocity.html>`__ and `Dynamic and Intrinsic Reaction
Coordinates <DRC_coordinates.html#t_irc>`__ for more details.
