.. _MRCI:

``MRCI``
========

Available for ```INDO`` <indo.html>`__-based CI calculations only. Use
multi-reference configuration interaction. The references for MRCI can
be selected using the C.A.S. keyword; by default, the active space is
two M.O.s. If ``CIS`` or ```CISD`` <cisd.html>`__ is not specified, CIS
is assumed.

 

Multi-reference CI is useful for generating specific double and higher
excitations. Within multi-reference CI, the reference determinants are
used as starting points for generating single excitations (or single and
double excitations, if CISD is specified). For a closed-shell system
using the default active space, the reference determinants are:

1.     The SCF ground state

1.     A single (HOMO → LUMO) excitation

2.     A double (HOMO, HOMO → LUMO, LUMO) excitation

The single excitation (HOMO – x → LUMO + y) starting from reference
determinant 1 will yield a single excitation, as in CIS. The same
excitation starting from reference determinant 2 will yield the double
excitation (HOMO – x, HOMO → LUMO, LUMO + y). Similarly, the same
excitation starting from reference determinant 3 will yield the triple
excitation (HOMO – x, HOMO, HOMO → LUMO, LUMO, LUMO + y).

 

 

 
