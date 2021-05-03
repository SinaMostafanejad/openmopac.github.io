.. _LET:

``LET, LET(nnn)``
=================

As MOPAC evolves, the meaning of ``LET`` is changing.

Now ``LET`` means essentially "I know what I'm doing, override safety
checks".

Currently, ``LET`` has the following meanings:

1.In a ``FORCE`` calculation, it means that the supplied geometry is to be used, even if the gradients are large.
2. In a geometry optimization, the specified ``GNORM`` is to be used, even if it is less than 0.01.
3.In a ``POLAR`` calculation, the molecule is to be orientated along its principal moments of inertia before the calculation starts. ``LET`` will prevent this step being done.
4.In a EF calculation, allow the ΔH\ :sub:`f` to rise. Obviously, the ΔH\ :sub:`f` should decrease on every step, but sometimes, particularly with very flat potential energy surfaces, motion in response to the gradients might not result in a decrease in energy.  By using ``LET``, small increases in ΔH\ :sub:`f` are allowed.  This will allow the gradient minimum to be reached.  This is a well-defined point, whereas the minimum in energy is not, so in this case the use of ``LET`` is justified.  Note that the use of\ ``LET`` will not result in motion to a different minimum.
5. When comparing protein geometries, it means that hydrogen atoms that would otherwise not be paired up, because they are on different residues, are in fact paired up.
6. In a ```LOCATE-TS`` <Locate-TS.html>`__ calculation, do not perform a comparison of the reactants and products.  Useful only with small systems where the use of PDB labels can cause problems.
7. In a ```LBFGS`` <lbfgs.html>`__ calculation, the default number of cycles used in identifying the lowest-energy geometry is increased from 30 to 60.  Other values can be set using ``LET(nnn)``, where "*nnn*" is the number of cycles to be used instead of 60.

