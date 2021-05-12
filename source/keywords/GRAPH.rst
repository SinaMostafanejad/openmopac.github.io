.. _GRAPH:

``GRAPH``
=========

Information needed to generate electron density contour maps can be
written to an unformatted file, <name>.gpt, by using the keyword
``GRAPH``. ``GRAPH`` first calls MULLIK in order to generate the
inverse-square-root of the overlap matrix, which is required for the
re-normalization of the eigenvectors. All data essential for the
graphics package DENSITY are then output.
