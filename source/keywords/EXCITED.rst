.. _EXCITED:

EXCITED
=======

Targets the first excited singlet spin state within the HOMO-LUMO active space of an :ref:`RHF` calculation, which is a synonym for ``MS=0``, ``OPEN(2,2)``, and ``ROOT=2``.
See the :ref:`MS`, :ref:`OPEN`, and :ref:`ROOT` keywords for more information.

This keyword will typically produce an open-shell singlet state unless the electronic ground state is a biradical,
in which case the first excited state can have a closed shell.
