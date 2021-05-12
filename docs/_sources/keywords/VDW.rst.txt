.. _VDW:

``VDW``
=======

In a COSMO calculation (keyword ```ESP=78.4`` <esp.html>`__), the Van
der Waals radii of atoms can be set or changed by use of ``VDW``. The
format of the command is:

````

VDW(<chemical symbol\ :sub:`1`>=\ *n*.\ *nn;*\ <chemical
symbol\ :sub:`2`>=\ *n*.\ *nn;*\ <chemical
symbol\ :sub:`3`>=\ *n*.\ *nn*;...)

| For example, ``VDW(Cl=2.33;Br=2.50)`` would override the default
  values of the van der Waals radii of chlorine and bromine (1.65 and
  1.80, respectively).
|  

| By default, the COSMO VdW radius is 117% of the default VdW radius.
|  

Where radii specific for various methods are available, they are used. 
Radii available are:

Table 1: Default radii (Angstroms) used in COSMO

I

II

 

III

IV

V

VI

VII

| H
| 1.08

 

 

| Li
| 1.80

Be

B

| C
| 1.53

| N
| 1.48

| O
| 1.36

| F
| 1.30

| Na
| 2.30

Mg

| Al
| 2.05

| Si
| 2.10

| P
| 1.75

| S
| 1.70

| Cl
| 1.65

| K
| 2.30

| Ca
| 2.75

 

| Transition Metals
| (none)

Ga

Ge

As

Se

| Br
| 1.80

Rb

Sr

In

Sn

Sb

Te

| I
| 2.05

Cs

Ba

Tl

Pb

Bi

 

 
