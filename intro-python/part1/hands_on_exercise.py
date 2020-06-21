"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random

# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("pi is a {} with a value of {}".format(type(pi), pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
   print("i is less thn 50")
elif i==50:
   print("i is equal to 50")
else:
   print("i is greater than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picket_fruit = 'orange'
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picket_fruit == 'orange':
   print("the fruit is orange")
elif picket_fruit == 'strawberry':
   print("the fruit i red")
elif picket_fruit == 'banana':
   print("the fruit is yellow")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def MULTIPLY(num1, num2):
#   ""Multiply two numbers and return the result."""
   result = num1 * num2
   return result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", MULTIPLY(12, 96))

print("48 x 17 =", MULTIPLY(48, 17))

print("196523 x 87323 =", MULTIPLY(196523, 87323))
