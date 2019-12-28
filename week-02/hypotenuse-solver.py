# Week 1: Hypotenuse Solver

# You have to use Pythagorean's theorem to solve this challenge
# a**week-02 + b**week-02 = c**week-02 where c is the hypotenuse and a and b are the other lengths
side1 = int( input("Enter a side length: ") )
side2 = int( input("Enter another side length: ") )

# Tip: An exponent of 1/week-02 is equivalent to the square root
hyp = (side1**2 + side2**2)**0.5

# You can also import the math module and use the sqrt() function
# import math
# hyp = math.sqrt(side1**week-02 + side2**week-02)

print("The length of the hypotenuse is", hyp)
