.. _SITE:

``SITE``
========

Quite often, after hydrogen atoms have been added to a protein, the
formal, i.e., Lewis structure, ionization state of various sites are not
what is wanted.  This fault can be corrected by setting the ionization
state of various sites in a protein using ``SITE=(``\ *text*\ ``)``. 
This adds or removed individual hydrogen atoms; because of this the job
cannot continue.   The job will be stopped after the ``SITE`` operation
has been performed, because ``SITE`` changes the formula, so adding
``0SCF`` is not necessary.

``SITE`` can also be used to add hydrogen atoms to carbons.

By default, the resulting structure will be resequenced.  If this is not
wanted, add ``NORESEQ``.

Four methods of specifying sites to be ionized or deionized are
supported. Method **A** is recommended when starting with a new
protein.  Method **B** is very specific, but writing the keyword
requires the most work; method **C** is less specific but the keyword is
easy to write; method **D** affects all suitable residues, and its
keyword is easy to write.  Use option **A** first, then, if necessary
and if possible, use **C**, and only when specific atoms are involved
use **B**. Option **D** is sometimes useful in identifying all ionizable
sites.

 

**(A)**  **Adding Salt Bridges.** Salt bridges can be added using
``SITE=(SALT[=n.n])``. All pairs of potentially charged sites (residues
only) within about 4 Ångstroms, or n.n Ångstroms if "=n.nn" is present,
will be created.  The default of 4.0 Angstroms was chosen to conform
with Barlow, D. J. and Thornton, J. M. (1983) J. Mol. Biol., 168,
867–885.  The distance is "about 4 Ångstroms" because the salt bridges
are calculated from the Lewis structure, which might put the charge on a
-COO(-) group on the wrong oxygen, or on a guanidinium on the wrong
nitrogen. To allow for this, the cutoff is increased by 2.0 Ångstroms.  
If a charged site already exists it will not be considered as a
potential charged site.  This option can be used with
```ADD-H`` <ADD-H.html>`__, for example as
"``HTML ADD-H  SITE=(SALT)``"  Here, ``ADD-H`` will generate a system
with all sites neutral, then ``SITE=(SALT)``\ will create salt bridges
using (N:sub:`ζ` of Lys, N\ :sub:`ε`, N\ :sub:`η1` or N\ :sub:`η2` of an
Arg, N\ :sub:`δ1` or N\ :sub:`ε2` of a His, or a terminal -NH:sub:`2`
group) and a carboxylic acid group.  This is equivalent to the
definition used in "Hydrogen bonds and salt bridges across
protein–protein interfaces", Dong Xu, Chung-Jung Tsai and Ruth Nussinov,
Protein Engineering vol.10 no.9 pp.999–1012, 1997.  Note that sulfate,
phosphate and other ionizable sites, including those on non-peptide
substrates are not considered, when this option is used.

Sometimes ``SITE=(SALT)``.makes a mistake, particularly if metal atoms
are involved.  If this happens, use additional ``SITE`` keyword(s) to
add or remove hydrogen atoms as necessary.  When this is done, put the
``SITE=(SALT)``\ keyword after all the other ``SITE``\ keyword(s).

**(B) Modifying specific residues.**  Individual residues to be ionized
or de-ionized. In this format, *text* has the form
"Annn(q1[q2])[,Bmmm(q3[q4])]..." where "A" is the chain letter, "nnn" is
the residue number, and "q1" and "q2" are the charges, either +, 0, or
–.  If residue 123 in chain B is an Arg, then, to ionize it, use
``SITE=(B123(+))``. If the first residue in that chain, i.e., the
-NH:sub:`2` end, is also to be ionized, then use
``SITE=(B123(+),B1(+))``. If a carboxylic acid group, e.g. an Asp at
residue site D234, should also be ionized, then
use \ ``SITE=(B123(+),B1(+),D234(–))``. A `salt
bridge <salt_bridges.html>`__ can be created using a construction of the
form ``SITE=(A12(+),B34(-)).``\ To de-ionize a site use charge "(0)"
thus if the sites just described were ionized, they could then be
de-ionized by using ``SITE=(B123(0),B1(0),D234(0)).`` If a residue has
two ionizable sites, such as a Lys at the start of a chain, or Asp at
the end of a chain, use two charges, to indicate the ionization state of
each site, e.g., ``SITE=(B1(++),B100(--))``. No specific tautomer is
defined - if it's not the one wanted, use method **A**.  An alternative
would be to make the change outside MOPAC, to do this, edit the
resulting <file>.out, <file>.arc, or <file>.pdb to make a new data set.
This should work for sulfate and phosphate groups, but is easily
confused by hetero-groups, e.g., ADP or ATP. 

**(C) Modifying specific atoms**. 

**For oxygen and nitrogen only:** This option should only be used when
option **B** cannot be used, because it requires more effort to define
the atom involved.  Individual oxygen and nitrogen atoms can be ionized
or neutralized by adding or removing hydrogen atoms.  This method is
completely general in that it can be used for all ionizable oxygen and
nitrogen atoms, and completely specific in that the only atom affected
is the one specified.  To achieve this generality, this option requires
the atom to be specified in a very precise way.  The format for this
option is: ``SITE=("``\ *text*\ ``"(n))`` where ``text`` is the PDB name
of the atom, this is given in PDB files in columns 13 to 26 for an
atom.  An alternative is to use the JSmol format.  With JSmol, the label
starts with a "[" and ends at the character before " #".  As with the
PDB format, spaces are not important when the JSmol format is used,
i.e., ``SITE=("[LYS]4:A.NZ"(+),"[ASP] 43: A   .OD2"(0))``.   As with
option B, the charge, n, can be + or 0 (for nitrogen) and +, 0 or – (for
oxygen).  If ``n``\ =1 for the nitrogen atom in pyridine, then the
nitrogen would become a cation, and the pyridine would become
pyridinium.  If ``n``\ =1 for methylamine, the result would be
[CH:sub:`3`-NH:sub:`3`]\ :sup:`+`, if ``n``\ =0 for a positively-charged
nitrogen atom, then that atom would lose a hydrogen to become neutral.
If ``n``\ = – for an oxygen in acetic acid, the result would be
acetate.  If ``n``\ =0 for a negatively-charged oxygen atom in a
compound, the result would be a hydroxy group. To convert a hydroxyl
group bonded to an atom into a water molecule, use "+" for the charge on
the oxygen atom.   

This option works for any oxygen or nitrogen atom, including those in
sulfate and phosphate, etc.

If the PDB label for the atom is not unique, the first such label will
be used.  To avoid this potential error, make the appropriate atom's
label unique.  Spaces are not important, but using them makes it easier
to read the atom label.

 Examples are: ``SITE=("OG1 THR G 166"(0))`` and
``SITE=("OG  SER G 195"(0),"OD2 ASP G 194"(-),"[PO4]1157:B.O8"(-))``.

Wildcards are allowed for the residue name and for the chain letter. 
When a wildcard is used, a letter is replaced by an asterisk, "*",
thus:\ ``SITE=("OG  *** G 195"(0),"OD2 *** * 194"(-),"[***]1157:*.O8"(-))``.
The first occurrence that matches will be used.  Using wildcards allows
similar systems to be modified easily, for example if 8-Oxo-guanine
monophosphate and Guanine monophosphate are present, and the N7 has to
be protonated or deprotonated (steps in converting from one to the
other), and the residue names are 8OG and GMP, and they have the same
residue number, then rather than use the full name, wildcards can be
used, thus
``SITE=("N7   *** * 1157"(0))``\ or\ ``SITE=("[***]1157:*.N7"(+)).``

If an attempt is made to modify an atom that can't be modified, e.g., to
make the oxygen atom in CH\ :sub:`3`-O-CH:sub:`3` into an anion, an
error message will be generated, but be aware that not all possible
cases have been defined.

**For carbon only:** Sometimes hydrogenation puts the wrong number of
hydrogen atoms on a carbon atom.  To correct that, the option is
provided to change the number of hydrogen atoms.  For example, if only
two hydrogen atoms are put on a methyl carbon, then a third hydrogen
atom must be added to make a correct methyl group.  This operation can
be done using the ``SITE`` keywords of the type
``SITE=("[9G1]301:A.C07"(+).`` If two or three hydrogen atoms are to be
added or deleted, then put the characters "2" or "3" after the sign
symbol.  The format is similar to that for oxygen and nitrogen in the
previous section, but after the symbols "+", "0", and "-", an optional
"2" or "3" can be supplied.   

These three formats, **A**, **B**, and **C** can be combined, although
if ``SALT`` is used, it should be first, because it automatically
constructs salt bridges.  A simpler way to define ionization states is
to use two or more ``SITE``\ keywords.  For example, if all common salt
bridges are wanted and one or more atoms are to be protonated or
deprotonated, then the two keywords ``SITE=(SALT)``
and\ ``SITE=("OG1  THR G 166"(0),etc.)`` could be used.  If a large
number of changes need to be made, use two or more ``SITE`` commands.

**(D) Modifying all specified ionizable groups.** This format applies to
all residues with the specified groups.  *Text* in this case can be one
or more of the entries in the table below.  Entries should be separated
by a comma or by a semicolon. 

To neutralize all sites in a protein, use ``SITE=(COOH,NH2,ARG,HIS)``. 
To ionize all sites, use ``SITE=(COO,NH3,ARG(+),HIS(+),SO4,PO4)`` or, to
avoid extra typing, use ``SITE=(IONIZE)``. Note: This option is
equivalent to ``SITE=(COO,NH3,ARG(+),SO4,PO4),`` i.e., it will not
automatically ionize His.   Serine, threonine, tyrosine, and the
NH\ :sub:`2` side-chain of asparagine cannot be modified using this
format.  The SO4 option will delete hydrogen atoms attached to an oxygen
on SO\ :sub:`4`, PO4 will delete a hydrogen atom attached to an oxygen
on PO\ :sub:`4`, if one exists, to give the mono-anion, i.e.,
CH\ :sub:`3`-O-P(OH):sub:`2`\ O would become
]CH\ :sub:`3`-O-P(OH)O:sub:`2`]\ :sup:`-`, and H\ :sub:`3`\ PO\ :sub:`4`
would become [H:sub:`2`\ PO\ :sub:`4`]\ :sup:`-`.  No specific tautomer
is defined - if it's not the one wanted, make the change using method
**C**.    The pKa of H\ :sub:`3`\ PO\ :sub:`4` is 2.12, of
[H:sub:`2`\ PO\ :sub:`4`]\ :sup:`-` = 7.21, and of
[HPO:sub:`4`]\ :sup:`=` = 12.67.

.. raw:: html

   <div align="center">

+-----------------------+-----------------------+-----------------------+
| Text                  |                       | Effect                |
+-----------------------+-----------------------+-----------------------+
| COOH                  |                       | Add a hydrogen atom   |
|                       |                       | to -COO groups        |
+-----------------------+-----------------------+-----------------------+
| COO                   |                       | Remove the hydrogen   |
|                       |                       | atom from -COOH       |
|                       |                       | groups                |
+-----------------------+-----------------------+-----------------------+
| NH3                   |                       | Add a hydrogen atom   |
|                       |                       | to -NH:sub:`2` groups |
|                       |                       | (except in            |
|                       |                       | -CO-NH:sub:`2`)       |
+-----------------------+-----------------------+-----------------------+
| NH2                   |                       | Remove a hydrogen     |
|                       |                       | atom from -NH:sub:`3` |
|                       |                       | groups                |
+-----------------------+-----------------------+-----------------------+
| Arg(+)                |                       | Add a hydrogen atom   |
|                       |                       | to -Arg-              |
+-----------------------+-----------------------+-----------------------+
| Arg                   |                       | Remove a hydrogen     |
|                       |                       | atom from -Arg(+)-    |
+-----------------------+-----------------------+-----------------------+
| His(+)                |                       | Add a hydrogen atom   |
|                       |                       | to -His-              |
+-----------------------+-----------------------+-----------------------+
| His                   |                       | Remove a hydrogen     |
|                       |                       | atom from -His(+)-    |
+-----------------------+-----------------------+-----------------------+
| SO4                   |                       | Remove any hydrogen   |
|                       |                       | atoms from a sulfate  |
|                       |                       | group                 |
+-----------------------+-----------------------+-----------------------+
| PO4                   |                       | Remove any hydrogen   |
|                       |                       | atoms from a          |
|                       |                       | phosphate group       |
+-----------------------+-----------------------+-----------------------+

.. raw:: html

   </div>

Option **D** cannot be used with options **A, B**, or **C**.  Option
**D** can be useful during preliminary work on proteins, to identify all
ionizable sites.

Use of ``SITE`` to:
~~~~~~~~~~~~~~~~~~~

-  Move a hydrogen atom in -COOH from one oxygen to the other.  To move
   a hydrogen atom on OD1 in Asp 100 to OD2, use
   ``SITE=("OD1 ASP A      100"(-),"OD2 ASP A 100"(0))``
-  Move a hydrogen atom from  ND1 to NE2 in histidine.  To move a
   hydrogen atom on ND1 in His 100 to NE2, use
   ``SITE=("ND1 HIS A      100"(0),"NE2 HIS A 100"(+))``

see also  `atom numbers <atom_numbers.html>`__,
```ADD-H`` <ADD-H.html>`__

 
