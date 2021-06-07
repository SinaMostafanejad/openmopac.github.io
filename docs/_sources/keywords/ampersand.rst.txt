.. _ampersand:

\&
==

A line of keywords containing ``&`` indicates that the next line is also a line of keywords rather than a line of comments.
The position of ``&`` within the line of keywords doesn't matter.
Starting from the standard input file structure of

::

  KEYWORD1 KEYWORD2 KEYWORD3
  COMMENT1
  COMMENT2
  GEOMETRY

one line of comments can be replaced through one use of ``&`` as

::

  KEYWORD1 &
  KEYWORD2 KEYWORD3
  COMMENT1
  GEOMETRY

and both lines of comments can be replaced through two uses of ``&`` as

::

  KEYWORD1 &
  KEYWORD2 &
  KEYWORD3
  GEOMETRY

This keyword is intended to improve the readability of long keyword lines.

.. warning::
  A single keyword list can only contain one type of line extender: ``&`` or ``+``.
