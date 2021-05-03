.. _PM6-DHplus:

``PM6-DH+``
===========

Usesthe PM6-DH+procedure of M. Korth, `"Third-Generation
Hydrogen-Bonding Corrections for Semiempirical QM Methods and Force
Fields <http://pubs.acs.org/doi/abs/10.1021/ct100408b>`__\ ,"J. Chem.
Theory Comput., 2010, 6 (12), pp 3808–3816. 

Abstract:  Computational modeling of biological systems is a rapidly
evolving field that calls for methods that are able to allow for
extensive sampling with systems consisting of thousands of atoms.
Semiempirical quantum chemical (SE) methods are a promising tool to aid
with this, but the rather bad performance of standard SE methods for
non-covalent interactions is clearly a limiting factor. Enhancing SE
methods with empirical corrections for dispersion and hydrogen-bonding
interactions was found to be a big improvement, but for the
hydrogen-bonding corrections the drawback of breaking down in the case
of substantial changes to the hydrogen bond, e.g., proton transfer,
posed a serious limitation for its general applicability. This work
presents a further improved hydrogen bonding correction that can be
generally included in parameter fitting procedures, as it does not
suffer from the conceptual flaws of previous approaches: hydrogen bonds
are now treated as an interaction term between electronegative acceptor
and donor atoms, “weighted” by a function of the position of H atoms
between them, and multiplied with a damping function to correct the
short- and long-range behavior. The performance of the new approach is
evaluated for PM6, AM1, OM3, and SCC-DFTB as well as several force-field
(FF) methods for a number of standard benchmark sets with
hydrogen-bonded systems. The new approach is found to reach the same
accuracy as the second-generation hydrogen-bonding correction with less
parameters, while it avoids among other issues the conceptual problem
with electronic structure changes. SE methods augmented this way reach
the accuracy of DFT-D approaches for a large number of cases
investigated, while still being about 3 orders of magnitude faster.
Moreover, the new correction scheme is transferable also to FF methods
that were shown to have serious problems with hydrogen-bonding
interactions.

The PM6-DH+ method was parameterized to reproduce interaction energies
for geometries obtained from high-level quantum mechanical
calculations.  See `accuracy <pm6_dh_plus_accuracy.html>`__.

The PM6-DH+ procedure corrects binding errors in the PM6 method.  It can
be used with geometry optimization or with a single point
(```1SCF`` <one_scf.html>`__) calculation.  Normally, two or three
calculations would be needed to get the binding energy. 

Notes
~~~~~

Frozen geometries were used during the development of PM6-DH+.  By
contrast, in the proposed strategy, fully optimized geometries are
used.  No inconsistency is involved - by sketching a simple Born cycle,
it becomes apparent that any errors arising from optimizing the PM6-DH+
parameters using frozen geometries and using those same parameters when
calculating the binding energy using the above strategy would be very
small; they would contribute only second order perturbation effects, and
would be completely negligible. 

To print the individual components of DH+, add\ ```DISP`` <disp.html>`__

 

 

 
