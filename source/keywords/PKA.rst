.. _PKA:

``PKA``
=======

 

When ``pKa`` is specified, the pKa of hydrogen atoms attached to oxygen
atoms is calculated and printed.  For a large set of
`compounds <../pKa_table.html>`__, the average unsigned error is about
0.31 pKa units.

pKa is calculated using the O-H distance calculated using PM6, and a
charge calculated using a method specifically designed to reproduce the
charge for pKa. 

Do not use COSMO in optimizing the geometry.  Use PM6 only.  When the
pKa calculation is done on the optimized PM6 geometry, the COSMO
technique is switched on temporarily in order to get a better charge on
the hydrogen atom(s). Once the pKa calculation finishes, the COSMO is
switchod off again.

Known problem: If an ionizable hydrogen is within hydrogen-bonding
distance of an atom with a large negative charge, as in the ene-ol form
of acetylacetone, then the predicted pKa will be much too negative. 
This is a consequence of the induced extra positive charge on that
hydrogen. 
