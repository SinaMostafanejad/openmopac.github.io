.. _PDBOUT:

``PDBOUT``
----------

 ``PDBOUT`` will cause the geometry to be printed in PDB format.
Although the format printed is designed to match that used in the
Brookhaven Protein Data Bank, the agreement is not always exact. 

If atomic partial charges have been calculated, these will be printed in
columns 61-66 for each atom.  In the PDB format, these are the columns
used for the temperature factor.  The atomic partial charges can be
viewed using  JSmol if ```HTML`` <html.html>`__ is present.

By default, the residue sequence will be that supplied by the data set. 
To re-calculate residues, use ``RESIDUES``; that will ignore the residue
names supplied by the data set, and re-calculate them using the topology
of the system. If this option is used, check that the new residue names
are acceptable.  To do this, look in the output file for the section:

If the data set includes comments (lines that start with an asterisk
(*)) followed by PDB words such as HEADER, TITLE, COMPOUND, REMARK,
etc., these will be printed in the PDB format.  This is very useful in
preserving the integrity of the PDB file.

If residues are missing, or if multiple proteins are present, keyword
``START_RES(text)`` should be used to indicate this. By default, each
chain, or section of chain, will be given a different letter, starting
with "A".  This can cause problems, particularly if a chain has a gap in
it, because, by default, MOPAC would give the two chain sections
different letters.  Chain letters can be explicitly assigned by using
``CHAIN(text)``.  These keywords are automatically generated when a PDB
file is read in and a MOPAC data set generated.

If hydrogen atoms have been added, these will automatically be put in
their correct place in the PDB file, unless
```NORESEQ`` <noreseq.html>`__ is present.

Except for hydrogen atoms, atom labels will not be changed. Label names
for hydrogen atoms will be based on the atom the hydrogen is attached
to.  This makes proton migrations easier to identify.

A fast way to convert a data-set from MOPAC to PDB format is to use
``0SCF`` and ``PDBOUT.`` Also, if a restart file, <file>.res, is
present, adding ``RESTART``\ to the data set will read in the updated
geometry and, if ``0SCF`` and ``PDBOUT`` are also both present, will
immediately print the current geometry in PDB format.

See also ```HTML`` <html.html>`__.
