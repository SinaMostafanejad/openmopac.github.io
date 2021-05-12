.. _CHARGE:

``CHARGE``
==========

When the system being studied is an ion, the charge, *n*, on the ion
must be supplied by ``CHARGE=n``. For cations *n* can be 1, 2, 3, etc.;
for anions -1 or -2 or -3, etc. Examples of various charged systems are
given in the Table below.

```MOZYME`` <mozyme.html>`__-specific definition of ``CHARGE:``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| If ``CHARGE=n`` is not present, the charge required by the `Lewis
  structure <Lewis_structures.html>`__ will be used.  In general, it is
  safer to use ``CHARGE=n`` because if a change is accidentally made to
  the net charge, the error will be detected and the run stopped.
| If ``CHARGE=n`` is present, including ``CHARGE=0``, that charge will
  be used, unless it is in conflict with the Lewis structure, in which
  case the job will be stopped.
| If both ```GEO-OK`` <geo-ok.html>`__ and ``CHARGE=n`` are present,
  that charge will be used, unless it is in conflict with the Lewis
  structure, in which case the charge required by the Lewis structure
  will be used. (This is not a useful option; it is equivalent to
  ``CHARGE=n`` being absent)

In cases where the charge supplied is in conflict with that required by
the Lewis structure, the Lewis structure will be printed.  That,
together with the printed charged sites, will allow the correct charge
to be determined.

To change the charge calculated by MOZYME use one or more of the
following keywords:

| ``METAL``  - Change the formal charge of a metal atom.
| ``SETPI``  - Change Lewis structure by adding and deleting π-bonds.
| ``CVB``  - Change the topography of the system by making and deleting
  connectivities.

 

| 

.. raw:: html

   <div align="CENTER">

 
Table: Use of ``CHARGE=n``

+-----------------+-----------------+-----------------+-----------------+
| Ion             | Keyword         | Ion             | Keyword         |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| NH\ :sub:`4`\ : | ````            | CH\ :sub:`3`\ C | ````            |
| sup:`+`         | CHARGE=1        | OO\ :sup:`-`    | CHARGE=-1       |
+-----------------+-----------------+-----------------+-----------------+
| C\ :sub:`2`\ H\ | ````            | (COO):sup:`=`   | ````            |
|  :sub:`5`\ :sup | CHARGE=1        |                 | CHARGE=-2       |
| :`+`            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| SO\ :sub:`4`\ : | ````            | PO\ :sub:`4`\ : | ````            |
| sup:`=`         | CHARGE=-2       | sup:`-3`        | CHARGE=-3       |
+-----------------+-----------------+-----------------+-----------------+
| HSO\ :sub:`4`\  | ````            | H\ :sub:`2`\ PO | ````            |
| :sup:`-`        | CHARGE=-1       | \ :sub:`4`\ :su | CHARGE=-1       |
|                 |                 | p:`-`           |                 |
+-----------------+-----------------+-----------------+-----------------+

.. raw:: html

   </div>
