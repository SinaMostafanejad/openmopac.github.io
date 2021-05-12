.. _XENO:

``XENO``
========

This keyword is only used when the default atomic labels in a PDB file
are not to be used, i.e., when ```RESIDUES`` <residues.html>`__ or
```RESIDUES0`` <residues.html>`__ is present. 

For non-standard residues and hetero groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the method that recognizes amino acid residues only
recognizes the standard twenty amino-acid residues, but some proteins
contain residues which have extra molecular fragments attached. Other
residues, particularly where there is a break in a chain, have atoms
missing and therefore they do not correspond to any of the 20 standard
residues.  In some cases, even though some atoms are missing, the
remaining residue is one of the standard 20 residues.  This results in
the residue being misidentified. Many hetero groups (small molecules,
e.g., water, sulfate, glucose) that are associated with a protein are
automatically recognized.  Unidentified residues are given the label
"UNK", and any heterogroups not recognized are given the label "HET". In
order to allow these unusual species to be correctly recognized, the
keyword ``XENO`` is provided. ````

XENO, from the Greek *ξενοσ*, xenos, for 'stranger', defines unusual
residues in a protein and unusual heterogroups in terms of the residue's
number and chain letter. The format of ``XENO`` is:

````

XENO=([*C*]\ *Res=L*\ [{,;}[*C*]\ *Res=L*][{,;}[*C*]\ *Res=L*]...) where
*[C]* is the chain letter, if used, *Res* is the residue number, and *L*
is the one-letter symbol for the residue, e.g.
``XENO=(A55=K;78=L,C3=P)``\ or a three-letter identifier, for example:
``XENO=(B1123=ATP,B1157=SO4)``.  These two styles can be used in any
order in the keyword, e.g.,:
``XENO=(A12=G,B1157=8OG,B45=D,A787=ATP,B1157=8OG,123=BIT)``

If the one letter abbreviation is used, e.g., K for lysine or L for
leucine, this will be replaced in the run by the standard three-letter
identifier.  If the chain letter is omitted, chain A will be assumed.

When a prosthetic group is present, e.g. the the extra fragment in
bacteriorhodopsin, on Lys216: -COCHRNH-;   R =
CH\ :sub:`2`\ CH\ :sub:`2`\ CH\ :sub:`2`\ CH\ :sub:`2`\ N=CHCH=CMeCH=CHCH=CMeCH=CHC\ :sub:`9`\ H\ :sub:`15`,
an alternative to using ``XENO`` is to delete the connection between the
normal residue (here lysine) and the prosthetic (here retinal), using
``CVB``

If ``XENO`` is *not* used, the checks on possible problems in the PDB
file will still work, but the label for partial or the modified residues
will be incorrect or reported as "\ ``UNK"`` or, for heterogroups,
``"HET"``, instead of the more descriptive label which would result from
using ``XENO``.

See also: ```RESIDUES`` <residues.html>`__, ```RESEQ`` <reseq.html>`__,
```CHAINS`` <chains.html>`__, and ```START_RES`` <start_res.html>`__.
