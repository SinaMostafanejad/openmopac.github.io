.. _GEO_DAT:

``GEO_DAT``
===========

``GEO_DAT`` provides an alternative method for supplying a geometry for
a job.   If more than one line of keywords is supplied, then this
keyword should be on the first line.

Ways to specify "*text*" :

| ``GEO_DAT="CRAMBIN 1CBN X-ray.mop``"
| ``GEO_DAT``\ ``="CRAMBIN.arc``"
| ``GEO_DAT="CRAMBIN.pdb``"
| ``GEO_DAT``\ ``="./CRAMBIN.arc``"
| ``GEO_DAT``\ ``="../CRAMBIN.arc``"
| ``GEO_DAT="../../arc files/C``\ RAMBIN.arc"
| ``GEO_DAT``\ ``="sub folder/CRAMBIN.arc``"
| ``GEO_DAT``\ ``=``"./sub folder/CRAMBIN.arc"
| ``GEO_DAT``\ ``="M:\data sets\CRAMBIN 1CBN X-ray.mop``"
| ``GEO_DAT``\ ``="/Users/jstewart/data_sets/CRAMBIN_1CBN_X-ray.mop``"
| ``GEO_DAT``\ ``="~/data_sets/CRAMBIN_1CBN_X-ray.mop``"

Only the geometry in the file specified by ``GEO_DAT`` will be used,
i.e., all keywords, comments, etc., will be ignored.

Warning: If ``GEO_DAT`` refers to a file that has the same name as the
data-set, but with a different suffix, and the data-set generates a file
with that suffix, then the file referred to by ``GEO_DAT`` will be
over-written.  For example, if ``GEO_DAT`` refers to test.arc, and the
data set name is test.mop, and the run would generate a file called
test.arc, then the original test.arc will be over-written.  If test-mop
is run again, then different results might be obtained, because the file
referred to by ``GEO_DAT`` had changed.

See also ```LOCATE-TS`` <Locate-TS.html>`__ and
```GEO_REF`` <geo_ref.html>`__
