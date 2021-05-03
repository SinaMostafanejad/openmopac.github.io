.. _LEWIS:

``LEWIS``
=========

Print the topography and Lewis structure.  When ``LEWIS`` is present,
the run is stopped after the structure is printed.

This keyword is useful for checking that a Lewis structure exists. 
Quite complicated systems can be supplied, such as buckyball
(C:sub:`60`), carbon nanotube (buckytube), graphite, phthalocyanines,
and diamond.

A Lewis structure consists of single, double and triple bonds, lone
pairs, anionic and cationic sites, and positively and negatively charged
atoms (ions).  The method used in MOPAC is quite powerful, and except
for rare cases, gives a reasonable structure.  The exceptions are:

-  In buckytubes, the assumption is made that a graphitic lattice,
   rather than an extended conjugated poly-acetylene type π bonding
   structure exists. In some cases, the only unionized structure
   involves using an extended conjugated poly-acetylene motif.

-  (To be added, as necessary)

When large organic molecules are being studied, a preliminary
calculation to generate the Lewis structure should be run before doing
serious work.  This will identify all ionized sites in the system.
* Check that these sites are correct!*  See also ``CHARGES``

If only the topography is important, then also add keyword ``0SCF.``
This will stop the run after the topography, but before the Lewis
structure is printed. This option is useful when using  keyword 
``CVB``\ to correct faults in the topology\ ``.``

| Related key-words: 
  ``CVB, METAL, VDWM, CHARGE, CHARGES, SETPI``,\ ``and MOZYME``
| See also: `Lewis Structures <Lewis_structures.html>`__, `MOZYME
  introduction <mozyme_introduction.html>`__,  `Lewis metal atom
  charges <Lewis_Metal_Charges.html>`__

.. raw:: html

   <div align="left">

 

.. raw:: html

   </div>

 

 

 
