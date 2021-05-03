.. _METAL:

``METAL[=(a[,b[,c[...]]])]``
============================

 

When adding hydrogen atoms using ```ADD-H`` <ADD-H.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All atoms defined as metals are assumed to be 100% ionic.  As a result,
oxygen and sulfur atoms near to a metal atom will be automatically
ionized.  This can produce structures such as -CH:sub:`2`-COO(-) ...
Na(+) and -CH:sub:`2`-COO(-) ... Ca(+2).

In Lewis structures for MOZYME calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some elements might need to be defined as not having any covalent bonds
when building the `Lewis structure <Lewis_structures.html>`__.  This can
be in order to generate a sensible Lewis structure for the user or, in
rare instances, to generate an acceptable Lewis structure for MOZYME.

Consider ferrocene.  In ferrocene, iron has 8 valence electrons, so if
it is allowed to bond to the carbon atoms, it would form 8 covalent
sigma bonds.  In such a system, iron would thus be Fe(VIII).  In a zinc
finger, if Zn bonds to the four ligands, it would have a formal charge
of -2.  Such unusual oxidation states or charges might be of concern to
users, however in most cases they would not affect the MOZYME
calculation. 

Individual elements and individual atoms can be re-defined as not
forming any covalent bonds by use of METAL.  In building Lewis
structures, all elements of Groups I and II are considered as being
fully ionic.  If they need to be considered as covalent, use ``CVB`` to
define bonds.

The oxidation state can be changed using METAL by adding the new
oxidation state immediately after the chemical symbol.  The new
oxidation state must be in the specific form +n, 0 or -n, so, for
example [Sc:sup:`I`]\ :sup:`+` would be Sc(+1).  Note that the "+1" is
needed, and that Sc(+), without the "1" would not be allowed.

Individual elements are specified by their chemical symbol, individual
atoms are specified by the atom-number of the real atom (Real atoms
numbers exclude any dummy atoms), or by the PDB or JSmol labels.

By default, elements of Group IA (Li, Na, K, Rb, Cs) and some of Group
IIA (Mg, Ca, Sr, Ba) are considered metals.

**Examples**

+-----------------------+-----------------------+-----------------------+
| METAL                 |                       | All metal atoms are   |
|                       |                       | re-defined as being   |
|                       |                       | 100% ionic            |
+-----------------------+-----------------------+-----------------------+
| METAL=(Fe)            |                       | Re-define all iron    |
|                       |                       | atoms are being 100%  |
|                       |                       | ionic                 |
+-----------------------+-----------------------+-----------------------+
| METAL=(Au(+3))        |                       | Re-define gold atoms  |
|                       |                       | as being 100% ionic   |
|                       |                       | and in oxidation      |
|                       |                       | state +3 (Used by     |
|                       |                       | MOZYME only).         |
+-----------------------+-----------------------+-----------------------+
| METAL=(Fe,Zn)         |                       | Re-define all iron    |
|                       |                       | and zinc atoms are    |
|                       |                       | being 100% ionic      |
+-----------------------+-----------------------+-----------------------+
| METAL=(3423)          |                       | Re-define atom 3423   |
|                       |                       | as being 100% ionic   |
+-----------------------+-----------------------+-----------------------+
| METAL=(Zn,6222)       |                       | Re-define all zinc    |
|                       |                       | atoms and atom 6222   |
|                       |                       | as being 100% ionic   |
+-----------------------+-----------------------+-----------------------+
| METAL=(Zn,"O GLY A    |                       | Re-define all zinc    |
| 1")                   |                       | atoms and the atom    |
|                       |                       | with PDB label "O GLY |
|                       |                       | A 1" as being 100%    |
|                       |                       | ionic                 |
+-----------------------+-----------------------+-----------------------+
| METAL=(22,54)         |                       | Re-define atoms 22    |
|                       |                       | and 55 as being 100%  |
|                       |                       | ionic                 |
+-----------------------+-----------------------+-----------------------+

| Related key-words:  ``LEWIS,  CVB, VDWM, CHARGE, CHARGES, and MOZYME``
| See also: `Lewis Structures <Lewis_structures.html>`__, `MOZYME
  introduction <mozyme_introduction.html>`__,  `Lewis metal atom
  charges <Lewis_Metal_Charges.html>`__

.. raw:: html

   <div align="left">

 

.. raw:: html

   </div>
