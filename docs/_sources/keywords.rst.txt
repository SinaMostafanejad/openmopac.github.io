Keywords
========

By default, MOPAC input files contain one line of keywords followed by two lines of comments.
MOPAC's keywords are strings that can include letters, numbers, and special characters excluding ``=``, ``(``, ``)``, and whitespace.
While the MOPAC documentation and source code refer to all keyword letters as being uppercase,
the specification of keywords in the input file is not case sensitive.

Keywords either appear by themselves or with the specification of additional values that can be integers, real numbers, or strings.
In some cases, one or more of these additional values is optional.
The standard syntax is ``KEYWORD=value`` for one value and ``KEYWORD=(value1,value2,...,valueN)`` for multiple values,
with no extra whitespace.
MOPAC can parse real numbers in scientific notation with ``d``, ``D``, ``e``, or ``E`` separating the mantissa and exponent.
Values that are strings should be delineated by ``"`` if they contain whitespace, ``,``, ``(``, or ``)``.
In older versions of MOPAC, some keywords deviate from this syntax and the present version maintains backward compatibility with older syntax,
which otherwise is not specified here.

Each keyword has its own webpage that describes its usage and specifies the number, type, and purpose of its additional values.

.. rubric:: Glossary

.. include:: glossary.txt

.. toctree::
  :hidden:

  keywords/list_num
  keywords/list_A
  keywords/list_B
  keywords/list_C
  keywords/list_D
  keywords/list_E
  keywords/list_F
  keywords/list_G
  keywords/list_H
  keywords/list_I
  keywords/list_J
  keywords/list_K
  keywords/list_L
  keywords/list_M
  keywords/list_N
  keywords/list_O
  keywords/list_P
  keywords/list_Q
  keywords/list_R
  keywords/list_S
  keywords/list_T
  keywords/list_U
  keywords/list_V
  keywords/list_W
  keywords/list_X
  keywords/list_Y
  keywords/list_Z
