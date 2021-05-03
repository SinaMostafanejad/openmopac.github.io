.. _ENPART:

``ENPART``

This is a very useful tool for analyzing the energy terms within a
system. The total energy, in eV, obtained by the addition of the
electronic and nuclear terms, is partitioned into mono- and bi-centric
contributions (if ```LARGE`` <large.html>`__ is present), and these
contributions in turn are divided into nuclear and one- and two-electron
terms (if ```LARGE`` <large.html>`__ is present). 

Atoms can be grouped into sets, up to 9 sets are allowed.  The format is
ENPART(n1, n2,n3...) where n1, n2, n3, etc., are the number of atoms in
each set.  All atoms in each set must be together in the geometry file. 
For example, to do an energy partition on the water molecule, use atoms
O, H, H, O, H, H, and use ENPART(3,3).  In this, the first three atoms
are the first water molecule.

Here is an example of energy partitioning for the HF dimer.  In order to
work out the HF - HF interaction energy, keyword ENPART(2,2) was used.

::

             TOTAL ENERGY PARTITIONING

             ALL ENERGIES ARE IN ELECTRON VOLTS

               ONE-CENTER TERMS 
             E-E:  ELECTRON-ELECTRON REPULSION
             E-N:  ELECTRON-NUCLEAR ATTRACTION


    
    ATOM      E-E       E-N    (E-E + E-N)
      F   1   333.3949 -800.5397 -467.1449  
      H   2     1.8754   -8.1040   -6.2286
      F   3   333.3956 -800.5406 -467.1450
      H   4     1.8754   -8.1039   -6.2285
      
      



   The one-center energy of each atom is in the column (E-E + E-N) 
   Unless you're REALLY interested in it, the component parts, E-E and E-N, are not useful.  


                 TWO-CENTER TERMS
              
             J:   RESONANCE ENERGY          E-E: ELECTRON-ELECTRON REPULSION
             K:   EXCHANGE ENERGY           E-N: ELECTRON-NUCLEAR ATTRACTION
                                            N-N: NUCLEAR-NUCLEAR REPULSION
             C:   COULOMBIC INTERACTION = E-E + E-N + N-N
             EE:  TOTAL OF ELECTRONIC AND NUCLEAR ENERGIES

        ATOM          J        K       E-E       E-N      N-N      C        EE
        PAIR
    
     H   2  F   1  -12.1007  -4.8374  51.3351 -121.4430  75.1795  5.0717 -11.8664
    
     F   3  F   1    0.0000  -0.0002 223.2326 -429.5659 206.6544  0.3210   0.3208
     F   3  H   2   -0.0012  -0.0001  23.5576  -55.3454  31.4388 -0.3490  -0.3503
    
     H   4  F   1   -0.0012  -0.0001  23.5496  -55.3269  31.4284 -0.3489  -0.3502
     H   4  H   2   -0.0015  -0.0001   2.2758   -6.3168   4.3835  0.3425   0.3409
     H   4  F   3  -12.0999  -4.8372  51.3339 -121.4406  75.1776  5.0709 -11.8662
     
    
               System is to be split into 2 parts
                   Part No. of atoms     Atoms
                     1       2         1 to   2
                     2       2         3 to   4        
    Part 1 self - energy (ONE-CENTER(E-E + E-N) + EE):          -485.2398 
    Part 2 self - energy (ONE-CENTER(E-E + E-N) + EE):          -485.2398 
    Part 2 - part 1 interaction energy (EE):                      -0.0388 Note on interaction energies






   The two-center energies of each atom pair is in the column EE.
   Unless you're REALLY interested in it, the component parts are not useful.  

   Energy of the first HF = one-center energy of F 1 (-467.145) + 
   one-center energy of H 2 (-6.229) + two-center energy of H 2 - F 1 interaction (-11.866)  
   Energy of the second HF = one-center energy of F 3 (-467.145) + 
   one-center energy of H 4 (-6.229) + two-center energy of H 4 - F 3 interaction (-11.866)  
   Energy of interaction of the first HF with the second HF = two-center energies of F 3 - F 1 - H interaction (0.321) 
   +  F 3 - H 2 (-0.350) + H 4 - F 1 (-0.350) + H 4 - H 2 (0.341) = -0.039eV 
   TOTAL OF ONE-CENTER TERMS = ELECTRON-NUCLEAR  (ONE-ELECTRON) + ELECTRON-ELECTRON (TWO-ELECTRON) 
   TOTAL ELECTROSTATIC INTERACTION =  ELECTRON-ELECTRON REPULSION + ELECTRON-NUCLEAR ATTRACTION + 
   NUCLEAR-NUCLEAR REPULSION 
   GRAND TOTAL OF TWO-CENTER TERMS =  (EXCHANGE + RESONANCE ENERGY) + TOTAL ELECTROSTATIC INTERACTION 
   ETOT (EONE + ETWO) = TOTAL OF ONE-CENTER TERMS + GRAND TOTAL OF TWO-CENTER TERMS
    = TOTAL ENERGY just after FINAL HEAT OF FORMATION in output  


   ***  SUMMARY OF ENERGY PARTITION  ***
    ---------------------------------------
        ONE-CENTER TERMS

    ELECTRON-NUCLEAR  (ONE-ELECTRON)        -1617.2882 EV
    ELECTRON-ELECTRON (TWO-ELECTRON)          670.5412 EV

    TOTAL OF ONE-CENTER TERMS                -946.7470 EV 
    ---------------------------------------
        TWO-CENTER TERMS

    RESONANCE ENERGY                          -24.2044 EV
    EXCHANGE ENERGY                            -9.6751 EV

    EXCHANGE + RESONANCE ENERGY:              -33.8795 EV

    ELECTRON-ELECTRON REPULSION               375.2846 EV
    ELECTRON-NUCLEAR ATTRACTION              -789.4387 EV
    NUCLEAR-NUCLEAR REPULSION                 424.2622 EV

    TOTAL ELECTROSTATIC INTERACTION            10.1081 EV 

    GRAND TOTAL OF TWO-CENTER TERMS           -23.7714 EV 
    ---------------------------------------
    ETOT (EONE + ETWO)                       -970.5184 EV
