.. _VDWM:

``VDWM(text)``
==============

In ```MOZYME`` <mozyme.html>`__,  the
```LEWIS`` <Lewis_structures.html>`__ structure is constructed from the
topology of the system.  Atoms are considered to be connected if they
are within 10% of the addition of the two radii, or within twice the
heavy-atom radius if one of the atoms is hydrogen.  Values for all radii
used are shown in the Table below.

The criterion of whether atoms are connected or not can be changed by
modifying the radii. using the ``VDWM`` keyword.   The format of the
command is:

````

VDWM(<chemical symbol\ :sub:`1`>=\ *n*.\ *nn*;<chemical
symbol\ :sub:`2`>=\ *n*.\ *nn*;<chemical
symbol\ :sub:`3`>=\ *n*.\ *nn;*...)

For example, if a hydrogen atom should be regarded as connected to a
nitrogen, but the N-H distance is 1.62 Angstroms, then ``VDWM(N=0.85)``
would override the default values of the van der Waals radii of nitrogen
(0.75), and result in the hydrogen being connected (the N-H distance of
1.62 being less than 2*0.85).

If a fluorine atom should be connected to a bromine, but the F-Br
distance is 2.1 Angstroms, i.e., it is too large for the two atoms to be
regarded as being connected (2.1 > 1.1(0.71 + 1.14), then either the F
radius, or the Br radius, or both, could be increased.  One possible
change would be to use keyword ``VDWM(F=0.75;Br=1.2)``

Entries for different elements should be separated by a colon, a comma,
or a semi-colon.

** Table 1:** Default radii (Angstroms) used in MOZYME

I

II

Transition Metals

 

 

III

IV

V

VI

VII

VIII

H

0.37

 

 

He

0.32

Li

1.34

Be

0.90

B

0.82

C

0.77

N

0.75

O

0.73

F

0.71

Ne

0.69

Na

1.54

Mg

1.30

Al

1.18

Si

1.11

P

1.06

S

1.02

Cl

0.99

Ar

0.97

K

1.96

Ca

1.74

Sc

1.44

Ti

1.36

V

1.25

Cr

1.27

Mn

1.39

Fe

1.25

Co

1.26

Ni

1.21

Cu

1.38

Zn

1.31

Ga

1.26

Ge

1.22

As

1.19

Se

1.16

Br

1.14

Kr

1.10

Rb

2.11

Sr

1.92

Y

1.62

Zr

1.48

Nb

1.37

Mo

1.45

Tc

1.56

Ru

1.26

Rh

1.35

Pd

1.31

Ag

1.53

Cd

1.48

In

1.44

Sn

1.41

Sb

1.38

Te

1.35

I

1.33

Xe

1.30

Cs

2.25

Ba

1.98

La

1.69

Hf

1.50

Ta

1.38

W

1.46

Re

1.59

Os

1.28

Ir

1.37

Pt

1.28

Au

1.44

Hg

1.49

Tl

148

Pb

1.47

Bi

1.46

 

 

 

| Related key-words: 
  ``LEWIS,  CVB, SETPI,  METAL, CHARGE, CHARGES, and MOZYME``
| See also: `Lewis Structures <Lewis_structures.html>`__, `MOZYME
  introduction <mozyme_introduction.html>`__

 

 

.. raw:: html

   <div align="left">

 

.. raw:: html

   </div>

 
