.. _OUTPUT:

``OUTPUT``
----------

The size of the normal output file can become very large when large
systems are being used.  This can make it difficult to find interesting
information. To reduce the amount of information printed to the output
file, add ``OUTPUT``\ to the keyword list. 

To allow some blocks of data that would otherwise be suppressed by
``OUTPUT`` use ``OUTPUT`` followed by letters in parentheses,  Allowed
letters are

+--------+---------------------------------------------+
| Letter | Does not suppress                           |
+--------+---------------------------------------------+
| C      | Coordinates                                 |
+--------+---------------------------------------------+
| F      | Force matrix (in a FORCE calculation)       |
+--------+---------------------------------------------+
| G      | Gradients                                   |
+--------+---------------------------------------------+
| N      | Normal coordinates (in a FORCE calculation) |
+--------+---------------------------------------------+
| O      | Orientation (in a FORCE calculation)        |
+--------+---------------------------------------------+
| P      | Atomic Orbital Populations                  |
+--------+---------------------------------------------+
| Q      | Fractional atomic charges                   |
+--------+---------------------------------------------+
| T      | Topography (atom connectivity)              |
+--------+---------------------------------------------+
| V      | Starting velocity of atoms in a DRC/IRC     |
+--------+---------------------------------------------+
| X      | Cartesian coordinates                       |
+--------+---------------------------------------------+

Thus, if fractional atomic charges are to be printed, but other
voluminous data suppressed, use ``OUTPUT(Q)``.  If atomic orbital
populations are also wanted, use ``OUTPUT(QP)``. Note that ``OUTPUT``
only suppresses output.  If some data would not normally be printed, for
example, in a ```1SCF`` <one_scf.html>`__ calculation the gradients
would not be printed unless ```GRADIENTS`` <gradients.html>`__ was also
present, then adding letters to the ``OUTPUT`` keyword to not suppress
the gradients would do nothing.  
