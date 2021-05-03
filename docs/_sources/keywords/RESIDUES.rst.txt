.. _RESIDUES:

``RESIDUES[0]``
---------------

In protein work, each atom will be labeled using information supplied by
the PDB file.  An alternative is to use keyword ``RESIDUES`` which
causes the PDB-style labels to be worked out using only the topology of
the system.  Modified residues can still be recognized if ``XENO=text``
is used. Unless other keywords such as  ```CHAINS`` <chains.html>`__,
and ```START_RES`` <start_res.html>`__ are present, or the input file is
already in PDB format, the residue nearest to the NH\ :sub:`2` end of
the protein will be No. 1 in chain A, the next is 2, and so on, and the
different chains will be labeled A, then B, C, D, etc.  If the input
file is in PAB format, not just in MOPAC format with PDB information,
the residue numbers and chain letters will be worked out from the PDB
file.

Keyword ``RESIDUES`` uses part of `MOZYME <mozyme_introduction.html>`__,
so when the job starts it uses the MOZYME option. If keyword
```MOZYME`` <mozyme.html>`__ is not present, then the job will only be
allowed to run if no SCF calculations are possible.  This is to prevent
a MOZYME calculation being done unless keyword ``MOZYME`` is present. 
Jobs that do not involve SCF calculations use one or more of the
keywords ```0SCF`` <zero_scf.html>`__, ```LEWIS`` <lewis.html>`__,
```CHARGES`` <charges.html>`__, ```ADD-H`` <ADD-H.html>`__,
```SITE`` <site.html>`__, or ```RESEQ`` <reseq.html>`__.

Keyword ``RESIDUES`` converts the data-set into almost standard PDB
format by making the minimum change to the existing format.  This means
that:

| \* The residue numbers and letters will be preserved.
| \* Atoms will not be re-arranged.  To put the atoms into standard PDB
  sequence, use ```RESEQ`` <reseq.html>`__.
| \* If a heterogroup is covalently bonded to an existing residue, the
  residue will not be correctly recognized.  To correctly recognize
  modified residues, use ```CVB`` <CVB.html>`__ to remove the covalent
  bond joining the heterogroup to the residue.  Then, if necessary, use 
  ``XENO=text`` to re-name the residue and to name the heterogroup.
| \* Heterogroups are labeled using a simple numbering system.  When
  more than one atom of an element is present, the atoms will be
  numbered sequentially, i.e., C1, C2, .... C45, C46.  When this
  convention is not wanted, for example if heteroatoms are labeled C2',
  P', etc., (think saccharides) then edit the new geometry by using
  cut-and-paste and the original, better, labeling system.  Do not
  correct errors in atom serial numbers - these will be automatically
  corrected by MOPAC in future jobs.
| \* All atoms will be given a chain-letter.  This includes water
  molecules, ligands, etc.
| \* Atom serial numbers correspond to atom numbers plus any terminators
  (TER's).  Although interesting, these numbers are re-calculated when
  any future jobs are run.  That is, atom serial numbers are not
  important in any MOPAC calculations.
| \* Many PDB files use non-standard atom labels.  If the label is
  highly unusual the new label might be incorrect.
| \* Every atom should have a unique label.  This is important for jobs
  that use ```GEO_REF`` <geo_ref.html>`__.

``RESIDUES0`` - preserves the original atom labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Good practice is to use ``RESIDUES`` to assign PDB labels to atoms, and
to not do any other operations, i.e., do not resequence the atoms, or do
any calculations in the same job.  After the ``RESIDUES`` job finishes,
examine both the output and the new data-set(s) to check that the
re-labeling operation was done correctly.  In the original PDB data-set,
some atoms might have unusual labels, for example, a sugar backbone atom
might have a label such as " C3' "  To keep the original atom labels,
use ``RESIDUES0`` (the word "RESIDUES" followed by a zero) instead of
``RESIDUES``.  If the starting geometry was already in PDB format, and
the re-labeling is partially incorrect, then copy and paste the relevant
parts of the correctly re-labeled file into the original data-set.

When individual amino acids are mutated, ``RESIDUES`` can be used to
re-label the mutated sites.

If ``RESIDUES`` does not work when other keywords are present, run
``RESIDUES`` with keyword ``0SCF``\ in a job on its own, then use the
results for the job you want.

The most common use for\ ``RESIDUES`` is to allow the residue sequence
reported in the PDB file to be compared to the sequence defined by the
geometry, i.e., by the topology, of the system.  By comparing reported
and actual sequences, possible problems in the PDB file can be detected.

.. raw:: html

   <div align="CENTER">

Table: Abbreviations for the 20 Amino Acids

+-----------------+-----------------+-----------------+-----------------+
| Amino Acid      | | Formula of    | | Three-Letter  | | One-Letter    |
|                 | | Residue\ |$^{ | | Abbreviation  | | Abbreviation  |
|                 | dag             |                 |                 |
|                 |   }$|           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Glycine         | C\ :sub:`2`\ NO | GLY             | G               |
|                 | H\ :sub:`3`     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Alanine         | C\ :sub:`3`\ NO | ALA             | A               |
|                 | H\ :sub:`5`     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Valine          | C\ :sub:`5`\ NO | VAL             | V               |
|                 | H\ :sub:`9`     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Leucine         | C\ :sub:`6`\ NO | LEU             | L               |
|                 | H\ :sub:`11`    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Isoleucine      | C\ :sub:`6`\ NO | ILE             | I               |
|                 | H\ :sub:`11`    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Serine          | C\ :sub:`3`\ NO | SER             | S               |
|                 | \ :sub:`2`\ H\  |                 |                 |
|                 | :sub:`5`        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Threonine       | C\ :sub:`4`\ NO | THR             | T               |
|                 | \ :sub:`2`\ H\  |                 |                 |
|                 | :sub:`7`        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Aspartic acid   | C\ :sub:`4`\ NO | ASP             | D               |
|                 | \ :sub:`3`\ H\  |                 |                 |
|                 | :sub:`5`        |                 |                 |
|                 | (4)             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Asparagine      | C\ :sub:`4`\ N\ | ASN             | N               |
|                 |  :sub:`2`\ O\ : |                 |                 |
|                 | sub:`2`\ H\ :su |                 |                 |
|                 | b:`6`           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Lysine          | C\ :sub:`6`\ N\ | LYS             | K               |
|                 |  :sub:`2`\ OH\  |                 |                 |
|                 | :sub:`12`       |                 |                 |
|                 | (13)            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Glutamic acid   | C\ :sub:`5`\ NO | GLU             | E               |
|                 | \ :sub:`3`\ H\  |                 |                 |
|                 | :sub:`7`        |                 |                 |
|                 | (6)             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Glutamine       | C\ :sub:`5`\ N\ | GLN             | Q               |
|                 |  :sub:`2`\ O\ : |                 |                 |
|                 | sub:`2`\ H\ :su |                 |                 |
|                 | b:`8`           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Arginine        | C\ :sub:`6`\ N\ | ARG             | R               |
|                 |  :sub:`4`\ OH\  |                 |                 |
|                 | :sub:`12`       |                 |                 |
|                 | (13)            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Histidine       | C\ :sub:`6`\ N\ | HIS             | H               |
|                 |  :sub:`3`\ OH\  |                 |                 |
|                 | :sub:`7`        |                 |                 |
|                 | (8)             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Phenylalanine   | C\ :sub:`9`\ NO | PHE             | F               |
|                 | H\ :sub:`9`     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Cysteine        | C\ :sub:`3`\ NO | CYS             | C               |
|                 | SH\ :sub:`5`    |                 |                 |
|                 | (4)             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Tryptophan      | C\ :sub:`11`\ N | TRP             | W               |
|                 | \ :sub:`2`\ O   |                 |                 |
|                 | H\ :sub:`10`    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Tyrosine        | C\ :sub:`9`\ NO | TYR             | Y               |
|                 | \ :sub:`2`\ H\  |                 |                 |
|                 | :sub:`9`        |                 |                 |
|                 | (8)             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Methionine      | C\ :sub:`5`\ NO | MET             | M               |
|                 | SH\ :sub:`9`    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Proline         | C\ :sub:`5`\ NO | PRO             | P               |
|                 | H\ :sub:`7`     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

|dag|: The number of hydrogen atoms in the ionized residue is given in
parenthesis after the formula. Cysteine may exist in the neutral,
ionized or reduced form.

.. raw:: html

   </div>

| 
| Small molecules are often found associated with proteins. To allow for
  this, many special groups, e.g., PO\ :sub:`4`, SO\ :sub:`4`,
  H\ :sub:`2`\ O, the aldohexoses and aldoketoses, are also recognized. 
  Any groups not automatically identified or wrongly identified can be
  explicitly labeled using ```XENO`` <xeno.html>`__.

See also: ```RESEQ`` <reseq.html>`__, ```CHAINS`` <chains.html>`__, and
```START_RES`` <start_res.html>`__.

.. |$^{dag }$| image:: img155.gif
   :width: 11px
   :height: 19px
.. |dag| image:: img176.gif
   :width: 12px
   :height: 25px
