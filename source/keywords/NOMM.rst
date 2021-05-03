.. _NOMM:

``NOMM``
========

All of the semiempirical methods (`MNDO <mndo.html>`__,
`AM1 <am1.html>`__, `PM3 <pm3.html>`__, `PM6 <PM6.html>`__,
`RM1 <rm1_key.html>`__, `PM7 <PM7.html>`__) underestimate the barrier to
rotation of a peptide bond. A Molecular Mechanics correction has been
added which increases the barrier in N-methyl acetamide to 14 kcal/mol.
If you do not want this correction, specify ``NOMM`` (NO Molecular
Mechanics).
