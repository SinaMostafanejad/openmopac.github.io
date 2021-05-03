.. _TRIPLET:

``TRIPLET``
===========

The triplet state is defined. In order to define this type of
calculation other keywords *must* also be used. For a 'simple' triplet
calculation, use ``C.I.=2``. Results from such calculations can be
compared with ground state calculations. If the triplet state consists
of two half-filled degenerate M.O.s, such as molecular oxygen, then
``OPEN(2,2)`` should be used.

From experience, ``OPEN(2,2)`` and ``TRIPLET`` run faster than
``C.I.=2`` and ``TRIPLET``.

If the system has an odd number of electrons, an error message will be
printed.

See also ```MS=n`` <ms.html>`__,
``SINGLET, DOUBLET, QUARTET, QUINTET, SEXTET, SEPTET, OCTET,`` and
``NONET``.

UHF interpretation:

The number of alpha electrons exceeds that of the beta electrons by 2.
If ``TRIPLET`` is not specified, then the numbers of alpha and beta
electrons are set equal. This does not necessarily correspond to a
singlet.

RHF interpretation:

````

TRIPLET cannot be used unless other keywords are present. If ``C.I.=2``
is used, then a single state corresponding to:

.. raw:: html

   <div align="CENTER">

|begin{displaymath}frac{1}{sqrt{2}}(psi_{homo}^{alpha}.psi_{lumo}^{beta}+psi_{homo}^{beta}.psi_{lumo}^{alpha})end{displaymath}|

.. raw:: html

   </div>

is calculated. See keywords ``C.I.=n`` and ``OPEN(n1,n2)``.  

When the configuration interaction calculation is done, all microstates
having a component of spin, M\ :sub:`S`, equal to 1 are selected. These
microstates are then used in the construction of states. Because of the
way in which the microstates were chosen, only states of spin equal to
or greater than 1 can be constructed. From this set, only a triplet
state can be selected, all other states will be ignored. If ``ROOT=n``
is present, then the *n*'th triplet state will be selected, otherwise
the first triplet state will be chosen.

.. |begin{displaymath}frac{1}{sqrt{2}}(psi_{homo}^{alpha}.psi_{lumo}^{beta}+psi_{homo}^{beta}.psi_{lumo}^{alpha})end{displaymath}| image:: img184.gif
   :width: 202px
   :height: 42px
