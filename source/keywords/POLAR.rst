.. _POLAR:

``POLAR``
=========

This calculates the polarizability and first and second
hyperpolarizabilities [`47 <references.html#polar>`__] This routine has
been completely re-written by Prof Henry Kurtz and Prakashan Korambath,
of Memphis State University.

The POLAR calculation now gives the frequency-dependent NLO properties
(α, β, and γ) at user-defined frequencies. 

See `units <polarizability.html>`__.

If a POLAR calculation gives the message "Calculation of polarizability
failed (This part of MOPAC is fragile)," and only the polarizability is
needed, use ```STATIC`` <static.html>`__

In 2004, the polarizability volume reported was modified by the use of
`additive corrections <additive_corrections.html>`__.

| 

Examples of ``POLAR`` keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description of `user-definable
terms <time_dependent_hartree_fock.html>`__ in POLAR keyword.

| To calculate the NLO quantities *α, β, and γ* at 1.0eV:
| ``POLAR(E=(1.0))``
| This same calculation can be set up by setting all the variables to
  their default value:

::

   POLAR(IWFLB=0,E=(1.),BETA=0,GAMMA=1,TOL=1.D-3,MAXITU=500,MAXITA=150,BTOL=1.D-3)

This takes up the entire keyword line. If more than one line is needed
to hold the keyword, use the ``+`` option, as in:

::

   + symmetry 1scf uhf POLAR(IWFLB=0,E=(1.),BETA=0,GAMMA=1,TOL=1.D-3,MAXITU=501,
    MAXITA=151,BTOL=1.D-3)

Note: This is not a recommended way of writing a keyword. In order for a
keyword to be recognized, the 'join' of the two lines must be perfect.
In other words, the last character of the first line must be in column
80, unless character 1 was not blank, in which case the last character
must be in column 79. Anyhow, it is unlikely that such long keywords
would be used very often.
