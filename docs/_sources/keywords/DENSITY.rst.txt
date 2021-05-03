.. _DENSITY:

``DENSITY``
===========

At the end of a MOPAC job, when results are being printed, the density
matrix is also printed. For RHF the normal density matrix is printed.
For UHF the sum of the alpha and beta density matrices is printed.

If density is not requested, then the diagonal of the density matrix,
i.e., the electron density on the atomic orbitals, will be printed.

Excited state density matrices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an excited state is calculated using the MECI method (see
Multi-Electron Configuration Interaction method in
`Theory <theory.html>`__) the corresponding density matrix is
constructed.  Keywords that cause MECI to be used are
```C.I.=text`` <ci=nm.html>`__, ```OPEN`` <open.html>`__,
```EXCITED`` <excited.html>`__,  and ```MICROS`` <micros.html>`__. When
``DENSITY`` is present, the excited state density matrix is printed. 
The excited state used in constructing the density matrix is indicated
in the MECI output by a "+" sign next to the state number in the list of
state energies (state energies are printed when keyword
```MECI`` <meci.html>`__ is present)  For transition dipoles or
`oscillator strength <oscillator_strength.html>`__, also see the
polarization values in the ``MECI`` output.
