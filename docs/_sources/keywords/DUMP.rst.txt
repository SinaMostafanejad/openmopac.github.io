.. _DUMP:

``DUMP``
========

Restart files are written automatically at two hour CPU time intervals
to allow a long job to be restarted if the job is terminated
catastrophically. To change the frequency of dump, set ``DUMP=nn`` to
request a dump every *nn* seconds. Alternative forms are ``DUMP=nnM``,
``DUMP=nnH``, ``DUMP=nnD`` for a dump every *nn*\ minutes, hours, or
days, respectively. ``DUMP`` only works with geometry optimization,
gradient minimization, path, ``IRC, DRC``, and ``FORCE`` calculations.
It does not (yet) work with a ``SADDLE`` calculation.
