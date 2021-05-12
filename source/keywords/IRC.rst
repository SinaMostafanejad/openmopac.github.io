.. _IRC:

``IRC``
=======

An `Intrinsic Reaction Coordinate <DRC_coordinates.html>`__ calculation
to be run.  The following options are provided:

IRC=1 and IRC=1\*

This option is intended for use with a transition state. The path from
the transition state to either the reactants or the products is
generated. The path generated depends on the coefficients of the
eigenvectors of the normal mode.  There is no easy *a priori* way of
determining what the phase of these coefficients is, so try running
``IRC``\ =1, and see if it goes the correct way.  If not, use
``IRC``\ =-1. If ``IRC``\ =1\* or ``IRC``\ =-1\* is used, then the
entire `reaction path <DRC_IRC_Description.html>`__, from reactants or
products, through the transition state, to products or reactants, is
mapped.  If DRC is present, then the system is given an initial
perturbation in the positive normal coordinate, then the DRC, i.e., the
total energy conserved path, is calculated.  A simple graph will be made
if ```HTML`` <html.html>`__ is added.

These two options require the normal mode for the reaction.  A
```FORCE`` <force.html>`__ or ```FORCETS`` <force.html>`__ calculation
must be run in order to generate the normal mode.  As this is
computationally expensive, a useful strategy is to run the ``FORCE`` or
``FORCETS`` calculation and use ```ISOTOPE`` <isotope.html>`__ to save
the results.  Then the IRC calculation can be run using, e.g., ``IRC=1``
``RESTART``.  If ``RESTART``\ is not present, a FORCE calculation will
automatically be run first.

IRC=+\ *n* or IRC=\ *n*

Normally used with ```DRC`` <drc0.html>`__, this option perturbs the
system along the *n*'th normal mode.  One quantum of kinetic energy is
added, the value of the quantum being that of the associated vibrational
energy.  This option allows the exact normal mode to be mapped out. 
IRC=n with DRC can be used with both ground and transition state
systems.  If IRC=1 and DRC is used with transition states, it would map
out the dynamic path from the transition state to reactants or products.

IRC=-n

The same as IRC=+\ *n*, except the initial perturbation is in the
opposite direction. Except for transition states, this option can be
duplicated by one of the other options described here.

When studying reaction paths involving transition states, one option,
although implied logically from the above description of the IRC, should
not be used.  The option IRC=\ *n*, where  *n* is not equal to 1 or -1,
is meaningless.  To see why, consider the option IRC=1.  That maps the
reaction path, and uses the lowest transition state normal mode, i.e.
the mode with the imaginary frequency.  Any other mode would simply
return to the transition state, in other words, it would do nothing
useful.

By default, all steps that are calculated are printed.  To produce a
more meaningful graph, use keyword ```X-PRIORITY`` <x-priority.html>`__.
