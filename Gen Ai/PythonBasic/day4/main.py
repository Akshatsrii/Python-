# # Exception handling 
# Exception Handling in Python

# Exception Handling is a way to handle runtime errors in Python so that the program does not crash unexpectedly. Instead of stopping, the program can display an error message or take another action.

# Why do we use Exception Handling?
# Prevents the program from crashing.
# Handles unexpected errors gracefully.
# Makes programs more reliable.
# Helps in debugging.
# Syntax
# try:
#     # Code that may cause an exception
# except:
#     # Code to handle the exception
# Example 1: Division by Zero
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# Output 1
# Enter first number: 10
# Enter second number: 2
# Result: 5.0
# Output 2
# Enter first number: 10
# Enter second number: 0
# You cannot divide by zero.
# Example 2: Invalid Input
# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)

# except ValueError:
#     print("Please enter a valid number.")
# Output
# Enter your age: abc
# Please enter a valid number.
# Multiple Exceptions
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)

# except ValueError:
#     print("Invalid input!")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# Using else

# The else block runs only if no exception occurs.

# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("You entered:", num)
# Output
# Enter a number: 25
# You entered: 25
# Using finally

# The finally block always executes, whether an exception occurs or not.

# try:
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Error")
# finally:
#     print("Program Finished")
# Output
# 5.0
# Program Finished

# Even if an error occurs:

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Program Finished")
# Output
# Cannot divide by zero
# Program Finished
# Using raise

# You can create (raise) your own exception.

# age = int(input("Enter your age: "))

# if age < 18:
#     raise ValueError("Age must be 18 or above.")

# print("You are eligible.")
# Output
# Enter your age: 15
# ValueError: Age must be 18 or above.
# Catching All Exceptions
# try:
#     x = int(input("Enter a number: "))
#     print(10 / x)

# except Exception as e:
#     print("Error:", e)

# Here, e contains the actual error message.

# Common Python Exceptions
# Exception	Cause
# ValueError	Invalid value (e.g., int("abc"))
# TypeError	Wrong data type
# ZeroDivisionError	Division by zero
# IndexError	Invalid list index
# KeyError	Dictionary key not found
# NameError	Variable not defined
# FileNotFoundError	File does not exist
# AttributeError	Object has no requested attribute
# Flow of Exception Handling
# Start
#    │
#    ▼
#  try block
#    │
#    ├── No Error ──► else (if present)
#    │                  │
#    │                  ▼
#    │              finally
#    │
#    └── Error Occurs
#            │
#            ▼
#       except block
#            │
#            ▼
#         finally
#            │
#            ▼
#           End
# Interview Questions
# 1. What is exception handling?

# Exception handling is a mechanism for handling runtime errors so that the program doesn't terminate unexpectedly.

# 2. Difference between try, except, else, and finally?
# try → Code that may raise an exception.
# except → Handles the exception.
# else → Runs if no exception occurs.
# finally → Runs regardless of whether an exception occurs.
# 3. What is the difference between an error and an exception?
# Error: A serious problem that usually cannot be recovered from (e.g., SyntaxError during parsing).
# Exception: A runtime event that can be caught and handled (e.g., ValueError, ZeroDivisionError).
# 4. What does Exception as e mean?
# try:
#     print(10 / 0)
# except Exception as e:
#     print(e)

# Output:

# division by zero

# e stores the exception object, allowing you to inspect or print the error message.

# Quick Summary
# try → Write code that might fail.
# except → Handle the error.
# else → Execute if no error occurs.
# finally → Always execute.
# raise → Manually throw an exception.
# Exception as e → Access the exception object and its message.

# These are the core concepts of exception handling in Python and are commonly asked in interviews and coding assessments.4

# File Handling
# append 
# r = open("Superman.txt ", 'a')
# r.write("and now i am append")

# r.close()

# read 
# r = open("Superman.txt ", 'r')
# r.write("and now i am append")

# r.close()

