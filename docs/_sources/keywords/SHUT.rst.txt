.. _SHUT:

The SHUT command
================

The SHUT command is not a keyword, instead it is a small command script
that can be used to send a message to a running MOPAC job to instruct it
to shut down in a tidy manner, and to generate restart and density
files.  When MOPAC reads the message, it increases the apparent CPU time
by 10,000,000 seconds (over 100 days).  This exceeds any reasonable job
time, so MOPAC behaves as if it had run out of time.

**Caveat**: Because the SHUT command stops a job in a tidy manner, it
will not stop a job if a time-consuming process such as an SCF is
running, instead it will wait until the process has finished.  This
means that if the process needs a lot of time to complete, it might
appear that SHUT has not worked.  SCF calculations are one of the most
time-consuming steps, so if a ```1SCF`` <one_scf.html>`__ job is run,
the job will normally go to completion even if the SHUT command is
issued.

**How SHUT works**

When a MOPAC job is running, it periodically checks a file called
<name>.end.  At the start of the run,  <name>.end is empty, that is, it
is a file with nothing in it.  While  <name>.end has nothing in it, the
job will continue normally.  If there is any text at all in  <name>.end
the next time MOPAC checks the file it will increase the apparent CPU
time by 10\ :sup:`7` seconds.  SHUT simply puts some text into
<name>.end.  The two scripts given below.

For WINDOWS:  Copy the script below and put it into a file called
shut.cmd.  Put shut.cmd into a folder in the PATH.  shut.cmd is used at
the command prompt in the folder where the job is running.  To use it to
shut down a job called <file>.mop, issue the command "shut <file>" ,
e.g.:

M:\> shut crambin

would issue the SHUTDOWN command to the running job crambin.

| Start of WINDOWS shut.cmd script:
| **echo off
  if exist %1.dat goto dat
  if exist %1.mop goto mop
  if exist %1.arc goto arc
  echo The file %1.mop, %1.dat, or %1.arc does not exist in this folder
  goto end
  :dat
  copy %1.dat %1.end
  goto end1
  :arc
  copy %1.arc %1.end
  goto end1
  :mop
  copy %1.mop %1.end
  :end1
  echo shutdown command issued to %1
  :end**
|  

For Mac and Linux:  Copy the script below and put it into a file called
shut.csh.  Change permissions on shut.csh to make it executable (chmod
+x shut.csh)  Put shut.csh into a directory in the PATH, or alias it in
the .bashrc or .cshrc scripts.  shut.csh is used at the command prompt
in the directory where the job is running.  To use it to shut down a job
called <file>.mop, issue the command "shut <file>" , e.g.:

~ > shut crambin

or

~ > shut crambin.mop

| would issue the SHUTDOWN command to the running job crambin.

Start of Linux and Mac file shut.csh:

::

   #!/bin/sh
   #
   #  SHUTDOWN command
   # Remove last four characters of file.
   #
   file=$1
   if [ `expr "$file" : ".*.mop"` -gt 0 ]; then file=${file:0:`expr $file : '.*'` -4}; fi
   if [ `expr "$file" : ".*.out"` -gt 0 ]; then file=${file:0:`expr $file : '.*'` -4}; fi
   if [ `expr "$file" : ".*.dat"` -gt 0 ]; then file=${file:0:`expr $file : '.*'` -4}; fi
   if [ `expr "$file" : ".*.arc"` -gt 0 ]; then file=${file:0:`expr $file : '.*'` -4}; fi
   echo Shutdown > $file.end

::

   The second form, ~ > shut crambin.mop, is useful if the name is long and has been supplied to "shut.csh" using "copy and paste."
