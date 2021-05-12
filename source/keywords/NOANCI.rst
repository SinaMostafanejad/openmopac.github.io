.. _NOANCI:

``NOANCI``
==========

RHF open-shell derivatives are normally calculated using Liotard's
analytical C.I. method [`43 <references.html#analci>`__]. In general, do
*not* use ``NOANCI`` (NO ANalytical Configuration Interaction
derivatives). ``NOANCI`` should *only* be used if there is cause to
believe that the derivatives are faulty, because it evaluates the
gradient using finite differences involving complete SCF calculations.
In contrast, Liotard's method is very fast, so using ``NOANCI`` will
cause the job to take much longer than if ``NOANCI`` were *not* used.

In the unusual situation when analytical C.I. derivatives are *not* to
be used, specify ``NOANCI``. See also
```GRADIENTS`` <gradients_discussion.html#derivs>`__.
