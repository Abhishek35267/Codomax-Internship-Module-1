# looping statements in python are used to execute a block of code repeatedly as long as a certain condition is met. Python provides two main types of loops: the `for` loop and the `while` loop.
#multiple line comment can be written using triple quotes (""" or ''') in Python. This is often used for documentation strings (docstrings) or to provide detailed explanations in the code.
# for loop: The `for` loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. The syntax of a `for` loop is as follows:
""" for iterator_variable in sequence:
    # block of code to be executed
"""
i=1 
for i in range(1, 6):  # This will iterate from 1 to 5
    print(f"Iteration {i}: Hello, World!")  # This block of code will be executed for each value of i 


# while loop: The `while` loop is used to execute a block of code as long as a specified condition is true. The syntax of a `while` loop is as follows:
''' initialize a variable
while condition:
    # block of code to be executed
    increment or update the variable to eventually break the loop
''' 
n=0 
while n < 5:
    print(f"While Loop Iteration {n + 1}: Hello, World!")
    n += 1
