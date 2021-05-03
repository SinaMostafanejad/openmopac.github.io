.. _PDB:

``PDB=(text)``
--------------

Although MOZYME will normally recognize all the elements in a PDB file,
the possibility exists that an element or entity will be defined in a
PDB file in an unusual way, and as a result it will not be recognized.
To allow for this, the keyword ``PDB(text)`` is provided. The *text* is
composed of a series of entries of form 'Chemical-symbol:Atomic number',
separated by commas. Thus if a PDB had some hydrogen atoms represented
by the symbol *J*, and a bromine atom represented by *QW*, then these
symbols would be correctly recognized by MOZYME if ``PDB(J:1,QW:35)``
were specified on the keyword line. Entities which do not correspond to
elements can be excluded by assigning them the atomic number zero, e.g.
``PDB(LP:0)`` would exclude any explicitly defined lone-pairs.
