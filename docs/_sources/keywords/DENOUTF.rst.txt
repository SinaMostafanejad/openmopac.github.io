.. _DENOUTF:

``DENOUTF``
===========

In a MOPAC calculation, the density matrix at the end of the calculation
is to be output in a form suitable for input in another job. If an
automatic dump due to the time being exceeded occurs during the current
run, and ``DENOUT`` is present, then the density matrix will also be
output. (see ``RESTART``).  The density matrix file is unformatted.  To
output the formatted file, use ``DENOUTF``.

In both formatted and unformatted density files, the layout of the data
is: Number of atomic orbitals, number of atoms, lower half triangle of
density matrix elements.  When the density file is used in a subsequent
calculation, the number of atomic orbitals and number of atoms is
compared with that expected.  If they are different, an error message is
printed, and the run is stopped.

In a MOZYME calculation, the LMOs at the end of the calculation are to
be output in a form suitable for input in another job. If an automatic
dump due to the time being exceeded occurs during the current run, and
``DENOUT`` is present, then the density matrix will also be output. (see
``RESTART``).  The formatted option, ``DENOUTF,`` is not available .

The opposite of ``DENOUT`` is ``OLDENS``
