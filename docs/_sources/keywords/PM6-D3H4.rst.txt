.. _PM6-D3H4:

PM6-D3H4
========

Use the PM6-D3H4 semiempirical model instead of the default model, PM7 :cite:p:`Stewart:2013`.
It combines the PM6 model :cite:p:`Stewart:2007` with the D3H4 model :cite:p:`Rezac:2012a` for interatomic pairwise corrections
for dispersion and hydrogen bonding.
MOPAC's implementation of the D3H4 model includes an additional correction to enhance hydrogen-hydrogen repulsion :cite:p:`Vorlova:2015`.
See the :ref:`model_summary` for a comparison of the various models available in MOPAC.

The :ref:`DISP` keyword can be used to print individual pairwise corrections from the D3H4 model.

