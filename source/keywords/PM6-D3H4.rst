.. _PM6-D3H4:

``PM6-D3H4``
============

``PM6-D3H4`` implements the corrections to hydrogen bonding and
dispersion, see: "Advanced Corrections of Hydrogen Bonding and
Dispersion for Semiempirical Quantum Mechanical Methods", Jan Řezáč and
Pavel Hobza,  Journal of Chemical Theory and Computation, **2012** *8*
(1), 141-151 DOI: 10.1021/ct200751e.

This implementation allows reactions to be modeled, but does not allow
for periodic boundary conditions, i.e., it should not be used for
modeling molecular solids of the type found in organic chemistry.

There are three parts to the D3H4 function in PM6-D3H4:

(A) A correction to the dispersion.  This uses Grimme's D3 method,
unmodified, with method-specific (here PM6) variables:  s6 = 0.88, alp =
22.0, rs18 = 1.0, rs6 = 1.18.

(B) The "H4" hydrogen-bond function developed by Řezáč and Hobza.

(C) A correction for the known fault in PM6 that hydrogen - hydrogen
steric repulsive interactions are too small. For details, see: Vorlová,
B.; Nachtigallová, D.; Jirásková-Vaníčková, J.; Ajani, H.; Jansa, P.;
Řezáč, J.; Fanfrlík, J.; Otyepka, M.; Hobza, P.; Konvalinka, J.; Lepšík,
M. *European Journal of Medicinal Chemistry* **2015**, *89*, 189–197.

To print the individual components of D3H4, add ```DISP`` <disp.html>`__
