"""condition_.py
This module contains the Condition class, which is used to represent a condition in a logical expression.   
"""
""" there are several types of conditions that can be used in logical expressions, including comparison 
conditions, logical conditions, and membership conditions. The Condition class provides a way to create 
and evaluate these conditions in a consistent manner."""

#simple if-else statement
x = int(input("Enter a number: "))
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")    

# simple if-elif-else statement
y = int(input("Enter a number: "))
if y > 10:
    print("y is greater than 10")
elif y > 5: 
    print("y is greater than 5 but less than or equal to 10")
else:
    print("y is not greater than 5")

# simple nested if statement
z = int(input("Enter a number: "))
if z > 5:
    if z < 15:
        print("z is between 5 and 15")
    else:
        print("z is not between 5 and 15")
else:
    print("z is not greater than 5")    

