.. _PMEPR:

``PMEPR``
=========

The Parametric Molecular Electrostatic Potential of Wang and
Ford [\ `45 <references.html#pmep1>`__,\ `46 <references.html#pmep2>`__]
is generated. When ``PMEPR`` is used, extra data must follow the
Z-matrix and symmetry data. This extra data defines the plane in which
the electrostatic potential is plotted, and is summarized in the Table.
Other keywords, e.g., ``MINMEP``\ (to print the minima) or
``PRTMEP``\ (to write data for ``esplot`` to use) *must* be present.

| 

.. raw:: html

   <div align="CENTER">

.. raw:: html

   <div align="CENTER">

 
Table: Data Required by PMEPR

+-----------------------------------+-----------------------------------+
| Name of                           | Allowed Values                    |
+-----------------------------------+-----------------------------------+
| Datum                             |                                   |
+-----------------------------------+-----------------------------------+
| ICASE                             | 1, 2, 3                           |
+-----------------------------------+-----------------------------------+
| N1                                | 1-NUMAT                           |
+-----------------------------------+-----------------------------------+
| N2                                | 1-NUMAT, not N1                   |
+-----------------------------------+-----------------------------------+
| N3                                | 1-NUMAT, not N1 or N2             |
+-----------------------------------+-----------------------------------+
| X0                                | Any real number                   |
+-----------------------------------+-----------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </div>

| 
| The various planes which can be drawn through the system are
  identified by the datum ICASE:

````

ICASE=1 If ``X0`` is zero, then the plane generated passes through atoms
``N1``, ``N2`` and ``N3``. Obviously, these atoms should not lie on a
straight line. If ``X0`` is non-zero, then the plane is parallel to the
plane of atoms ``N1``, ``N2`` and ``N3``, but ``X0`` Ångstroms above it.

````

ICASE=2 If ``X0`` is zero, then the plane generated is perpendicular to
the plane of ``N1``, ``N2`` and ``N3``, and includes the line from atom
``N1`` to ``N2``. If ``X0`` is non-zero, then the plane is perpendicular
to the plane of ``N1``, ``N2`` and ``N3``, and is ``X0`` Ångstroms
above, and parallel to, the line from atom ``N1`` to ``N2``.

````

ICASE=3 The plane used is that which bisects the angle
``N2``-``N1``-``N3``. ``X0`` is meaningless in this context, and should
be set to zero.

Examples of extra data:

To generate data for the plane through atoms 10, 11, and 20, use as
extra data: "1 10 11 20 0" (do not include the quotation marks.) 
Alternatively, every datum can be expressed in keyword style, as
"icase=1 n1=10 n2=11 n3=20 z0=0"
