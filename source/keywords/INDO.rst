.. _INDO:

``INDO``
========

(This keyword was written by Prof. Rebecca L. M.
`Gieseking <https://sites.google.com/a/brandeis.edu/gieseking/>`__,
Brandeis University)

The INDO/S method is to be used. The default parameters are Zerner’s
INDO/S parameters (also known as ZINDO/S). Other parameters can be read
in from an external file using ```EXTERNAL`` <external.html>`__. Since
the INDO/S parameters were developed exclusively for spectroscopic
(excited-state) properties, calculations involving energy gradients
(geometry optimizations, transition states, frequencies, etc.) are not
available.

Advantages of adding INDO/S
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The INDO/S Hamiltonian (or equivalently, ZINDO/S),\ :sup:`1` has
  parameters designed specifically to reproduce vertical excited-state
  energies using a configuration interaction ( ``C.I.``) approach with
  single excitations (``CIS``). In benchmarking studies, INDO/S has
  performed significantly better than traditional NDDO-based
  semiempirical methods for singlet excited states. For a set of 103
  excited states of prototypical π-conjugated organic molecules, the
  mean absolute error at the INDO/S level is 0.51 eV, versus 1.35 eV at
  the MNDO level, 1.19 eV at the AM1 level, and 1.41 eV at the PM3
  level.\ :sup:`2`
| The solvatochromic shifts computed using INDO/S and the
  `COSMO <cosmo.html>`__ solvent model are in good agreement with
  experimental results and comparable to the accuracy of typical DFT
  functionals. For a series of 24 donor-acceptor substituted polyenes,
  the computed solvatochromic shift between toluene and ethanol at the
  INDO/CIS level has a root mean square error of 0.087 eV versus
  experimental results.  This can be compared with the 0.077 eV at the
  ωB97XD/6-31G\* level and 0.116 eV at the B3LYP/6-31G\*
  level.\ :sup:`3`
| The INDO/S Hamiltonian has also shown success in understanding excited
  states with large double-excitation character using either single and
  double excitations (``CISD``) or a multi-reference approach
  (``MRCI``); these calculations have been particularly important in
  understanding the nonlinear optical properties of several classes of
  π-conjugated organic molecules.\ :sup:`4–7` The INDO/S Hamiltonian
  also provides good agreement with Time-Dependent Density Functional
  Theory (TD-DFT) for the optical properties of noble metal
  clusters\ :sup:`8,9` and is to date the only semiempirical method to
  yield physically reasonable ground-state electronic structures for
  these clusters.\ :sup:`10`
|  

(1)      Ridley, J.; Zerner, M. An Intermediate Neglect of Differential
Overlap Technique for Spectroscopy: Pyrrole and the Azines. *Theor.
Chim. Acta* **1973**, *32*, 111–134. https://doi.org/10.1007/BF00528484.

(2)      Silva-junior, M. R.; Thiel, W. Benchmark of Electronically
Excited States for Semiempirical Methods: MNDO, AM1, PM3, OM1, OM2, OM3,
INDO/S, and INDO/S2. *J. Chem. Theory Comput.* **2010**, *6* (5),
1546–1564. https://doi.org/10.1021/ct100030j.

(3)      Gieseking, R. L.; Ratner, M. A.; Schatz, G. C. Implementation
of INDO/SCI with COSMO Implicit Solvation and Benchmarking for
Solvatochromic Shifts. *J. Phys. Chem. A* **2016**, *120*, 9878–9885.
https://doi.org/10.1021/acs.jpca.6b10487.

(4)      Pierce, B. M. A Theoretical Analysis of Third-Order Nonlinear
Optical Properties of Linear Polyenes and Benzene. *J. Chem. Phys.*
**1989**, *91*, 791–811. https://doi.org/10.1063/1.457132.

(5)      Meyers, F.; Marder, S. R.; Pierce, B. M.; Bredas, J. L.
Electric Field Modulated Nonlinear Optical Properties of Donor-Acceptor
Polyenes: Sum-over-States Investigation of the Relationship between
Molecular Polarizabilities (Alpha, Beta, and Gamma) and Bond Length
Alternation. *J. Am. Chem. Soc.* **1994**, *116*, 10703–10714.
https://doi.org/10.1021/ja00102a040.

(6)      Geskin, V. M.; Lambert, C.; Brédas, J. L. Origin of High
Second- and Third-Order Nonlinear Optical Response in Ammonio/Borato
Diphenylpolyene Zwitterions: The Remarkable Role of Polarized Aromatic
Groups. *J. Am. Chem. Soc.* **2003**, *125*, 15651–15658.
https://doi.org/10.1021/ja035862p.

(7)      Gieseking, R. L.; Ensley, T. R.; Hu, H.; Hagan, D. J.; Risko,
C.; Van Stryland, E. W.; Brédas, J.-L. Nonlinear Optical Properties of
X(C 6 H 5 ) 4 (X = B – , C, N + , P + ): A New Class of Molecules with a
Negative Third-Order Polarizability. *J. Am. Chem. Soc.* **2015**,
*137*, 9635–9642. https://doi.org/10.1021/jacs.5b04377.

(8)      Shapley, W. A.; Reimers, J. R.; Hush, N. S. INDO/S Parameters
for Gold. *Int. J. Quantum Chem.* **2002**, *90*, 424–438.
https://doi.org/10.1002/qua.10058.

(9)      Gieseking, R. L.; Ratner, M. A.; Schatz, G. C. Semiempirical
Modeling of Ag Nanoclusters: New Parameters for Optical Property Studies
Enable Determination of Double Excitation Contributions to Plasmonic
Excitation. *J. Phys. Chem. A* **2016**, *120*, 4542–4549.
https://doi.org/10.1021/acs.jpca.6b04520.

(10)    Gieseking, R. L. M.; Ratner, M. A.; Schatz, G. C. Benchmarking
Semiempirical Methods To Compute Electrochemical Formal Potentials. *J.
Phys. Chem. A* **2018**, *122*, 6809–6818.
https://doi.org/10.1021/acs.jpca.8b05143.

 

Details to be aware of when using INDO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Normally only model RHF systems. UHF is not implemented and although
  ROHF is implemented its SCF convergence behavior may be poor.
| The default active space for single excitations is all M.O.s. The
  number of excitations included in the CI matrix is controlled by
  ```MAXCI`` <MAXCI.html>`__, so it is possible to generate a large
  number of single excitations within an active space of hundreds of
  M.O.s.
| Within INDO, the active space indicated by the ``C.I.`` keyword
  applies only to single excitations; if ``CISD`` is specified, the
  active space for double excitations must be specified by
  ```C.I.D`` <C.I.D.html>`__. The configurations are automatically
  spin-adapted, so only electron configurations of a single spin are
  included. By default, only configurations with the lowest possible
  spin are included (singlet for a closed-shell system or doublet for an
  odd-electron system). Higher spins can be selected using
  ```TRIPLET`` <triplet.html>`__ or ```QUARTET`` <quartet.html>`__.

 

See also: ``C.A.S., C.I.D., MAXCI, MRCI, TDIP,  WRTCI``, and
``WRTCONF``.

 
