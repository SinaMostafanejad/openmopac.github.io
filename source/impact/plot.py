import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})

year, citations = np.loadtxt("citations.txt", comments="#", unpack=True)

plt.figure(figsize=(8,4))

plt.ylim(0,1200)
plt.xlim(1980,2025)

plt.errorbar(year, citations*0.72, yerr=citations*0.03, ms=3.5, marker='s', ls='', color='red')
plt.title('MOPAC references in scientific publications')
plt.xlabel('year')
plt.ylabel('# of publications per year')

plt.savefig("plot.pdf",bbox_inches='tight',pad_inches=0.01)
