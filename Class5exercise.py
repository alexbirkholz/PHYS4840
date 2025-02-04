#!/usr/local/Anaconda2023/bin/python

#####################################
#
# Class 5: Linear and Log + Plotting
# Author: < Alexina Birkholz > 
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

## in your functions library, which should 
## be in a different file, define the function
#
# def y(x):
# 	y = 2.0*x**3.0
# 	return y
#
# and import your functions library

import Birkholz_functions_lib as mfl

# define your x values
x = np.linspace(1, 100, 500)  # x values
y = mfl.y(x)
plt.plot(y,x)
plt.xlabel('y')
plt.ylabel('x')
plt.show()
plt.plot(np.log10(y),np.log10(x))
plt.xlabel('y')
plt.ylabel('x')
plt.show()
plt.plot(y,x)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log y')
plt.ylabel('log x')
plt.show()
# (1) make a linear plot of y vs x
# (2) make a log-log plot of y vs x
# (3) make a plot of log(x) vs log(y)