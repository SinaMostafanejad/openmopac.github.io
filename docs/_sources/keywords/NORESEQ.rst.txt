.. _NORESEQ:

``NORESEQ``
-----------

By default, proteins are re-sequenced into the standard PDB file
sequence, i.e., all atoms in a residue are contiguous, when keywords
``ADD-H`` or ``SITE`` are used, or if the input data set is a pure PDB
file.  To prevent ``ADD-H`` or ``SITE`` from re-sequencing the data, add
``NORESEQ``.  To stop a pure PDB file from being resequenced, convert it
to a MOPAC data set by adding the standard three lines to the start, and
use keywords ``ADD-H`` and ``NORESEQ.``

Some PDB files contain severe topologic errors that confuse the residue
recognition routine, a pre-requisite step for resequencing. Such errors
result in a warning message being printed, and the run stopped.  This
type of problem occurs most often when adding hydrogen atoms using
``ADD-H.``  By default ``ADD-H`` uses the residue recognition routine,
and a topologic problem could prevent ``ADD-H`` from working correctly. 
To avoid this problem, run ``ADD-H`` with ``NORESEQ;`` this avoids using
the residue recognition routine.   Of course, the topologic problem is
still present, even after hydrogen atoms are added.  To correct the
underlying problem, first optimize the positions of the hydrogen atoms,
then optimize the positions of the atoms responsible for the topologic
error.

Unless corrective action is taken, some topologic errors can result in
an incorrect assignment of hydrogen atoms when using ``ADD-H``.  To
correct this fault, use ```CVB`` <CVB.html>`__ with ``ADD-H`` and
``NORESEQ``. This is an unusual use of ``CVB`` in that it normally
cannot be used with ``ADD-H``, but it is justified in this specific
case.

See also: ``RESEQ``, ```RESIDUES`` <residues.html>`__, ``XENO``,
```CHAINS`` <chains.html>`__, and ```START_RES`` <start_res.html>`__.

 
