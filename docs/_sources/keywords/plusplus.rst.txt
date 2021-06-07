.. _plusplus:

\+\+
====

The presence of ``++`` in a line of keywords indicates that the next line of the input file is an additional line of keywords.
In its general usage, the position of ``++`` within the line of keywords doesn't matter.
Starting from the standard input file structure of

::

  KEYWORD1 KEYWORD2
  COMMENT1
  COMMENT2
  GEOMETRY

an extra line of keywords can be added using ``++`` as

::

  KEYWORD1 ++
  KEYWORD2
  COMMENT1
  GEOMETRY

An arbitrary number of extra keyword lines can be added in this manner.
This keyword is intended to improve the readability of long keyword lines.

The ``++`` keyword also has special behavior that allows a single keyword to be split over multiple lines.
In this usage, ``++`` must appear as the last two non-whitespace characters on a keyword line,
following the split keyword without any whitespace between them.
The split keyword must immediately continue on the next line without any leading whitespace.
Relative to the standard input file structure noted above, the generic syntax for this usage is

::

  KEY++
  WORD1 KEYWORD2
  COMMENT1
  GEOMETRY

where ``KEYWORD1`` refers to a string containing a keyword and any additional values that might be assigned to it.
A single keyword can be split over an arbitrary number of lines in this manner.
This special behavior is intended for keywords containing string values with a large number of characters.
