# Codomax Internship - Module 1
# Topic: Functions in Python

print("===== PYTHON FUNCTIONS =====")


# -------------------------------------------------
# 1. Simple function
# -------------------------------------------------

def greet():
    print("Hello! Welcome to Python programming.")


print("\n1. Simple Function:")
greet()


# -------------------------------------------------
# 2. Function with parameters
# -------------------------------------------------

def greet_user(name):
    print("Hello", name + "!")


print("\n2. Function with Parameter:")
greet_user("Ishwari")


# -------------------------------------------------
# 3. Function with multiple parameters
# -------------------------------------------------

def add_numbers(a, b):
    print("Addition:", a + b)


print("\n3. Function with Multiple Parameters:")
add_numbers(20, 10)


# -------------------------------------------------
# 4. Function returning a value
# -------------------------------------------------

def multiply_numbers(a, b):
    return a * b


print("\n4. Function with Return Value:")

result = multiply_numbers(5, 6)

print("Multiplication:", result)


# -------------------------------------------------
# 5. Function to calculate average
# -------------------------------------------------

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


print("\n5. Calculate Average Using Function:")

student_marks = [85, 78, 92, 88, 76]

average = calculate_average(student_marks)

print("Marks:", student_marks)
print("Average:", average)


# -------------------------------------------------
# 6. Function to check even or odd
# -------------------------------------------------

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("\n6. Even or Odd Function:")

number = int(input("Enter a number: "))

result = check_even_odd(number)

print("The number is:", result)


# -------------------------------------------------
# 7. Function to calculate factorial
# -------------------------------------------------

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


print("\n7. Factorial Function:")

number = int(input("Enter a number for factorial: "))

result = factorial(number)

print("Factorial of", number, "is:", result)


# -------------------------------------------------
# Program completed
# -------------------------------------------------

print("\n===== FUNCTION PRACTICE COMPLETED =====")