Keywords
========

By default, MOPAC input files contain one line of keywords followed by two lines of comments.
MOPAC's keywords are strings that can include letters, numbers, and special characters.
Keywords are separated by whitespace, and their order is irrelevant.
While the MOPAC documentation, output files, and source code treat all keyword letters as being uppercase,
the specification of keywords in the input file is not case sensitive.

Keywords either appear by themselves or with the specification of additional values that can be integers, real numbers, or strings.
In some cases, one or more of these additional values is optional.
The syntax for specifying these values is keyword-specific and not fully standardized.
For one value, the syntax is either ``KEYWORD=value``, ``KEYWORD(value)``, or ``KEYWORD-value``.
For multiple values, the syntax is either ``KEYWORD=(value1,value2,...,valueN)`` or ``KEYWORD(value1,value2,...,valueN)``.
In all cases, whitespace is not allowed in a keyword statement outside string values with delimiters.
MOPAC can parse real numbers in scientific notation with ``d``, ``D``, ``e``, or ``E`` separating the mantissa and exponent.
String values do not include a delimiter unless explicitly stated in the keyword syntax, either ``"string"`` or ``(string)``.

Older versions of MOPAC contain keywords that are no longer officially supported.
While MOPAC continues to support obsolete keywords to maintain backward compatibility,
they are not recommended or documented on this website.

Each keyword has its own webpage that describes its usage and syntax and specifies the number, type, and purpose of its additional values.

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
