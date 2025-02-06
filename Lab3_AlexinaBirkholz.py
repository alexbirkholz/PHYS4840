import numpy as np
import matplotlib.pyplot as plt
import sys
import Birkholz_functions_lib as mfl

filename = 'NGC6341.dat'
blue, green, red = np.loadtxt(filename, usecols=(8,14,26), unpack=True)
quality_cut_red = np.where(red > 5)
magnitude = blue
color = blue - red

fig, ax = plt.subplots()
ax.plot(np.log10(magnitude), np.log10(color), marker='.')
plt.show()
