"""
Task 1: Variables and Syntax
Module 1: Introduction to AI & Python
Author: abhishek wahule 
Internship: Codomax Digital Solutions
"""

# ==========================================
# 1. Understanding Python Syntax & Output
# ==========================================
print("--- Task 1: Python Variables and Syntax Execution ---\n")

# ==========================================
# 2. Variable Declaration & Assignment
# ==========================================
# A variable is created the moment you first assign a value to it.
intern_name = "Abhishek wahule "             # String (str)
internship_id = 101              # Integer (int)
stipend_amount = 4500.50         # Floating-point (float)
is_task_completed = True         # Boolean (bool)

# ==========================================
# 3. Printing Variables and Data Types
# ==========================================
print("\n[INFO] Displaying Variable Values:")
print("Intern Name:", intern_name)
print("Internship ID:", internship_id)
print("Stipend Amount:", stipend_amount)
print("Task Status Completed:", is_task_completed)

print("\n[INFO] Checking Data Types using type() function:")
print(f"Data type of intern_name: {type(intern_name)}")
print(f"Data type of internship_id: {type(internship_id)}")
print(f"Data type of stipend_amount: {type(stipend_amount)}")
print(f"Data type of is_task_completed: {type(is_task_completed)}")


# 4. Rules for Python Variable Names (Syntax)

# Valid variable naming conventions (snake_case):
user_age = 23
total_score = 95.5
_hidden_variable = "Internal use"

print("\n[INFO] Valid Naming Examples Executed Successfully.")
print(f"User Age: {user_age}, Total Score: {total_score}")

# ==========================================
# 5. Multiple Assignment & Reassignment
# ==========================================
# Assigning values to multiple variables in a single line
language, framework, level = "Python", "Streamlit", "Beginner"
print(f"\nTech Stack: {language} | Framework: {framework} | Level: {level}")

# Reassigning a variable
progress_status = "In Progress"
print("Initial Status:", progress_status)

progress_status = "Completed"
print("Updated Status:", progress_status)