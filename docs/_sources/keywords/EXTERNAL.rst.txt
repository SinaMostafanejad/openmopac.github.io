.. _EXTERNAL:

.. raw:: html

   <div class="WordSection1">

.. rubric:: ``EXTERNAL=name``
   :name: externalname

.. rubric:: Atom parameters
   :name: atom-parameters

Normally, all semiempirical parameters are taken from the module files
within MOPAC. When the supplied parameters are not suitable, as in an
element recently parameterized, and the parameters have not yet
installed in the user's copy of MOPAC, then the new parameters can be
inserted at run time by use of ``EXTERNAL=<filename>``, where
``<filename>`` is the name of the file which contains the new
parameters. If the file-name contains spaces, then enclose the filename
in quotation marks, e.g. ``EXTERNAL="E:\Test Data\Parameter Set". ``

<filename>contains a series of parameter definitions in the
format:\ ````

<Parameter> <Element> <Value of parameter>
where the possible parameters
are\ ``USS, UPP, UDD, ZS, ZP, ZD, BETAS, BETAP, BETAD, GSS, GSP, GPP, GP2, HSP, F0SD, G2SD, ALP, XFAC_xx, ALPB_xx, FNnm``\ ,\ ``n``\ =1,2,
or 3, and\ ``m``\ =1 to 10, and the elements are defined by their
chemical symbols, such as Si or SI.  So FN11 is the first "a" parameter
of the core-core term, FN12 is the second "a" parameter (if it exists),
FN21 is the first "b" parameter of the core-core term, and FN31 is the
first "c" parameter of the core-core term.

When new parameters for elements are published, they can be typed in as
shown. This file is ended by a blank line, the word END or nothing i.e.,
no end-of-file delimiter. An example of a parameter data file is given
in the Figure:

**Figure:** Use of ``EXTERNAL=name``

+-----------------------------------------------------------------------+
| ::                                                                    |
|                                                                       |
|        USS      Si    -34.08201495                                    |
|        UPP      Si    -28.03211675                                    |
|        UDD      Si     -6.0                                           |
|        BETAS    Si     -5.01104521                                    |
|        BETAP    Si     -2.23153969                                    |
|        Betad    Si     -1.0                                           |
|        ZS       Si      1.28184511                                    |
|        ZP       Si      1.84073175                                    |
|        ALP      Si      2.18688712                                    |
|        GSS      Si      9.82                                          |
|        GPP      Si      7.31                                          |
|        GSP      Si      8.36                                          |
|        GP2      Si      6.54                                          |
|        HSP      Si      1.32                                          |
|        BETAD    TC      -5.72433498                                   |
|        F0SD     TC      5.43488602                                    |
|        G2SD     TC      1.10687502                                    |
|        XFAC_Ag   I      2.0                                           |
|        ALPB_C   Rb      2.0                                           |
+-----------------------------------------------------------------------+

.. raw:: html

   </div>

INDO/S parameters
~~~~~~~~~~~~~~~~~

Since the parameter structure of INDO is different from NDDO methods,
the allowed parameter names are also different. The allowed values for
INDO are BETAS, BETAP, BETAD, NORBS, ZCORE, ZSP, ZD1, ZD2, ZWT1, ZWT2,
and FGi (i = 1-24). Note that in INDO many parameters for s and p
orbitals should be identical, so BETAS should be set to equal BETAP.
Both s and p orbital exponents are set up using ZSP.

Derived parameters do not need to be entered; they will be calculated
from the optimized parameters. All "constants" such as the experimental
heat of atomization are already inserted for all elements.

If a parameter is not set, e.g. UPP for hydrogen, do not attempt to
define the parameter as zero.  If a parameter that has not been defined
is given a defined value of zero, then it will become defined, and have
the value zero.  From that point on, it would be recognized as a defined
parameter, usually with disastrous results.  So do **not** use lines
such as:

.. raw:: html

   <div align="center">

+-----------------------------------------------------------------------+
| ::                                                                    |
|                                                                       |
|        UPP       H    0.0                                             |
+-----------------------------------------------------------------------+

.. raw:: html

   </div>

Derived parameters do not need to be entered; they will be calculated
from the optimized parameters. All "constants" such as the experimental
heat of atomization are already inserted for all elements.

Global parameters
~~~~~~~~~~~~~~~~~

Most users should not change the values of global parameters; because of
this, definitions of global parameters are not provided.  Users who need
to edit global parameters would normally have access to the source code
of MOPAC, and would be able to read and edit the parameters. 

Values of global parameters are set and re-set using EXTERNAL lines of
the type:

::

     PAR1 1.234
       PAR6 2.345
       PAR23 3.456

| Any other data on the line is ignored.
|  

 

 

 
