.. _XYZ:

``XYZ``
=======

Regardless of the coordinate system used in defining the geometry, if
``XYZ`` is present, then all atoms will be converted to Cartesian
coordinates, and the calculation will be run entirely in Cartesian
coordinates.

When a system involving several rings, or big rings, is optimized using
internal coordinates, the geometry optimizers often have difficulty. 
This is because the effect of a small change in an angle can be a large
change in the interatomic distance of two bonded atoms.  This is
particularly important in enzymes and other large molecules.  This
problem is completely solved if Cartesian coordinates are used. 
Therefore, if problems are encountered with geometry optimizations,
particularly if internal coordinates are used, keyword ``XYZ`` should be
used.

Notes

-  If  ``XYZ`` is used, the optimization flags are not changed.
   Therefore, before running a system with  ``XYZ`` all the optimization
   flags should be set to "1". For atoms 1, 2, and 3, the optimization
   flags are forced to 1 if all the other optimization flags are set to
   1.  To be safe, use ``XYZ`` with ``0SCF``, then edit the resulting
   ARC file to delete ``XYZ`` and set the optimization flags by hand.
-  Be very careful if some atoms have optimization flags set to"0".  If
   the geometry supplied is in internal coordinates, and an atom, say
   atom 10, has all three optimization flags set to "0", then that means
   "Do not change the bond length, angle, and dihedral of atom 10, with
   reference to the atoms used for the connectivity."  The atom can
   still move if the atom it is attached to moves.  If that atom is
   converted to Cartesian coordinates, the optimization flags will still
   be zero, but now the definition changes to "Do not change the
   Cartesian coordinates of atom 10."  This is very different from the
   internal coordinate definition.
-  Any dummy atoms are automatically deleted if  ``XYZ`` is present. 
   Dummy atoms are only meaningful if internal coordinates are used. 

See also ```INT`` <int.html>`__
