.. _INT:

``INT``
=======

Regardless of what type of coordinates are used in the data set, ``INT``
will force all the coordinates to be internal coordinates. Atom 1 is, by
definition, always defined in Cartesian coordinates.

Notes

-  If  ``INT`` is used, the optimization flags are not changed.
   Therefore, before running a system with \ ``INT`` all the
   optimization flags should be set to "1", except for atoms 1, 2, and
   3. For atom 1, all optimization flags should be set to "0", for atom
   2, the second and third flags should be "0", and for atom 3 the third
   flag should be "0".
-  Be very careful if some atoms have optimization flags set to "0".  If
   the geometry supplied is in Cartesian coordinates, and an atom, say
   atom 10, has all three optimization flags set to "0", then that means
   "Do not change the Cartesian coordinates of atom 10."   If that atom
   is converted to internal coordinates, the optimization flags will
   still be zero, but now the definition changes to "Do not change the
   bond length, angle, and dihedral of atom 10, with reference to the
   atoms used for the connectivity."  Now atom 10 will move if the atom
   it is attached to moves. This is fundamentally different from the
   Cartesian coordinate definition.
-  Any dummy atoms are automatically deleted if ``INT`` is present. 
   This is because the first step in running ``INT`` is to convert the
   system to Cartesian coordinates.  This involved deleting any dummy
   atoms.  The next step involves conversion from Cartesian to internal
   coordinates.
-   ``INT`` is a rapid and efficient way of deleting atoms from a
   molecule that is defined using internal coordinates.  Re-label the
   atoms to be deleted as dummy atoms, and run ``INT`` with ``0SCF.``

See also ``XYZ.``
