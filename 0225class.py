#!/user/bin
import Birkholz_functions_lib as mfl
import numpy as np
import matplotlib.pyplot as plt
h = 10e-10
#Using this h value derived in class caused a numpy.core._exceptions._ArrayMemoryError so I reduced the number

x=np.arange(-2,2,0.001)

derivative_approx = mfl.cd_approx(mfl.f, x, 0.001)
derivative_analytic = mfl.tanh_deriv_analytical(x)

plt.scatter(x,derivative_approx, label="Central Difference", s=0.1, color ="red")
plt.plot(x, derivative_analytic, label="Analytical", color="blue")
plt.title("Derivative of tanh via Central Difference and Analytical Methods")
plt.legend()
plt.show()

