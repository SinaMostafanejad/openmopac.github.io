.. _PM6-DH2:

PM6-DH2
=======

Use the PM6-DH2 semiempirical model instead of the default model, PM7 :cite:p:`Stewart:2013`.
It combines the PM6 model :cite:p:`Stewart:2007` with the DH2 model :cite:p:`Korth:2010a` for interatomic pairwise corrections
for dispersion and hydrogen bonding.
See the :ref:`model_overview` for a comparison of the various models available in MOPAC.

The :ref:`DISP` keyword can be used to print individual pairwise corrections from the DH2 model.

.. warning::
  There are terms missing from the analytical gradients of the DH2 model.
  While these terms are often negligible, this issue can be avoided by using the :ref:`NOANCI` keyword
  to produce consistent numerical gradients, albeit at an increased computational cost.

