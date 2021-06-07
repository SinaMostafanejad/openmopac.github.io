.. _plus:

\+
==

A line of keywords containing ``+`` indicates that another line of keywords is being added as the next line of the input file.
The position of ``+`` within the line of keywords doesn't matter.
Starting from the standard input file structure of

::

  KEYWORD1 KEYWORD2 KEYWORD3
  COMMENT1
  COMMENT2
  GEOMETRY

one extra line of keywords can be added through one use of ``+`` as

::

  KEYWORD1 +
  KEYWORD2 KEYWORD3
  COMMENT1
  GEOMETRY

and another extra line of keywords can be added through two uses of ``&`` as

::

  KEYWORD1 &
  KEYWORD2 &
  KEYWORD3
  GEOMETRY

Only two extra lines of keywords are allowed to be added in this manner.
This keyword is intended to improve the readability of long keyword lines.

.. warning::
  A single keyword list can only contain one type of line extender: ``&`` or ``+``.
