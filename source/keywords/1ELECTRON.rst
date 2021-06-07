.. _1ELECTRON:

1ELECTRON
=========

Print the matrix of one-electron resonance integrals for the final molecular geometry.
For the MNDO-form models implemented in MOPAC, this matrix has the form :cite:p:`Dewar:1977`

.. math::

   H_{\lambda\sigma} = \frac{1}{2} (\beta_{\lambda} + \beta_{\sigma}) S_{\lambda\sigma}

where :math:`\lambda` and :math:`\sigma` are the atomic orbital indices,
:math:`\beta_{\lambda}` are the atomic orbital energies,
and :math:`\S_{\lambda\sigma}` is the atomic orbital overlap matrix.
This matrix is only one term of the full MNDO-form Fock matrix.
