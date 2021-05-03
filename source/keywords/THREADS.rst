.. _THREADS:

``THREADS=n``
=============

By default, the maximum number of threads are used.  To reduce this
number, use ``THREADS=n``, where ``n`` is the number of threads to be
used.

If ``n`` is greater than the maximum, it will be re-set to the maximum. 
If ``n`` is less than 1 it will be re-set to 1.

The maximum number of threads is normally equal to the number of cores,
even if each core supports two threads.

In the special case of ``THREADS=1``, parallelization is switched off.

See also ```NOGPU`` <nogpu.html>`__.
