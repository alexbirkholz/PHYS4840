#Pseudo-code:
#For m dollars, how many integer n number of a cookie type can be bought with m dollars, and what is the remainder r left over from m?
#given: Sugar=$2.65, Chocolate=$3.20, Snickerdoodle=$3:45,Smores=$3:70. Test value m=$10:00
#logic structure:
#Divide m by a cookie value*n using modular arithmetic to obtain r. Run for each cookie type and output r to determine which cookie gives the least left over change.
#CODE:
import numpy as np
sugar=2.65
chocolate=3.20
snickerdoodle=3.45
smores=3.70
list=[sugar,chocolate,snickerdoodle,smores]
cookies=np.array(list)
startdollars=10.00
for i in cookies:
	n=startdollars//cookies
	r=startdollars%cookies
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
#probably a more efficient way to do this
print("the number of cookies that can be bought within the amount given is",n)