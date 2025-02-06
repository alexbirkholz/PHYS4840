#!/usr/bin/
import numpy as np
import Birkholz_functions_lib as mfl
vector = [1,2,3,0]
print(mfl.my_function(vector))
#Exercise 3a: answer is 3.7416573867739413
#Exercise 3b: 2 entries gets an Index Error with list index out of range.
#4 entries gets a result of 5.477225575051661 (I used the vector <1 2 3 4>).
#Changing that to 0 gets the same answer previously.
#This is because assigning a,b,c to parts of the vector is actually irrelevant: it returns np.linalg.norm of the vector which does not depend on a, b, c.
#Bonus Exercise 4: numpy only has to be imported in my_functions_lib.py because it is imported to here as part of my_functions_lib
sugar=2.65
chocolate=3.20
snickerdoodle=3.45
smores=3.70
list=[sugar,chocolate,snickerdoodle,smores]
cookielist=np.array(list)
cookies=np.array(list)
startdollars=10.00
print(mfl.cookiecalculate(cookielist,startdollars))