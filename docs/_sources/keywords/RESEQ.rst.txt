.. _RESEQ:

``RESEQ``
---------

According to the PDB format, atoms in a protein are specified starting
with the nitrogen of the -NH:sub:`2` end and ending with the atoms at
the -COOH end. ``RESEQ`` will re-arrange the atoms into the standard PDB
sequence. ``RESEQ`` is useful particularly after adding hydrogen atoms,
see below. Because ``RESEQ`` changes the order of the atoms, further
work is not possible, and the calculation is stopped after the new
geometry is printed.

A useful additional keyword is ```HTML`` <html.html>`__; this generates
a simple HTML web-page and a PDB file in a form that is useful for
displaying protein structures using
`JSmol <http://sourceforge.net/projects/jsmol/>`__.

When ```ADD-H`` <ADD-H.html>`__ or ```SITE`` <site.html>`__ is used,
changes are made to the number or locations of hydrogen atoms. In these
two cases, ``RESEQ`` will be run automatically unless ``NORESEQ``\ is
present, so there is no need to add ``RESEQ``.  If the number or
location of hydrogen atoms is changed outside MOPAC, ``RESEQ`` should be
used.  If a raw PDB file, i.e., a file from the Protein Data Bank, is
used as a data set, then hydrogen atoms will be added automatically, and
``RESEQ`` will then be run automatically.  To stop ``RESEQ`` being run,
use a MOPAC data set, i.e., a data set with keywords, and add
``NORESEQ``.

``RESEQ`` sometimes re-arranges the atoms in unexpected ways.  Consider
phenylalanine, for example.  In it, the sequence of atoms is uniquely
defined except for C\ :sub:`δ1` and C\ :sub:`δ2`.  This means that
either one of these atoms might be chosen at random to be C\ :sub:`δ1`,
and the choice might be different from that used in the starting data
set.  This should not cause a problem when resequenced proteins are
compared using the ```GEO_REF`` <geo_ref.html>`__ option, because,
during the calculation of RMS difference, ambiguities of this type are
automatically resolved.

Also, if the protein has gaps where residues are missing, ``RESEQ``
might put the fragments into the wrong order, particularly if the
residues in the protein have been re-arranged as the result of earlier
operations.  If the order of fragments is incorrect, use ``CVB`` to make
dummy bonds that bridge the gaps and re-run. Suitable atoms are the N
terminus of one residue and the C of carboxyl of the other residue.

A `complete worked example of RESEQ <Resequence.zip>`__ can be
downloaded. This shows how ``RESEQ`` can re-arrange the sequence of
atoms into the standard PDB sequence.  The example is used in validating
MOPAC, and is much more complicated than most cases users are likely to
encounter. 

Compliance with PDB conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following operations are performed when ``RESEQ`` is used:

Within each residue, the order of atoms is: First, the four backbone
atoms, N-Ca-C-O, then the side-chain non-hydrogen atoms, then the
terminal oxygen atom, OXT, (if present), then the hydrogen atoms, in the
order in which they occur.  One exception is that the HXT atom, if
present, might not be the last hydrogen atom.

Heterogroups are positioned after all protein and isolated amino acid
moieties.

See also: ```RESIDUES`` <residues.html>`__, ``XENO``,
```CHAINS`` <chains.html>`__, and ```START_RES`` <start_res.html>`__.

 
