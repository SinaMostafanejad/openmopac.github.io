.. _CHARGE:

CHARGE
======

The total electric charge, which specifies the number of electrons in a system.
The default charge is zero, corresponding to a number of electrons equal to the total effective nuclear charge on all atoms in the system.

**SYNTAX:** ``CHARGE=n``

The charge :math:`n` must be an integer.
Positive values correspond to cations, and negative values correspond to anions.

.. rubric:: Use with ``MOZYME``

The ``CHARGE`` keyword is compatible with :ref:`MOZYME` calculations, but its behavior changes.
``MOZYME`` calculations begin by assigning a :ref:`Lewis_structure` to a system, which sets atomic charges and thus a total charge.
By default, ``CHARGE`` is assigned to the total charge of the Lewis structure.
The ``CHARGE`` keyword cannot change a system's total charge in a :ref:`MOZYME` calculation,
rather its purpose is to verify that the total charge corresponds to a value that the user expected.
By default, a discrepancy in charge values will cause an error, but it can be reduced to a warning with the :ref:`GEO-OK` keyword
(the total charge assigned to the Lewis structure is still used in the :ref:`MOZYME` calculation).

When charge conflicts are present, the Lewis structure is printed by MOPAC to assist
in the use of other keywords that can adjust the total charge of the Lewis structure to the desired value:
:ref:`METAL` to fully ionize specific atoms, :ref:`SETPI` to set explicit double bonds,
and :ref:`CVB` to set explicit single bonds or suppress bonds while assiging the Lewis structure.
