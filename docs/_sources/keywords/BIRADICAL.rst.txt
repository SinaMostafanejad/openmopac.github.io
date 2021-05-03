.. _BIRADICAL:

``BIRADICAL``
=============

Note: ``BIRADICAL`` is a redundant keyword, and represents a particular
configuration interaction calculation. Experienced users of
`MECI <Multi_Electron_Configuration_Interaction.html>`__ can duplicate
the effect of the keyword ``BIRADICAL`` by using the MECI keywords
`OPEN(2,2) <open.html>`__ and `SINGLET <singlet.html>`__.

````

BIRADICAL is limited to restricted Hartree Fock systems, so
```UHF`` <uhf.html>`__ should not be present.

For molecules which are believed to have biradicaloid character, the
option exists to optimize the lowest singlet energy state which results
from the mixing of four microstates. These microstates are, in order:
the microstate arising from a one electron excitation from the HOMO to
the LUMO (Microstate 1 in the Figure); the microstate resulting from the
  time-reversal operator acting on the parent microstate (Microstate 2);
the microstate resulting from de-excitation from the formal LUMO to the
HOMO (Microstate 3); and the microstate resulting from the single
electron in the formal HOMO being excited into the LUMO (Microstate 4).
Microstates 1 and 2 mix to form a singlet
state,(1/2)\ :sup:`1/2`\ (Ψ:sub:`1`-Ψ:sub:`2`) , and a triplet state
(1/2):sup:`1/2`\ (Ψ:sub:`1`\ +Ψ\ :sub:`2`). Microstates 3 and 4 are true
singlet states. The singlet state arising from microstates 1 and 2 mixes
with the (micro)states 3 and 4 to form three singlet states.

| 

.. raw:: html

   <div align="CENTER">

  
Figure: Configurations used in ``BIRADICAL`` Calculation

+-----------------------------------------------------------------------+
| .. raw:: html                                                         |
|                                                                       |
|    <div align="CENTER">                                               |
|                                                                       |
| |includegraphics{picbirad}|                                           |
|                                                                       |
| .. raw:: html                                                         |
|                                                                       |
|    </div>                                                             |
+-----------------------------------------------------------------------+

.. raw:: html

   </div>

| 
| A configuration interaction calculation is involved here. A biradical
  calculation done without C.I. at the RHF level would be meaningless. 
  Either rotational invariance would be lost, as in the D\ :sub:`2\ d`
  form of ethylene, or very artificial barriers to rotations would be
  found, such as in a methane molecule "orbiting" a D\ :sub:`2\ d`
  ethylene. In both cases the inclusion of limited configuration
  interaction corrects the error. ``BIRADICAL`` should not be used if
  either the HOMO or LUMO is degenerate; in this case, the full manifold
  of HOMO \*LUMO should be included in the C.I., using MECI options. The
  user should be aware of this situation. When the biradical calculation
  is performed correctly, the result is normally a net stabilization.
  However, if the first singlet excited state is much higher in energy
  than the closed-shell ground state, ``BIRADICAL``\ can lead to a
  destabilization. Abbreviation: ``BIR``

.. |includegraphics{picbirad}| image:: img102.gif
   :width: 571px
   :height: 198px
