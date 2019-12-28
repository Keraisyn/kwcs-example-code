# Week 1: Hypotenuse Solver

# You have to use Pythagorean's theorem to solve this challenge
# a**2 + b**2 = c**2 where c is the hypotenuse and a and b are the other lengths
side1 = int( input("Enter a side length: ") )
side2 = int( input("Enter another side length: ") )

# Tip: An exponent of 1/2 is equivalent to the square root
hyp = (side1**2 + side2**2)**0.5

# You can also import the math module and use the sqrt() function
# import math
# hyp = math.sqrt(side1**2 + side2**2)

print("The length of the hypotenuse is", hyp)
