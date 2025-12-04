# ------------------------------------------------------------
# Manejo de bucles en Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas
# Student ID: 2530260
# Group: IM 1-3
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# This document presents six programming problems that require
# the use of Python loops, specifically for-loops and while-loops.
# A for-loop is typically used when the number of iterations is
# known in advance, such as iterating through a range or a list.
# A while-loop is more natural when repetition depends on a
# condition, such as reading input until a sentinel value appears.
# Counters and accumulators are essential tools used inside loops
# to keep track of quantities and totals. It is also crucial to
# define clear exit conditions to prevent infinite loops.
# The document includes descriptions, inputs, outputs, validations,
# test cases, and code implementations that demonstrate loop usage
# in ranges, menus, sentinels, attempts, and pattern generation.
# ------------------------------------------------------------
# GOOD PRACTICES AND PRINCIPLES (STRINGS)
# ------------------------------------------------------------
# - Strings are immutable: any modification creates a new string.
# - Always normalize input with strip() and lower() before comparing it.
# - Avoid magic numbers when slicing; document each slice clearly.
# - Prefer built-in string methods instead of rewriting basic logic.
# - Validation order matters: first check empty input, then structure.
# - Write clean code with descriptive variable names and clear messages.
#
# ------------------------------------------------------------
# START OF CODE
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 1: Sum of range with for
# ------------------------------------------------------------
# Description:
# Calculates the sum of all integers from 1 to n (including n)
# and also calculates the sum of even numbers in the same range.
# A for-loop with accumulators is used to compute both totals.
#
# Inputs:
# - n (int): upper limit of the range.
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be convertible to int.
# - n must be >= 1; otherwise print "Error: invalid input".
#
# Test cases:
# 1) Normal:
#    Input: n = 5
#    Output: Sum 1..n: 15
#            Even sum 1..n: 6
#
# 2) Border:
#    Input: n = 1
#    Output: Sum 1..n: 1
#            Even sum 1..n: 0
#
# 3) Error:
#    Input: n = -3
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

n_input = input("Enter n: ").strip()

# Validation: must be int
try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for number in range(1, n + 1):
            total_sum += number
            if number % 2 == 0:
                even_sum += number

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
# ------------------------------------------------------------  
# ------------------------------------------------------------
# Problem #: 2 Multiplication table with for
# ------------------------------------------------------------
# Description:
# Genera la tabla de multiplicar de un número base desde 1
# hasta un límite m usando un ciclo for.
#
# Inputs:
# - base (int)
# - m (int; límite de la tabla)
#
# Outputs:
# - “base x 1 = resultado”
# - “base x 2 = resultado”
# - ...
#
# Validations:
# - Verificar que base y m se puedan convertir a int.
# - m >= 1
#
# Test cases:
# 1) Normal:
#    Input: base = 5, m = 4
#    Output:
#       5 x 1 = 5
#       5 x 2 = 10
#       5 x 3 = 15
#       5 x 4 = 20
#
# 2) Border:
#    Input: base = 7, m = 1
#    Output:
#       7 x 1 = 7
#
# 3) Error:
#    Input: base = 5, m = 0
#    Output:
#       Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

try:
    base = int(input("Enter base: "))
    m = int(input("Enter limit: "))

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")

except:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 3 Average of numbers with while and sentinel
# ------------------------------------------------------------
# Description:
# Lee números hasta que el usuario ingrese un sentinela (-1).
# Calcula el promedio y la cantidad de números válidos.
#
# Inputs:
# - number (float)
# - sentinel_value = -1
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - Si no hay datos válidos:
#   "Error: no data"
#
# Validations:
# - Cada número debe convertirse a float.
#
# Test cases:
# 1) Normal:
#    Input: 5, 3, 2, -1
#    Output:
#       Count: 3
#       Average: 3.3333333333
#
# 2) Border:
#    Input: 10, -1
#    Output:
#       Count: 1
#       Average: 10.0
#
# 3) Error:
#    Input: -1
#    Output:
#       Error: no data
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

sentinel_value = -1
total = 0
count = 0

while True:
    try:
        number = float(input("Enter number (-1 to finish): "))
    except:
        print("Error: invalid input")
        continue

    if number == sentinel_value:
        break

    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 4  Password attempts with while
# ------------------------------------------------------------
# Description:
# Simple password attempt system with limited tries.
# User must enter the correct password within MAX_ATTEMPTS.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - "Login success"
# - "Account locked"
#
# Validations:
# - MAX_ATTEMPTS > 0
#
# Test cases:
# 1) Normal:
#    Input: admin123 on attempt 2
#    Output: Login success
#
# 2) Border:
#    Input: admin123 on attempt 1
#    Output: Login success
#
# 3) Error:
#    Input: wrong passwords 3 times
#    Output: Account locked
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break

    attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 5
# ------------------------------------------------------------
# Description:
# Simple text menu that repeats until the user selects exit (0).
# Allows greeting, showing a counter, and incrementing it.
#
# Inputs:
# - option (int or convertible to int)
#
# Outputs:
# - "Hello!"
# - "Counter:" <counter_value>
# - "Counter incremented"
# - "Bye!"
# - "Error: invalid option"
#
# Validations:
# - option must be 0, 1, 2, or 3
#
# Test cases:
# 1) Normal:
#    Input: 1 → 2 → 3 → 0
#    Output: Hello!, Counter:0, Counter incremented, Bye!
#
# 2) Border:
#    Input: 0
#    Output: Bye!
#
# 3) Error:
#    Input: 9
#    Output: Error: invalid option
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_text = input("Choose an option: ")

    try:
        option = int(option_text)
    except:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 6
# ------------------------------------------------------------
# Description:
# Print a right-triangle star pattern using nested loops (simple version).
# Optionally prints an inverted pattern (documented decision: YES, included).
#
# Inputs:
# - n (int; number of rows)
#
# Outputs:
# - "*" 
# - "**"
# - "***"
# - ...
# - (Optional) inverted pattern after the first one
#
# Validations:
# - n must be convertible to int
# - n >= 1
#
# Test cases:
# 1) Normal:
#    Input: 4
#    Output:
#      *
#      **
#      ***
#      ****
#      ****
#      ***
#      **
#      *
#
# 2) Border:
#    Input: 1
#    Output:
#      *
#      *
#
# 3) Error:
#    Input: 0
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

n_text = input("Enter n: ")

try:
    n = int(n_text)
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

# First triangle
for i in range(1, n + 1):
    print("*" * i)

# Optional inverted triangle (simple)
for i in range(n, 0, -1):
    print("*" * i)
# ------------------------------------------------------------
# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# In this practice, I learned the practical differences between using for and while loops.
# The for loop is ideal when the number of repetitions is known, while the while loop
# depends on a changing condition. Counters and accumulators helped me control totals,
# attempts, and other values inside the loops. I also saw that a poorly designed while
# loop can cause infinite loops if the condition is never updated. Menu systems and
# password attempts are classic examples of while loops in real programs. Finally,
# nested loops allowed me to generate visual patterns such as star triangles.

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python documentation - For and While Loops
#    https://docs.python.org/3/tutorial/controlflow.html
# 2) W3Schools - Python For Loops
#    https://www.w3schools.com/python/python_for_loops.asp
# 3) W3Schools - Python While Loops
#    https://www.w3schools.com/python/python_while_loops.asp
# 4) Real Python - "Python 'for' Loops Explained"
#    https://realpython.com/python-for-loop/
# 5) GeeksforGeeks - "Loops in Python"
#    https://www.geeksforgeeks.org/loops-in-python/
# 6) Programiz - "Python while Loop"
#    https://www.programiz.com/python-programming/while-loop
# 7) Tutorialspoint - "Python - Loop Control Statements"
#    https://www.tutorialspoint.com/python/python_loop_control.htm
# 8) DigitalOcean - "How To Construct While Loops in Python"
#    https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python
# 9) Stack Overflow - Various discussions on loop usage and best practices
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------