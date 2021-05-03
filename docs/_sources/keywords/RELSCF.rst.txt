.. _RELSCF:

``RELSCF``
==========

When ``RELSCF=n`` is present, the default SCF criterion is multiplied by
*n*. This is useful if the value of the default SCF criterion is not
readily available, as for example when ```PRECISE`` <precise.html>`__ or
any other keywords that modify the SCF criterion is used. Examples:
``RELSCF=10`` will make the SCF test easier to pass--the criterion will
be made 10 times easier. Similarly, if the results are not precise
enough, then ``RELSCF=0.1`` would increase the precision 10 times.
However, if the precision is increased too much, the SCF test might
never be passed. See also ``SCFCRT``.
