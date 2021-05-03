.. _START_RES:

``START_RES(text)``
===================

 Keyword ``START_RES`` provides information on the residue starting
numbers and on the locations of the ends of chains.

Some PDB files represent two or more proteins, for example there are
four proteins in one hemoglobin.  At the end of each such protein there
is a TER entry, indicating the termination of the protein chain. 
Sometimes, in a protein, one or more residues are missing.  Missing
residues are indicated in the PDB file by a discontinuity in the residue
number in a chain. By default, when a PDB file is read in, all missing
residues and gaps are automatically identified, and used in constructing
the keyword ``START_RES``. In normal work, this keyword should not be
modified, however if there is a need to modify it, the following
definition of the *text* is provided as a guide:

``START_RES[=](n1[C1][ ,-][n2[C2][ ,-][n3[C3][ ,-]...]])``

n\ :sub:`n` is the number of the first residue in a section of
contiguous residues in the PDB file, and C\ :sub:`n` is the chain
letter.  If two contiguous sections are separated by missing residues,
then the two n\ :sub:`n` are separated by a minus sign.  If the two
contiguous sections are on different proteins, then the two n\ :sub:`n`
are separated by a single space.  Only the first residue in each chain
needs a chain letter.

Thus if a PDB file consists of three proteins, A, B, and C, and A has
residues 30 31 32 33 34 38 39 40, B has residues 44 45 46 49 50 51 55 56
57, and C has residues -4 -3 -2 -1 0 1 2 3, then the keyword would be:

 ``START_RES(30A-38 44B-49-55 -4C-3)``\ or\ ``START_RES=(30A-38 44B-49-55  -4C-3)``
(The equals sign is optional.)

This keyword is read by the program as follows: 

The first residue has residue number 30 and chain letter A.  Subsequent
residues have the same chain letter, and residue number increments by
one on going from one residue to the next.  After residue 34 there is a
gap, so this set of residues would be 30:34.  The next residue found, in
the next piece of the same chain, is given the residue number 38, and
the same chain letter (A), and is bonded to the last residue of the
previous chain (residue #34).  Subsequent residues in this short chain
are given consecutive numbers, here 39 and 40.  Residue 40 marks the end
of this short bit of chain. 

When ```PDBOUT`` <pdbout.html>`__ is present, the gap between "30A-38"
and "44B-49-55" is used to indicate that a "TER" should be written to
the PDB file.

The next complete chain starts with residue #44 and has chain letter B. 
This chain consists of three short bits of chain, 44:46, 49:51, and
55:57.  The gaps due to missing residues are indicated by the minus
sign, which shows that the last residue of a bit of chain is connected
to the first residue of the next bit of chain. 

The third chain, C, is unusual, in that the original authors used a
negative number, -4, for the residue number of the first residue. 
Because of this, the symbol for the first residue in chain C is "-4C"

See also ``CHAINS(text)`` to define chain-letters.

See also: ```RESIDUES`` <residues.html>`__, ``XENO``, and ``RESEQ``.
