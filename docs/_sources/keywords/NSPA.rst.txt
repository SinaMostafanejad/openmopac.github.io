.. _NSPA:

``NSPA``
========

Used for the COSMO method (see ``EPS``) to set the number of geometrical
segments per atom to *n*. This keyword should seldom be used, as the
default value (42) should be adequate. However, for high-precision work
a larger value from the set 3\ :sup:`i` x j\ :sup:`2` x 10 + 2  should
be used (e.g., 92,122, or 162).  See also ``DVFILL``

Examples of NSPA

In these examples, the surface of a single atom is outlined in terms of
geometric segments.  All segments are triangles, although some lines
indicating edges in the following diagrams are missing.

NSPA=42

             

|image0|.

NSPA=92

|image1|.

NSPA=122

|image2|.

.. |image0| image:: cos_42.gif
   :width: 410px
   :height: 247px
.. |image1| image:: cos_92.gif
   :width: 415px
   :height: 256px
.. |image2| image:: cos_122.gif
   :width: 419px
   :height: 254px
