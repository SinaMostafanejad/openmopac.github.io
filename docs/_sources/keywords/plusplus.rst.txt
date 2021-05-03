.. _plusplus:

``++``
======

Why this keyword is needed
~~~~~~~~~~~~~~~~~~~~~~~~~~

In some complicated structures, particularly when several such
structures are present in a single protein, the Lewis structure can only
be constructed if various bonds are made or broken using keyword
```CVB`` <CVB.html>`__. Editing long CVB  keywords can be difficult.  To
make this task easier keyword "++" has been written.  All it does is to
allow a single, long, keyword or ```SETUP`` <setup.html>`__ line to be
split into parts to simplify writing the long keyword line.  At
run-time, the "++" will be used in reconstructing the long keyword line.

How to use "++"
~~~~~~~~~~~~~~~

Two "+" signs, i.e., "++" can be used to split a long keyword into parts
that can be put on separate lines.  For example, in defining the bonds
in the heme ring systems in oxy-hemoglobin the keyword:

CVB=("[HEM]1142:A.Fe":-"[HEM]1142:A.NA","[HEM]1142:A.Fe":-"[HEM]1142:A.NC","[HEM]1290:B.Fe":-"[HEM]1290:B.ND","[HEM]1290:B.Fe":-"[HEM]1290:B.NB","[HEM]1542:C.Fe":-"[HEM]1542:C.NB","[HEM]1542:C.Fe":-"[HEM]1542:C.ND","[HEM]1690:D.Fe":-"[HEM]1690:D.NB","[HEM]1690:D.Fe":-"[HEM]1690:D.ND","[HEM]1142:A.Fe":-"[OXY]1143:A.O1","FE
HEM B1290":-"O2 OXY B1291","FE HEM C1542":-"O1 OXY
C1543","[HEM]1690:D.Fe":-"O2 OXY D1691") setpi

is difficult to read and very difficult to debug.  But if "++" is used,
then it can be rewritten as:

| CVB=( ++
| "[HEM]1142:A.Fe":-"[HEM]1142:A.NA", ++
| "[HEM]1142:A.Fe":-"[HEM]1142:A.NC", ++
| "[HEM]1290:B.Fe":-"[HEM]1290:B.ND", ++
| "[HEM]1290:B.Fe":-"[HEM]1290:B.NB", ++
| "[HEM]1542:C.Fe":-"[HEM]1542:C.NB", ++
| "[HEM]1542:C.Fe":-"[HEM]1542:C.ND", ++
| "[HEM]1690:D.Fe":-"[HEM]1690:D.NB", ++
| "[HEM]1690:D.Fe":-"[HEM]1690:D.ND", ++
| "[HEM]1142:A.Fe":-"[OXY]1143:A.O1", ++
| "FE HEM B1290":-"O2 OXY B1291", ++
| "FE HEM C1542":-"O1 OXY C1543", ++
| "[HEM]1690:D.Fe":-"O2 OXY D1691") ++
|   setpi

When the job starts, each line ending in "++" has the following line
joined to it, and the "++" is deleted. If "++" is used, and the next
line starts with one or more spaces, these spaces will be preserved in
the final keyword line.

**WARNING!** A common mistake is to have a "++" after a keyword ends and
forget to add a space before the next keyword at the start of the
following line.  If this happened, so the space was not present, the
next keyword would be attached to the end of the last keyword on the
line with the "++". An example of the correct use of this space can be
seen in the space before "setpi" above.
