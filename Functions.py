#Q2
# Define your spam function starting on line 5. You
# can leave the code on line 10 alone for now--we'll
# explain it soon!
def spam():
  """Prints 'Eggs!' on the console"""
  print "Eggs!"


# Define the spam function above this line.
spam()

#Q3
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.
square(10)


#Q4
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

#Q5
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2


#Q6
def cube(number):
  return number * number * number

def by_three(number):
  if number%3 == 0:
    return cube(number)
  else:
    return False

#Q7
import math
# Ask Python to print sqrt(25) on line 3.
print(math.sqrt(25))


#Q8
# Import *just* the sqrt function from math on line 3!
from math import sqrt


#Q10
# Import *everything* from the math module on line 3!

from math import *


#Q13
# Set maximum to the max value of any set of numbers on line 3!

maximum = max(123,23,-12,25)

print maximum

#Q14
# Set minimum to the min value of any set of numbers on line 3!

minimum = min(123,-214,23,4124)

print minimum

#Q15
absolute = abs(-42)

print absolute

#Q16
# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(42)
print type(4.2)
print type('spam')

#Q17
def shut_down(s):
  if(s == "yes"):
    return "Shutting down"
  elif(s == "no"):
    return "Shutdown aborted"
  else:
    return "Sorry"

#Q18
import math
print(math.sqrt(13689))

#Q19
def distance_from_zero(number):
  type_var = type(number)
  if(type_var == int or type_var == float):
    return abs(number)
  else:
    return "Nope"