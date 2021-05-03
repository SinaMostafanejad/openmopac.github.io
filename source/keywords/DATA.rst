.. _DATA:

``DATA="<text>"``
=================

| Normally, MOPAC reads data from the data-file supplied.  When the name
  of the data set cannot be changed, the data set to be used can be
  provided in the fixed data set by use of ``DATA="<text>". `` Thus if
  the name of the fixed data set is "input.dat", so the only job that
  can be run is:
| MOPAC input.dat

and the job that is to be run is the data set "toluene.mop" in folder
"F:\my mopac jobs" then the file input.dat would contain the single
line:

DATA="F:\my mopac jobs\toluene.dat"

When the MOPAC job is run, input.dat would be read in, then because
'DATA="F:\my mopac jobs\toluene.dat"' was present, the file toluene.dat
would be read in.  The results would be put into files of the type
input.<suffix>.
