.. _UHF:

``UHF``
=======

The unrestricted Hartree-Fock Hamiltonian is to be used.

This is the default for odd-electron (radical) systems because geometry
optimization using UHF runs faster than when ``RHF`` is used.  This is
because the open-shell RHF gradient calculation is relatively slow.

If UHF methods are to be used on even electron systems, add keyword
``UHF``.

A limitation of the ``UHF`` method is that the resulting wavefunction is
not spin quantized, that is, although <S:sub:`z`> has a  well-defined
value, e.g. 0, 1/2, 1, 3/2, etc., <S:sup:`2`> is normally not
quantized.  For a system with an <S:sub:`z`> of 1/2, the <S:sup:`2`>
should be 3/4 = 1/2*(1/2+1), but is usually higher.  This is a
consequence of spin contamination.  Spin contamination is not present if
``UHF`` is not used.
