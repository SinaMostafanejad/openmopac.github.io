.. _CHARGES:

``CHARGES``
===========

When ``CHARGES`` is present, all ionized sites in the system will be
identified and printed.  The run will then be stopped.  This operation
is useful during the preparation of a data set, in that it is very easy
for even experienced users to have incorrect charges on large systems,
particularly complicated organic species such as enzymes and
organometallics.

The method for identifying charged atoms is very powerful.  So although
you might be quite certain that you have the charges correct, if
``CHARGES`` indicates that you have made a mistake, please check the
system using the information printed.  In 100% of the cases where users
have complained that MOPAC reported faulty charges, ``CHARGES``
identified errors in the user's structure.

In MOPAC, many common Lewis structures involve hypervalent systems being
represented as ions.  Thus the sulfur atom in sulfuric acid would be
represented as S\ :sup:`+` and there would be a counter-charge of
O\ :sup:`-`.  Be aware that during a geometry optimization "`salt
bridges <salt_bridges.html>`__" can form, e.g. -COOH :sup:`...` 
H\ :sub:`2`\ N-  can convert to -[COO]:sup:`-` :sup:`...` 
[H:sub:`2`\ N]\ :sup:`+`-. Such structures should *not* be regarded as
faults. Also, metal ions might be reported as having an unexpected
charge, thus Zn with four oxygen atoms as ligands might be reported as
[Zn]:sup:`2-`. If this causes any concern, add keyword
`METAL <metal.html>`__, and all bonds to metal ions will be broken, so
for example Zn with four ligands would be reported as [Zn]:sup:`2+` and
all four ligands would each acquire a negative charge.

The choice of which nitrogen atoms in the heterocycle in histidine have
attached hydrogen atoms is often not immediately obvious.  But in many
cases, the choice is important - the wrong choice will always result in
a high-energy structure, and be accompanied by severe rotation of the
heterocycle, as it tries to relieve the stress.  ``CHARGES`` cannot help
with identifying the right choice.

| Related key-words:  ``LEWIS,  CVB, METAL, VDWM, CHARGE, and MOZYME``
| See also: `Lewis Structures <Lewis_structures.html>`__, `MOZYME
  introduction <mozyme_introduction.html>`__

.. raw:: html

   <div align="left">

 

.. raw:: html

   </div>
