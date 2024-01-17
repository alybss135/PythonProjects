"""
 Project Description:
 Approximates the area under the curve using the Right Riemann Sum, Trapezoidal Sum, and Simpson's Rule
 Values needed to be inputted first
"""

# libraries
import numpy as np
import math as math
import sys
import getopt

a = -8		# sample value
b = 8		# sample value
n = None
opts = None

# testing inputs
try:
	opts, args = getopt.getopt(sys.argv[1:], "n:", [ "n="])
	for opt, arg in opts:
		if opt == "-n":												# if value is negative
			try:													
				n = int(arg)
			except:													# for other cases such as if a character entered
				print("Parameter n cannot be parsed as an integer")
				sys.exit()			
except:
	if (opts == None):
		print("Please provide a value for n")
	sys.exit()

if (n == None):
	print("Please provide a value for n")
	sys.exit()
	
if n == 1:
	print("n cannot be 1")
	sys.exit()

# calculations
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sqrt(x*x*x-75*x+350)
    
# for calcuating the right Riemann sum
def right():
    I_right = h * sum(f[1::])
    print("A_right =", round_up(I_right,4))

# for calculating the trapezoidal sum
def trapezoidal():
    I_trapezoidal = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
    print("A_trapezoidal =", round_up(I_trapezoidal, 4))

# for calcuating the area under the curve using Simpson's rule
def simpsons():
    I_simpsons = (h/3) * (f[0] + 2*sum(f[:n-2:2]) + 4*sum(f[1:n-1:2]) + f[n-1]) 
    if (n % 2 == 0):
        print("A_simpsons =", round_up(I_simpsons,4))
    else: 
        print("simspons error: number of intervals is not even")

# rounding decimals to a specific decimal value
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# calls to functions
right()
trapezoidal()
simpsons()