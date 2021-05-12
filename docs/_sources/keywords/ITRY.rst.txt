.. _ITRY:

``ITRY``
========

The default maximum number of SCF iterations is 2000. When this limit
presents difficulty, ``ITRY=nn`` can be used to re-define it. For
example, if ``ITRY=4000`` is used, the maximum number of iterations will
be set to 4000. ``ITRY`` should normally not be changed until all other
means of obtaining a SCF have been exhausted, e.g. ``PULAY``,
``CAMP-KING``, etc.

If ``ITRY`` is set to 0, 1, or 2, then that number of iterations will be
run then the SCF calculation will be stopped, and the normal output
generated.  This option is useful when the SCF needs to be started, but
the results of the SCF are not needed.
