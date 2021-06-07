.. _PM6-D3H4X:

PM6-D3H4X
=========

Use the PM6-D3H4X semiempirical model instead of the default model, PM7 :cite:p:`Stewart:2013`.
It combines the PM6 model :cite:p:`Stewart:2007` with the D3H4X model :cite:p:`Rezac:2012b` for interatomic pairwise corrections
for dispersion, hydrogen bonding, and halogen bonding.
MOPAC's implementation of the D3H4X model includes an additional correction to enhance hydrogen-hydrogen repulsion :cite:p:`Vorlova:2015`
and revised halogen-bonding parameters :cite:p:`Brahmkshatriya:2013`.
See the :ref:`model_summary` for a comparison of the various models available in MOPAC.

The :ref:`DISP` keyword can be used to print individual pairwise corrections from the D3H4X model.
