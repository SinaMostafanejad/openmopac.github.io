.. _CHAINS:

``CHAINS=(text)``
=================

``CHAINS=(A)``\ can be used to select all atoms in a PDB file that have
the same chain-letter, here ``A``.  Some PDB files contain more than one
protein. If, for example, a PDB file contains two proteins plus
associates small molecules, e.g., H\ :sub:`2`\ O or
[SO:sub:`4`]\ :sup:`=`, and all atoms relates to the first protein are
assigned chain-letter A, and all the others are assigned chain-letter B,
then if \ ``CHAINS=(A)``\ is present, only those atoms with chain-letter
``A`` will be selected. In rare cases two or more chain-letters might be
needed, in which case the letters needed would be specified as, e.g.,
``CHAINS=(AB)``. or ``CHAINS=(CDEF)`` Up to four letters can be
specified.

A more common use of this keyword would be when there is, or will be, a
need to re-label the atoms in the PDB file by using
```RESIDUES`` <residues.html>`__. If keyword ``CHAINS``\ is already
present in the data set, and there will never be a need to re-label the
atoms using ``RESIDUES`` (this is the most likely case), then, to reduce
the number of keywords, it is safe to delete keyword ``CHAINS``.  By
default, when a PDB file is read in, all chains are automatically
identified, and used in constructing the keyword ``CHAINS``. In normal
work, this keyword should not be modified, however if there is a need to
modify it, the following definition of the *text* is provided as a
guide:

Protein chains are normally labeled A, then B, then C, etc.  If this
sequence is correct, then keyword ``CHAINS=(ABC)`` is not needed.  If a
different sequence is to be used, put that sequence in place of *text*
in ``CHAINS=(text).``

For example, in PDB entry 2V66, the chains are B, C, D, and E, not A, B,
C, D; for this system, the keyword, if used, would be:
``CHAINS=(BCDE).``

See also ```START_RES(text)`` <start_res.html>`__ to define residue
numbers.

See also: ```PDB`` <pdb.html>`__, ```RESIDUES`` <residues.html>`__,
``XENO``, ```ALT_A`` <alt_a.html>`__, and ``RESEQ``.

 
