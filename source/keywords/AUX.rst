.. _AUX:

``AUX[([n][,][COMP][,][PRECISION=m][,][MOS=n][,][XP][,][XS][,][XW])]``
======================================================================

| When ``AUX`` is used then auxiliary information is output to a file
  called <file>.aux.  When ``AUX``\ (*n*) is used, output for the
  changing geometry is re-directed to output channel *n, n* is limited
  to the range 0 - 99. Thus ``AUX``\ (6) would re-direct the changing
  geometry to standard output unit 6. Useful values are *n* = 0 and *n*
  = 6. Avoid using units 2 to 4, and 9 to 30, as these are used by
  MOPAC. The <file>.aux  files are intended for use by Graphical User
  Interfaces (GUI's), but the files can be converted using a simple
  Windows utility, `Read_AUX <../Downloads/Read_AUX.zip>`__, into ASCII
  tables for use by programs such as EXCEL.
| AUX is supported by Avogadro, Gabedit, and Molden.
| When ``COMP`` is present, all large blocks of data are printed in
  compressed form. 
| To increase precision by *m* digits (*m* limited to the range 1 to 9),
  use ``PRECISION=m``.
| By default, only the 10 highest occupied  and 10 lowest unoccupied
  M.O.s are printed, unless ``LARGE`` is present, in which case all
  M.O.s are printed To change the default, use ``MOS=n``, where *n* is
  the number of occupied and virtual M.O.s to be printed.  If *n* is
  greater than the number of M.O.s, it will be re-set to all the M.O.s,
  so an alternative way to print all the M.O.s is to use ``MOS=99999``.
  To prevent printing of M.O.'s, use ``MOS=-99999``.
| The commas are optional.
| If the re-direction unit "*n*" is used together with any of COMP,
  PRECISION, or MOS, then "*n*" must come first, followed by the other
  options.
| For large systems, the AUX file might still be very large, even if
  COMP is used.  To reduce the size of the AUX file, use one or more of
  the following options:
| If XP is present, the density matrix will not be printed.
| If XS is present, the overlap matrix will not be printed.
| If XW is present, the M.O.s will not be printed.  This is an
  alternative to ``MOS=-99999``.

Only data considered to be important to GUI programs will be included in
the .aux file.  A consequence of this is that some data might be
missing.  If such data can be identified, and a message sent to
MrMOPAC@ATT.net, then the data will be added to the .aux file.

| The auxiliary information is a very compact form of the results of a
  calculation in a primitive mark-up language. This file is intended for
  use by other programs. An example of the auxiliary file for water is
  given below.  No explanation is necessary: the file is intended to be
  self-descriptive.
|   START OF MOPAC FILE
|  ####################################
|  #                                  #
|  #       Start of Input data        #
|  #                                  #
|  ####################################
|  MOPAC_VERSION=MOPAC2007.7.150W
|  DATE="Mon Jun  4 12:15:37 2007"
|  METHOD=PM6
|  TITLE=" Water"
|  KEYWORDS=" SYMMETRY"
|  ATOM_EL[0003]=
|   O  H  H
|  ATOM_X:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.6018    0.7647    0.0000
|     0.6018   -0.7647    0.0000
|  AO_ATOMINDEX[0006]=
|   1  1  1  1  2  3
|  ATOM_SYMTYPE[0006]=
|   S PX PY PZ  S  S
|  AO_ZETA[0006]=
|   5.4218  2.2710  2.2710  2.2710  1.2686  1.2686
|  ATOM_PQN[0006]=
|  2 2 2 2 1 1
|  NUM_ELECTRONS=0008
|  EMPIRICAL_FORMULA="H2 O"
|  ####################################
|  #                                  #
|  #      Geometry optimization       #
|  #                                  #
|  ####################################
|  HEAT_OF_FORM_UPDATED:KCAL/MOL=-0.540108D+02
|  GRADIENT_UPDATED:KCAL/MOL/ANG=+0.210682D+02
|  ATOM_X_UPDATED:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.6018    0.7647    0.0000
|     0.6018   -0.7647    0.0000
|  HEAT_OF_FORM_UPDATED:KCAL/MOL=-0.542600D+02
|  GRADIENT_UPDATED:KCAL/MOL/ANG=+0.893385D+01
|  ATOM_X_UPDATED:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.5693    0.7558    0.0000
|     0.5693   -0.7558    0.0000
|  HEAT_OF_FORM_UPDATED:KCAL/MOL=-0.543026D+02
|  GRADIENT_UPDATED:KCAL/MOL/ANG=+0.225094D+01
|  ATOM_X_UPDATED:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.5641    0.7630    0.0000
|     0.5641   -0.7630    0.0000
|  HEAT_OF_FORM_UPDATED:KCAL/MOL=-0.543063D+02
|  GRADIENT_UPDATED:KCAL/MOL/ANG=+0.144932D+00
|  ATOM_X_UPDATED:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.5610    0.7655    0.0000
|     0.5610   -0.7655    0.0000
|  ####################################
|  #                                  #
|  #        Final SCF results         #
|  #                                  #
|  ####################################
|  HEAT_OF_FORMATION:KCAL/MOL=-0.543063D+02
|  ENERGY_ELECTRONIC:EV=-0.458386D+03
|  ENERGY_NUCLEAR:EV=+0.139308D+03
|  POINT_GROUP=C2v
|  DIPOLE:DEBYE=+0.206870D+01
|  AREA:SQUARE ANGSTROMS=+0.424512D+02
|  VOLUME:CUBIC ANGSTROMS=+0.251444D+02
|  ATOM_X_OPT:ANGSTROMS[0009]=
|     0.0000    0.0000    0.0000
|     0.5610    0.7655    0.0000
|     0.5610   -0.7655    0.0000
|  ATOM_CHARGES[0003]=
|  -0.61867 +0.30933 +0.30933
|  OVERLAP_MATRIX[000021]=
|  #  Lower half triangle only
|    1.0000   0.0000   1.0000   0.0000   0.0000   1.0000   0.0000  
  0.0000   0.0000   1.0000
|    0.1618   0.2330   0.3180   0.0000   1.0000   0.1618   0.2330 
  -0.3180   0.0000   0.2333
|    1.0000
|  EIGENVECTORS[000036]=
|   -0.8288  -0.2451   0.0000   0.0000  -0.3556  -0.3556   0.0000  
  0.0000   0.8129   0.0000
|    0.4118  -0.4118   0.4394  -0.8417   0.0000   0.0000  -0.2220 
  -0.2220   0.0000   0.0000
|    0.0000   1.0000   0.0000   0.0000   0.3463   0.4812   0.0000  
  0.0000  -0.5694  -0.5694
|    0.0000   0.0000   0.5824   0.0000  -0.5748   0.5748
|  TOTAL_DENSITY_MATRIX[000021]=
|  #  Lower half triangle only
|    1.7601  -0.3333   1.5370   0.0000   0.0000   1.3216   0.0000  
  0.0000   0.0000   2.0000
|    0.3944   0.5480   0.6695   0.0000   0.6907   0.3944   0.5480 
  -0.6695   0.0000   0.0123
|    0.6907
|  M.O.SYMMETRY_LABELS[0006]=
|   1a1     1b2     2a1     1b1     3a1     2b2 
|  EIGENVALUES[0006]=
|   -30.402  -18.983  -14.111  -11.905    4.067    6.038
|  MOLECULAR_ORBITAL_OCCUPANCIES[00006]=
|  2.0000 2.0000 2.0000 2.0000 0.0000 0.0000

| When ``COMP`` is present, the overlap and density matrices, and
  eigenvectors, are printed in compressed form.
| Compare the previous uncompressed data with the following compressed
  data to see how the compression is done.

::

    OVERLAP_INDICES[013]=
        1     3     6    10    15    21    18    13    20    17    12    16    11
    OVERLAP_COEFFICIENTS[013]=
      1.0000   1.0000   1.0000   1.0000   1.0000   1.0000  -0.3180   0.3180   0.2336   0.2332
      0.2332   0.1619   0.1618
    SET_OF_MOS=       1       6
    MO_INDICES[004]=
        1     6     5     2
    MO_COEFFICIENTS[004]=
      0.8287   0.3558   0.3557   0.2452
    MO_INDICES[003]=
        3     5     6
    MO_COEFFICIENTS[003]=
      0.8129   0.4118  -0.4118
    MO_INDICES[004]=
        2     1     5     6
    MO_COEFFICIENTS[004]=
      0.8416  -0.4396   0.2219   0.2219
    MO_INDICES[001]=
        4
    MO_COEFFICIENTS[001]=
      1.0000
    MO_INDICES[004]=
        5     6     2     1
    MO_COEFFICIENTS[004]=
      0.5694   0.5693  -0.4812  -0.3465
    MO_INDICES[003]=
        3     6     5
    MO_COEFFICIENTS[003]=
      0.5824   0.5749  -0.5748
    DENSITY_MATRIX_INDICES[014]=
       10     1     3     6    21    15    13    18    12    17    16    11     2    20
    DENSITY_MATRIX_COEFFICIENTS[014]=
      2.0000   1.7599   1.5369   1.3217   0.6908   0.6908   0.6695  -0.6695   0.5480   0.5480
      0.3945   0.3945  -0.3334   0.0124

::

   When COMP and MOS are present, a user-defined set of M.O.s is printed.  The default is the 10 highest M.O.s and 10 lowest virtual M.O.s.
   If LARGE is present, all the M.O.s are printed.
      
