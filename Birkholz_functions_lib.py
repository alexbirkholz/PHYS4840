import numpy as np
def my_function (vector):
	a=vector[0]
	b=vector[1]
	c=vector[2]

	return np.linalg.norm(vector)

def cookiecalculate (cookielist,startdollars):
    for i in cookielist:
	    n=startdollars//cookiea
	    r=startdollars%cookiela
    print("the remaining change is $", np.round(np.min(r),2))
    print("the list location for the cookies that leave the least change is ", np.argmin(r))
    if np.argmin(r)==0:
	    print("the cookies to buy that result in the least change are sugar")
    if np.argmin(r)==1:
	    print("the cookies to buy that result in the least change are chocolate")
    if np.argmin(r)==2:
	    print("the cookies to buy that result in the least change are snickerdoodles")
    if np.argmin(r)==3:
	    print("the cookies to buy that result in the least change are s'mores")
    print("the number of cookies that can be bought within the amount given is",0)
    return np.argmin

def y(x):
	y=2.0*x**3.0
	return y
def distancemodulus(d):
	mu=5*np.log10(d/10)
	return mu
def format_axes(ax):
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1.5)  # Larger major ticks
    ax.tick_params(axis='both', which='minor', labelsize=12, length=3, width=1)    # Minor ticks
    ax.minorticks_on()  # Enable minor ticks