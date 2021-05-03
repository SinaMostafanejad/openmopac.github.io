.. _ESR:

``ESR``
=======

The unpaired spin density arising from an odd-electron system can be
calculated both RHF and UHF. In a UHF calculation the alpha and beta
M.O.s have different spatial forms, so spin density can naturally be
present on in-plane hydrogen atoms such as in the phenoxy radical.

In the RHF formalism a MECI calculation is performed. In general,
``ESR`` can be used for *any* system for which M\ |$_S \\neq 0$|. If the
C.I. calculation results in many states, then the spin density for the
state requested and the next few states will be printed. For example, if
benzene cation, D\ :sub:`6\ h`, is calculated, using ``ESR OPEN(3,2)``,
then the spin density for the two degenerate components of
E\ :sub:`1\ g` will be printed. For this system, the total spin density
on any given atomic orbital or any atom is given by the *average* of the
spin densities for the two components. For benzene\ :sup:`+`, this would
be 1/6 electrons.

Thus, for example, for ethylene, ``ESR TRIPLET C.I.=2`` would give
meaningful results, as would ``ESR MS=1 C.I.=2``. However,
``ESR ROOT=2 C.I.=2`` would not, as this would be used to calculate the
spin density arising from the M\ :sub:`S` = 0component of a triplet
state, which will have a zero spin density.

Spin density for state **Ψ**\ :sub:`j`, calculated as spin, S\ :sub:`A`,
on atom A, is given in terms of contributions from the M.O.s of the
active space *ψ*\ :sub:`i`, *ψ*\ :sub:`i` = Σ\ :sub:`λi`\ *φ* as:

S\ :sub:`A` =
Σ\ :sub:`λ`\ :sup:`A`\ *φ*\ :sub:`λi`\ :sup:`2`\ Σ\ :sub:`i`\ S\ :sub:`i`,

where the S\ :sub:`i` are the contributions of spin from each M.O., 
expressed as a sum over the microstates of the C.I., **Ψ**\ :sub:`j` =
Σc\ :sub:`kj`\ Ψ\ :sub:`j`, :

S\ :sub:`i` =
Σ\ :sub:`k`\ (O:sub:`i`\ :sup:`αk`-O:sub:`i`\ :sup:`βk`)c\ :sub:`kj,`

Where O\ :sub:`i`\ :sup:`αj` is the alpha or "spin up" occupancy of M.O.
*ψ*\ :sub:`i`, in microstate Ψj. Although φ\ :sub:`λi`\ :sup:`2` is
obligate positive, S\ :sub:`i` can be positive or negative, therefore
S\ :sub:`A` can be positive or negative, although it is unlikely to be
very negative, and the sum over all atoms must equal
2\ *M*\ :sub:`S`\ (Z)

If the keywords ``OPEN`` and ``C.I.=`` are both absent, then only a
single state is calculated. The spin density is then calculated from the
state function. In order to have spin density on the hydrogens in, for
example, the phenoxy radical, several states should be mixed.

.. |$_S \\neq 0$| image:: img115.gif
   :width: 38px
   :height: 30px
