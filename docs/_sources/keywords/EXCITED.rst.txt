.. _EXCITED:

``EXCITED``
===========

The state to be calculated is the first excited open-shell singlet
state. If the ground state is a singlet, then the state calculated will
be S(1); if the ground state is a triplet, then S(2). This state would
normally be the state resulting from a one-electron excitation from the
HOMO to the LUMO. Exceptions would be if the lowest singlet state were a
biradical, in which case the EXCITED state could be a closed shell.

````

EXCITED is limited to restricted Hartree Fock systems, so
```UHF`` <uhf.html>`__ should not be present.

The ``EXCITED`` state will be calculated from a
`BIRADICAL <biradical.html>`__ calculation in which the second root of
the C.I. matrix is selected. Abbreviation: ``EXCI``.

Note: ``EXCITED`` is a redundant keyword, and represents a particular
configuration interaction calculation. Experienced users of MECI can
duplicate the effect of the keyword ``EXCITED`` by using the MECI
keywords `OPEN(2,2) <open.html>`__, `SINGLET <singlet.html>`__, and
`ROOT=2 <root.html>`__.
