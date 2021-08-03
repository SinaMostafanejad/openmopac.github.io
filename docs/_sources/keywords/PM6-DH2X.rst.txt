.. _PM6-DH2X:

PM6-DH2X
========

Use the PM6-DH2X semiempirical model instead of the default model, PM7 :cite:p:`Stewart:2013`.
It combines the PM6 model :cite:p:`Stewart:2007` with the DH2X model :cite:p:`Rezac:2011` for interatomic pairwise corrections
for dispersion, hydrogen bonding, and halogen bonding.
See the :ref:`model_overview` for a comparison of the various models available in MOPAC.

The :ref:`DISP` keyword can be used to print individual pairwise corrections from the DH2X model.

.. warning::
  There are terms missing from the analytical gradients of the DH2X model.
  While these terms are often negligible, this issue can be avoided by using the :ref:`NOANCI` keyword
  to produce consistent numerical gradients, albeit at an increased computational cost.

