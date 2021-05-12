.. _LOCATE-TS:

``LOCATE-TS``
=============

``LOCATE-TS, LOCATE-TS(C:[n.nn[,n.nn[,n.nn...]]][;Set:m])``

Description
-----------

This function was developed specifically for locating transition states
in enzyme-catalyzed reactions, but can be used for more general
reactions.

The objective of ``LOCATE-TS``\ is to locate and refine a transition
state joining two stationary points in a reaction.  These points are
more commonly referred to as reactants and products, but for convenience
in this description these geometries will be referred to as **A** and
**B**.  **A** and **B** are used because during the calculation the
geometries will be modified as they move towards each other, and would
therefore no longer be stationary points.  In ``LOCATE-TS,``\ the
geometry optimization is performed on both **A** and **B**
simultaneously.   For small systems consider using
```SADDLE`` <saddle.html>`__.

The function being optimized is:

 ΔH:sub:`f`' = ΔH\ :sub:`f\ A` + ΔH\ :sub:`f\ B`
+cΣ\ :sub:`i`\ (X:sub:`A`\ :sup:`i` - X\ :sub:`B`\ :sup:`i`)\ :sup:`2`

where ΔH\ :sub:`f\ A` and ΔH\ :sub:`f\ B`  are the calculated heats of
formation of **A** and **B**, respectively. "c" is a constant, in
kcal/mol/Ångstrom\ :sup:`2`, and X\ :sub:`A`\ :sup:`i` and
X\ :sub:`B`\ :sup:`i` are the coordinates of atom "i" in the **A** and
**B**, respectively. 

Advice on using\ ``LOCATE-TS``
------------------------------

Both geometries used must be as good as possible: They should be
stationary points on the Potential Energy Surface (PES); they should
include PDB data, either by using a PDB file or, more commonly, by using
the normal MOPAC data-set format, and having the atoms labeled with PDB
data.

It is helpful to have all the files involved located in the same
folder.  Although not essential, this will make the job of defining
``GEO_DAT``\ and ``GEO_REF`` easier.

Because of the large probability of introducing errors into the data
sets, instead of preparing specific data-sets it is safer to define the
geometries to be used using ```GEO_DAT`` <geo_dat.html>`__ and
```GEO_REF`` <geo_ref.html>`__, and having these keywords point to ARC
files.  This results in a very small data set.  For example, if the
reactant geometry is in Step_1.arc and the product geometry is in
Step_2.arc, the data set would be as follows:

**Example of a complete data set for LOCATE-TS**

**LOCATE-TS GEO_DAT="Step_1.arc" GEO_REF="Step_2.arc" EPS=78.4**

``EPS`` is specified here, because using implicit solvation gives a more
realistic model for biochemical reactions.   Keyword  ``LOCATE-TS``
causes the ```MOZYME`` <mozyme.html>`__ function to be used, so there is
no need to add keyword ``MOZYME``, if it is supplied, it will be
ignored.

WARNING:\ **The quality of the transition state geometry is normally not
very good.  It's good enough to allow tests, such as**
```FORCE`` <force.html>`__ **and inspection using a GUI, to be run to
verify that it is, in fact, a transition state, but the heat of
formation is likely to be in error because the geometry is not fully
optimized. Unless corrected, this fault would compromise any comparison
of transition-state heats of formation with heats of formation of
ground-state systems.  This correction is not done automatically -
finding transition state geometries requires a lot of CPU time, and,
often at the start of a project, many attempts will fail.  So rather
than perform a lengthy geometry optimization on a faulty transition
state, a "quick and dirty" job is done.  Once a good transition state is
found, it can then be refined as follows:**

**Reactions involving bond making and bond breaking, i.e., chemical reactions**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geometries resulting from transition state refinement could be regarded
as being composed of two sets: those atoms directly involved in the
reaction, and all other atoms. As a result of the refinement the
positions of all atoms in the first set, typically 7 or fewer, would be
highly optimized. By freezing the positions of these atoms and then
running the second geometry optimization procedure, the geometry of the
entire transition-state system could be optimized to the same precision
as that used for stable intermediates. In test calculations, a gradient
minimization was performed using the atoms in the first set to verify
that this operation did not introduce spurious forces; in all cases,
this resulted in only insignificant changes in the heat of formation and
in the positions of the atoms.  Use ```INVERT`` <invert.html>`__ to
quickly switch optimization flags.

If keyword ``LET`` is present, docking of the two systems will not be
performed in a ``LOCATE-TS`` job.  This is useful in small systems if
the atoms are in the same order in the reactants and products.  Avoid
using ``LET``\ in large systems, instead identify any mis-matches and
edit the reactants or product labels to correct the error.  

**Reactions involving only conformational changes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transition states between different conformers can be located using
``LOCATE-TS``. As with chemical reactions, conformational changes
involve "reactants" and "products," but no bonds are made or broken. 
Once the approximate transition state is located, it can be refined
using ```TS`` <ts.html>`__ or other transition-state refinement method.
Unlike the refinement when chemical reactions are modeled, ``INVERT``
cannot be used because no bonds are made or broken.

Worked exercise in locating a transition state.
-----------------------------------------------

A complete enzyme catalyzed mechanism for the hydrolysis of a peptide
bond is given in `Chymotrypsin
Mechanism <Chymotrypsin_mechanism.html>`__.  The worked exercise
involves determining the transition state for the first reaction step. 
Except for Step 3 => Step 4, the other steps are similar.

Download `Step_1.arc <Step_1.arc>`__ and `Step_2.arc <Step_2.arc>`__ and
store them in a new folder.  In the same folder, create a text file,
Step_1_2_Transition_State.mop.  Edit this file to add the text in the
above example.  Run the job using MOPAC.  It should run for about one
day.  If an ARC file is generated, the test was successful.  If it was
not generated, please contact me at MrMOPAC@ATT.net, and send me the
data set and output files. 

How  LOCATE-TS works
--------------------

The process that LOCATE-TS uses is as follows: The reference data set
geometry, defined using ```GEO_REF`` <geo_ref.html>`__, is rotated and
translated to put it into the best overlap with the geometry from the
input data set.  At this point, the two geometries are likely to be
quite different.  This difference can be expressed as a distance,
defined as the square root of the sum in the above equation.  Typical
distances in enzyme chemistry are in the order of 50 - 300Å.  Geometry
optimization is then started, using a small value for "c," by default
this is 3 kcal/mol/Ångstrom\ :sup:`2`.  The first step consists of
solving the SCF equations using the ```MOZYME`` <mozyme.html>`__
technique.  (There is no need to specify ``MOZYME``, the presence of
``LOCATE-TS`` implies ``MOZYME``.)  All subsequent steps use the
wavefunction from this initial SCF calculation, and the pull exerted by
the "c" term. This causes the two geometries to move towards each other
without imposing a large stress. During this process, the distance will
typically drop by a large amount - the two geometries can be regarded as
moving across an almost level plane until they stop near the bottom of
the activation barrier.  The value of "c" is then increased; the new
default value is 30 kcal/mol/Ångstrom\ :sup:`2`.  This large pull then
moves **A** and **B** up the barrier to near to the transition state. 
As with the previous step, the first point involves solving the SCF
equations, and all subsequent points use the frozen wavefunction.  This
optimization is repeated a few times using the same value of "c" to
ensure that the wavefunction is sufficiently relaxed.  When the
optimization is finished the geometries of **A** and **B** are almost
the same, with one on each side of the transition state.

An estimate of the transition state geometry, **C**,  is obtained by
averaging the two geometries.  The next few steps involve a pair of
operations, each pair being repeated a small number of times, typically
two to five times.  The first of this pair of operations involves
geometry optimization of **C**, while holding fixed all atoms involved
in bond making or bond breaking, i.e. optimizing the positions of all
atoms except those in the active site.  The second step involves
transition state location, i.e., gradient minimization, but this time
using only the atoms in the active site. 

Options for LOCATE-TS
---------------------

``LOCATE-TS``
~~~~~~~~~~~~~

``LOCATE-TS`` can be used on its own, i.e., without any of the terms in
the square brackets; if that is done, then the default optimization
procedure is used, and output is small.  The default optimization can be
reproduced using ``LOCATE-TS(C:3,30,30,30;SET:1)``

About half the time the default ``LOCATE-TS`` does not finish correctly.
Almost always the first big step, moving the reactants and products up
the reaction barrier, runs correctly, and most of the time when failures
occur they occur in the refinement of the transition state. Because of
this behavior, at the end of the first big step three data sets are
generated that can then be used in attempting to refine the transition
stae.  These data sets have the names **<name>_30p0_first.mop**, 
**<name>_30p0_second.mop**, and  **<name>_30p0_average.mop**.  
**<name>_30p0_first.mop** is the final geometry generated from the
original data set (the reactant) or by the file defined by ``GEO_DAT``. 
**<name>_30p0_second.mop** is the final geometry from ``GEO_REF``.
**<name>_30p0_first.mop** and **<name>_30p0_second.mop** are thus the
geometries on each side of the transition state, near the top of the
reaction barrier.  An approximation to the transition state geometry is
the average of these two structures, this is given in
**<name>_30p0_average.mop**.  The final value of "c" used is indicated
by the text "**30p0**"  This specific case represents a value of "c" of
30.0 kcal/mol/Ångstrom\ :sup:`2`.

``LOCATE-TS(C:30,30,30,40,40;SET:1)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``LOCATE-TS`` does not finish correctly, examine the structures on
each side of the transition state.  If these look correct, then try to
refine them by using this option.  Do not start with a constraint lower
than the last value used in the previous run - if the constraint is
lowered, the two systems will move away from the transition state. 
Using options of the type shown here increases the possibility that the
refinement would work correctly because the refinement would be started
with a geometry that was nearer to the transition state.

If the structures on each side of the transition state do not look
correct, then start over with a more cautious set of constraints.  An
example of such a cautious set would be
``LOCATE-TS(C:1,3,10,20,25,25;SET:1)`` This starts the procedure with a
small penalty function, 1.0 kcal/mol/Ångstrom\ :sup:`2` followed, in
order, by increasing biases, until a penalty of 25.0
kcal/mol/Ångstrom\ :sup:`2` is used. The transition state would then be
refined using Set 1, i.e., all atoms involved in bond making or bond
breaking.

When this form of the keyword is used, the output will be larger, and
intermediate files generated; these files can then be used in locating
the transition state manually.  The number of constraints used can be
decreased to zero or increased up to 20.  Two main options for the size
of the active site are provided. ``SET:1`` consists of only those atoms
involved in bond making or bond breaking and ``SET:2`` which consists of
``SET:1`` plus nearest neighbors.

``LOCATE-TS(C:0.001,0.002,0.005,0.010,0.020,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200)  NOSWAP``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Used when reactions involving conformational changes are being modeled. 
Because no bonds are made or broken, ";SET:x" is not used.  Because
conformational changes typically involve large geometric changes the
starting bias is very small. For the same reason, keyword
```NOSWAP`` <noswap.html>`__ is also used.

``LOCATE-TS(C:;SET:1)``
~~~~~~~~~~~~~~~~~~~~~~~

The two data sets used by  ``LOCATE-TS`` are passed directly, i.e.,
without modification, to the transition state refinement operation. If
the two geometries are near to the transition state, there is an
increased probability that the process for recognizing bond-breaking and
bond making operation will not work correctly.  To avoid problems with
this operation, use the next option, *vis* ``LOCATE-TS(SET:1).``

``LOCATE-TS(SET:1)``
~~~~~~~~~~~~~~~~~~~~

This option uses only one data-set, usually the one generated by an
earlier run, e.g., **<name>_30p0_average.mop. ** Carefully define the
atoms involved in bond-breaking and bond-making by setting their
optimization flags set to "1", all other optimization flags being set to
zero. When this option is used the option for "``SET:2``" is
meaningless.

   ``LOCATE-TS`` was developed and optimized for use with enzymes.  It
can be used for other species, but the probability of success is lower.

 

When Things Go Wrong
--------------------

Quite often, particularly with difficult reactions, e.g., hydride,
H\ :sup:`-`, migration, the gradient minimizer might fail to produce a
valid geometry. When this happens, have a look at the geometry in
"<filename> Loop1.mop"  If it looks reasonable, proceed as follows:

Edit the set of keywords to convert it into a normal transition-state
optimization calculation.  This will involve deleting the keywords
``GEO_REF`` and ``LOCATE-TS``, and adding the keywords ``MOZYME``,
``TS``, ``GNORM=3``.  The geometry already has the flags set for the
atoms involved in the reaction.  Run that job.  It will likely fail, but
the resulting geometry will likely be nearer to the transition state,
and if that geometry is run, the gradient minimization will likely
work.  Well, it did work on several difficult transition states.

At this point, a reasonable question is, why doesn't MOPAC do this
itself.  The short answer is "Yes, it should."  The longer answer is,
someone has to write the software to do this.  An even longer answer is,
there should be better gradient minimizers.  Until work on this is done,
the process just described is the best that exists in MOPAC.

If ``LOCATE-TS`` fails to produce a reasonable transition state, it is
possible to get better geometries for the reactants and products, i.e.,
geometries on each side of the transition state.  In addition, the
average of these geometries might be a useful approximation to the
transition state.  When ``LOCATE-TS`` is run it produces a set of
data-set files for each value of bias used, one for the reactants, one
for the products, and one for the average.  These can be identified by
the value of the bias and the words "first", "second", and "average" in
the the file-names.  If the transition state geometry was correct, then
delete these intermediate geometries.  If it is not correct, look at
these files to see if anything useful can be found.  In particular, look
for intermediate geometries that are on the slope of the activation
barrier.  These might be useful in restarting the transition state
location.

 

TS, SIGMA, NLLSQ
~~~~~~~~~~~~~~~~

Three different gradient optimization methods can be used: Baker's
Eigenfollowing method ```TS`` <ts.html>`__, the McIver-Komornicki
gradient minimization method ```SIGMA`` <sigma.html>`__, and Bartel's
```NLLSQ`` <nllsq.html>`__. If one of these keywords is present, that
method will be used. Otherwise, Baker's Eigenfollowing method will be
used by default. 

Complete worked examples of ``LOCATE-TS``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``LOCATE-TS`` was used to locate transition states in the `chymotrypsin
mechanism <Chymotrypsin_mechanism.html>`__.  To reproduce this
mechanism, download the ARC files for the intermediates (Step 1 to Step
6), and use the ``LOCATE-TS`` keyword in the transition state stationary
point arc files.

A simple worked example of a conformational change is
`provided <Test%20of%20LOCATE-TS%20using%20Nitrogen%20inversion.zip>`__
by the inversion of a nitrogen atom in triethanolamine.

 

 

 
