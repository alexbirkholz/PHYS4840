#!/usr/bin/
import numpy as np
#problem 2
#initial values/price list
startmoney=20.00
ham_price=3.65
apple_price=4.25
pbj_price=3.00
turkey_price=3.35
halfham_price=2.19
halfapple_price=2.55
halfpbj_price=1.80
halfturkey_price=2.01
#empty lists for storing values
combos=[]
remainingchange=[]
#Nested loops to calculate combinations
for ham_count in range(int(startmoney//ham_price)+1):
	for apple_count in range(int(startmoney//apple_price)+1):
		for pbj_count in range(int(startmoney//pbj_price)+1):
			for turkey_count in range(int(startmoney//turkey_price)+1):
				for halfham_count in range(int(startmoney//halfham_price)):
					for halfapple_count in range(int(startmoney//halfapple_price)):
						for halfpbj_count in range(int(startmoney//halfpbj_price)):
							for halfturkey_count in range(int(startmoney//halfturkey_price)):
								#cost calculation
								total = (ham_count * ham_price + apple_count * apple_price + pbj_count * pbj_price + turkey_count * turkey_price + halfham_count * halfham_price + halfapple_count * halfapple_price + halfpbj_count * halfpbj_price + halfturkey_count * halfturkey_count)
								spare_change = startmoney - total
								#verify within budget + meet problem parameters
								if total <= startmoney and halfham_count <= 1 and halfapple_count <= 1 and halfpbj_count <= 1 and halfturkey_count <=1 and halfham_count + halfturkey_count + halfapple_count + halfpbj_count >= 1 and spare_change * 4 ==int(spare_change * 4):
									combos.append((ham_count, apple_count, pbj_count, turkey_count, halfham_count, halfapple_count, halfpbj_count, halfturkey_count))
									remainingchange.append(spare_change)
spare_change_array = np.array(remainingchange)
combinations = np.array(combos)
print(f"combinations found: {len(combinations)}")
least_change_index = spare_change_array.argmin()
best_combo = combinations[least_change_index]
print(f"the least amount of change is", spare_change_array.min())
print("the ideal sandwich combo is", f"Ham: {best_combo[0]}, Apple: {best_combo[1]}, PBJ: {best_combo[2]}, Turkey: {best_combo[3]}, Half Ham: {best_combo[4]}, Half Apple: {best_combo[5]}, Half PBJ: {best_combo[6]}, Half Turkey: {best_combo[7]}")



#problem 3
primelist=[]
#define a function to determine if something is prime
def primefinder(n):
	output = True
	for i in range(2, int(np.sqrt(n))+1):
		if n % i == 0:
			output = False
		elif n % i:
			pass
	return output
#add primes to list
for n in range(2,55):
	if primefinder(n) == True:
		primelist.append(n)
print(primelist)


#problem 4
#part a
def Catalan(n):
	if n==0:
		return 1
	else:
		return (((4 * n) - 2) / (n + 1)) * Catalan(n - 1)
print(Catalan(100))
#part b
def g(m,n):
	if n==0:
		return m
	else:
		return g(n,m%n)
print(g(108,192))


#Exercise 6
#def min(array):
	#for in array:
		#if:
			
		#else:


#Exercise 7
#import datetime as datetime
#import time as time