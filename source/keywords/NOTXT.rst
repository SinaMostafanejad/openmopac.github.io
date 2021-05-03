.. _NOTXT:

``NOTXT``
=========

When ``NOTXT``\ is present, all text associated with an atom symbol is
deleted when the ARC file or some OUT files are generated.  E.g., if an
ARC file would normally have text:

::

      N(     1 CYS*  1)  13.94944700 +1  19.84245900 +1  23.08322500 +1                     0.0000
     C(     2 CYS*  1)  14.44344800 +1  18.75345800 +1  23.94622600 +1                     0.0000
     C(     3 CYS*  1)  13.82944700 +1  18.85446000 +1  25.33422500 +1                     0.0000

if ``NOTXT`` were present, the equivalent lines in the ARC file would
look like this:

::

      N  13.94944700 +1  19.84245900 +1  23.08322500 +1                     0.0000
     C  14.44344800 +1  18.75345800 +1  23.94622600 +1                     0.0000
     C  13.82944700 +1  18.85446000 +1  25.33422500 +1                     0.0000

This keyword is useful when the geometry in the ARC file is needed as
input to a GUI or format converter,

 

 
