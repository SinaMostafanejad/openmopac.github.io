.. _SMOOTH:

``SMOOTH``
----------

In some GRID or PATH maps, there are artifacts in the potential energy
surface, caused by the way the maps are generated.  To prevent these
artifacts, use SMOOTH.

In a grid map, the PES is constructed in the same way a field is
ploughed: A line is generated, left to right. At the end of the line, a
step is taken in the other direction, then a line is generated right to
left. Another step is taken, and the process continued until the "field"
is "ploughed".  The effect of SMOOTH is to plough the field again, in
reverse, then to plough it twice more, at 90 degrees to the original
direction. For each point, four separate calculations are done, one for
each ploughing.  The point with the lowest energy is then used.

In a path map, after the path has been generated, the direction is
reversed, and the path re-calculated.  As with the GRID map, the lower
energy conformer is used at each point.

A limitation of SMOOTH is that the calculation must be run without using
``RESTART``. 

Without "SMOOTH":

| :sub:`  >`\ \___________________\_
|   \_____________________\|
|   \|____________________\_
|   \_____________________\|
|   \|____________________\_
|   \_____________________\|
|   \|____________________\_
| :sub:`  <`\ \____________________\|
|  

With "SMOOTH", the following grids are also used:

Grid 2

| :sub:`  <`\ \___________________\_
|   \_____________________\|
|   \|____________________\_
|   \_____________________\|
|   \|____________________\_
|   \_____________________\|
|   \|____________________\_
| :sub:`  >`\ \____________________\|

Grid 3

|        \___     \___      \__\_
|   v    \|     \|     \|     \|     \|     \|     ^  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|_\_ \|     \|_\_ \|     \|_\_ \|     \|_\_ \|
|  

Grid 4

|         \___     \___      \__\_
|   ^    \|     \|     \|     \|     \|     \|     v
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|     \|     \|     \|     \|     \|     \|     \|  
|   \|_\_ \|     \|_\_ \|     \|_\_ \|     \|_\_ \|
|  
