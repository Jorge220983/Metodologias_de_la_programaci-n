# ------------------------------------------------------------
# Fibonacci Series with Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas
# Student ID: 2530260
# Group: IM 1-3
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# The Fibonacci sequence is a numerical pattern where each term 
# is the sum of the two previous ones, starting with 0 and 1. 
# Calculating the sequence up to n terms means generating exactly 
# the first n values of this pattern in order. 
# This program reads an integer n, validates it, and uses a loop 
# to generate and display the first n Fibonacci terms. 
# It focuses on correct input handling, structured logic, and 
# clear output formatting in English.
# ------------------------------------------------------------
# GOOD PRACTICES AND PRINCIPLES (STRINGS)
# ------------------------------------------------------------
# - Strings are immutable: any modification creates a new string.
# - Always normalize input with strip() and lower() before comparing it.
# - Avoid magic numbers when slicing; document each slice clearly.
# - Prefer built-in string methods instead of rewriting basic logic.
# - Validation order matters: first check empty input, then structure.
# - Write clean code with descriptive variable names and clear messages.
# - Use f-strings for readable and efficient string formatting.
# ------------------------------------------------------------
# PROBLEM: Fibonacci series generator
# ------------------------------------------------------------
# Description:
# Program that reads an integer n and prints the first n terms
# of the Fibonacci series, starting with 0 and 1. The program
# validates the input before calculating the series and prints
# all terms in a single line separated by spaces.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated by spaces
#
# Validations:
# - n must be a valid integer
# - n must be >= 1
# - (Optional) n must be <= 50 to avoid overly large series
#
# Test cases:
# 1) Normal:
#    Input: n = 7
#    Output: Fibonacci series: 0 1 1 2 3 5 8
#
# 2) Border:
#    Input: n = 1
#    Output: Fibonacci series: 0
#
# 3) Error:
#    Input: n = "hello"
#    Output: Error: invalid input
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
# Read input
user_input = input("Enter the number of terms: ")

# Input validation
try:
    n = int(user_input)

    if n < 1 or n > 50:
        print("Error: invalid input")
        exit()

except:
    print("Error: invalid input")
    exit()

# Fibonacci calculation
first = 0
second = 1

# Special cases
if n == 1:
    print("Fibonacci series: 0")
    exit()
elif n == 2:
    print("Fibonacci series: 0 1")
    exit()

# Generate the series for n >= 3
fibonacci_list = [first, second]

for _ in range(3, n + 1):
    next_term = first + second
    fibonacci_list.append(next_term)
    first = second
    second = next_term

# Output
print("Fibonacci series:", *fibonacci_list)
# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Using a loop made it much easier to generate the Fibonacci series because
# the pattern repeats and each term depends on the two previous ones.
# Handling special cases like n = 1 and n = 2 is important so the program
# produces correct output even in the smallest valid inputs.
# This logic could be reused in other programs that need cumulative sequences,
# iterative calculations, or pattern-based numerical generation.
# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# References:
# 1) Python Official Documentation – "for Statements"
#    https://docs.python.org/3/tutorial/controlflow.html#for-statements
#
# 2) Python Official Documentation – "while Statements"
#    https://docs.python.org/3/tutorial/controlflow.html#the-while-statement
#
# 3) GeeksforGeeks – "Program for Fibonacci Numbers in Python"
#    https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers/
#
# 4) W3Schools – "Python For Loops"
#    https://www.w3schools.com/python/python_for_loops.asp
#
# 5) TutorialsPoint – "Python Fibonacci Series"
#    https://www.tutorialspoint.com/python-program-to-print-fibonacci-series
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------