.. _SCFCRT:

``SCFCRT=n.nn``
===============

``SCFCRT``\ sets the self-consistent field criterion, i.e., the change
in energy in kcal/mol on two successive iterations. For most situations
where the SCF criterion need to be modified, use
```RELSCF`` <relscf.html>`__ instead.  ``RELSCF`` is useful if the value
of the default SCF criterion is not readily available, as for example
when ```PRECISE`` <precise.html>`__ or any other keywords that modify
the SCF criterion is used. The default SCF criterion,1x10\ :sup:`-4`
kcal/mol, is to be replaced by that defined by ``SCFCRT=n.nnn``.  Other
criteria may make the requirements for an SCF slightly more stringent.
The SCF criterion can be varied from about 1.0 to 1.D-25, although
numbers in the range 0.1 to 1.D-9 will suffice for most applications.

In ```FORCE`` <force.html>`__, ```NLLSQ`` <nllsq.html>`__, 
```SIGMA`` <sigma.html>`__, or ```TS`` <ts.html>`__ calculations, the
default value of ``SCFCRT`` is 1x10\ :sup:`-7`. Be careful in
``FORCE``\ calculations - high precision is needed, if high precision is
not used, the vibrational frequencies might be wrongly predicted.

An overly tight criterion can lead to failure to achieve an SCF, and the
consequent failure of the run.  See also ```RELSCF`` <relscf.html>`__
and ``PRECISE``
