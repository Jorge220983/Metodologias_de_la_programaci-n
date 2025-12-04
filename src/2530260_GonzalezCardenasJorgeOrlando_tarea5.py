# ------------------------------------------------------------
# Manejo de funciones en Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas Jorge Orlando
# Student ID: 2530260
# Group: IM 1-3
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# In Python, a function is a reusable block of code that performs a 
# specific task. Functions help organize programs by separating 
# logic into smaller, clear, and maintainable units. Parameters are 
# variables defined in the function header, while arguments are the 
# actual values passed during the function call. 
#
# Functions are useful because they avoid code repetition, improve 
# readability and allow complex programs to be built from simpler 
# components. A return value provides the result back to the caller, 
# making the function more flexible than simply printing inside it. 
#
# This document includes six problems that demonstrate the use of 
# parameters, return values, default parameters, validation, and 
# main-program organization. Each problem is documented with 
# descriptions, test cases, and clear function-based solutions.
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
# Problem #: 1 - Rectangle area and perimeter
# ------------------------------------------------------------
# Description:
# This program defines two functions:
# - calculate_area(width, height): returns the rectangle area.
# - calculate_perimeter(width, height): returns the rectangle perimeter.
# The main code reads the values, validates them, and prints results.
#
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
# - If invalid: "Error: invalid input"
#
# Validations:
# - width > 0
# - height > 0
# - Both must be valid numbers
#
# Test cases:
# 1) Normal:
#    Input: width = 5, height = 3
#    Output: Area: 15 | Perimeter: 16
#
# 2) Border:
#    Input: width = 1, height = 1
#    Output: Area: 1 | Perimeter: 4
#
# 3) Error:
#    Input: width = -2, height = 4
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)


try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)

        print("Area:", area)
        print("Perimeter:", perimeter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 2 - Grade classifier
# ------------------------------------------------------------
# Description:
# This program defines a function classify_grade(score) that receives
# a numeric score (0–100) and returns its letter category (A–F).
# The main code reads the score, validates it, and prints the result.
#
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
# - If invalid: "Error: invalid input"
#
# Validations:
# - score must be convertible to float
# - score must be between 0 and 100
#
# Test cases:
# 1) Normal:
#    Input: 85
#    Output: Score: 85 | Category: B
#
# 2) Border:
#    Input: 90
#    Output: Score: 90 | Category: A
#
# 3) Error:
#    Input: -5
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter score (0-100): "))

    if 0 <= score <= 100:
        letter = classify_grade(score)
        print("Score:", score)
        print("Category:", letter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 3 - List statistics function (min, max, average)
# ------------------------------------------------------------
# Description:
# This program defines a function summarize_numbers(numbers_list)
# that returns a dictionary containing:
# - "min": the smallest number
# - "max": the largest number
# - "average": the average of the numbers
# The main code reads a text with comma-separated numbers, converts
# them into a list, validates the data, and prints the results.
#
#
# Inputs:
# - numbers_text (string, e.g., "10,20,30")
# - numbers_list (list of float or int, created internally)
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
# - If invalid: "Error: invalid input"
#
# Validations:
# - numbers_text must not be empty
# - numbers_list must not be empty
# - all values must be valid numbers
#
# Test cases:
# 1) Normal:
#    Input: "10,20,30"
#    Output: Min: 10 | Max: 30 | Average: 20.0
#
# 2) Border:
#    Input: "5"
#    Output: Min: 5 | Max: 5 | Average: 5.0
#
# 3) Error:
#    Input: "10,abc,30"
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def summarize_numbers(numbers_list):
    info = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return info


numbers_text = input("Enter numbers separated by commas: ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            num = float(p)
            numbers_list.append(num)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 4 - Apply discount list (pure function)
# ------------------------------------------------------------
# Description:
# This program defines a function apply_discount(prices_list, discount_rate)
# that returns a new list with all prices discounted. The original list
# must not be modified. The main code reads prices from text, converts
# them into floats, validates the discount rate, and prints both lists.
#
#
# Inputs:
# - prices_text (string, e.g., "100,200,300")
# - discount_rate (float between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
# - If invalid: "Error: invalid input"
#
# Validations:
# - prices_text not empty
# - all prices > 0
# - discount_rate between 0 and 1
# - list must not be empty
#
# Test cases:
# 1) Normal:
#    Input: "100,200,300", discount_rate = 0.10
#    Output: Original prices: [100.0, 200.0, 300.0]
#            Discounted prices: [90.0, 180.0, 270.0]
#
# 2) Border:
#    Input: "50", discount_rate = 0
#    Output: Original prices: [50.0]
#            Discounted prices: [50.0]
#
# 3) Error:
#    Input: "100,abc,300", discount_rate = 0.20
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def apply_discount(prices_list, discount_rate):
    new_list = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        new_list.append(new_price)
    return new_list


prices_text = input("Enter prices separated by commas: ").strip()

if prices_text == "":
    print("Error: invalid input")
else:
    try:
        parts = prices_text.split(",")
        prices_list = []

        for p in parts:
            price = float(p)
            if price <= 0:
                raise ValueError
            prices_list.append(price)

        if len(prices_list) == 0:
            print("Error: invalid input")
        else:
            try:
                discount_rate = float(input("Enter discount rate (0 to 1): "))
                if discount_rate < 0 or discount_rate > 1:
                    print("Error: invalid input")
                else:
                    discounted = apply_discount(prices_list, discount_rate)
                    print("Original prices:", prices_list)
                    print("Discounted prices:", discounted)
            except ValueError:
                print("Error: invalid input")

    except ValueError:
        print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 5 - Greeting function with default parameters
# ------------------------------------------------------------
# Description:
# This program defines a function greet(name, title="")
# that builds a full greeting. If a title is provided, it is
# placed before the name (e.g., "Dr. Alice"). Otherwise, only
# the name is used. The function returns: "Hello, <full_name>!".
# The main code reads the name and title, validates them, and
# prints the final greeting.
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
# - If invalid: "Error: invalid input"
#
# Validations:
# - name not empty after strip()
# - title can be empty, but should be stripped
#
# Test cases:
# 1) Normal:
#    Input: name="Alice", title="Dr."
#    Output: Greeting: Hello, Dr. Alice!
#
# 2) Border:
#    Input: name="Bob", title="" 
#    Output: Greeting: Hello, Bob!
#
# 3) Error:
#    Input: name="" (after strip)
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def greet(name, title=""):
    if title == "":
        full_name = name
    else:
        full_name = title + " " + name
    return f"Hello, {full_name}!"


name = input("Enter name: ").strip()

if name == "":
    print("Error: invalid input")
else:
    title = input("Enter title (optional): ").strip()

    # title can be empty, so no strict validation needed
    message = greet(name, title)
    print("Greeting:", message)
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem #: 6
# ------------------------------------------------------------
# Description:
# This program defines a function factorial(n) that returns n! 
# using an iterative approach. The main code reads an integer n,
# validates it, calls the function, and prints the factorial.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer.
# - n >= 0.
# - Optional limit: n <= 20 to avoid excessively large values.
#
# Test cases:
# 1) Normal:
#    Input: 5
#    Output: Factorial: 120
#
# 2) Border:
#    Input: 0
#    Output: Factorial: 1
#
# 3) Error:
#    Input: -3
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def factorial(n):
    """
    Iterative factorial function:
    factorial(0) = 1
    factorial(n) = 1 * 2 * ... * n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    n_text = input("Enter an integer n: ").strip()

    # Validate integer
    if not n_text.lstrip("-").isdigit():
        print("Error: invalid input")
    else:
        n = int(n_text)

        # Validations
        if n < 0 or n > 20:
            print("Error: invalid input")
        else:
            value = factorial(n)
            print("n:", n)
            print("Factorial:", value)

except:
    print("Error: invalid input")
# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Working with functions helped me understand how code becomes more organized,
# because each task is separated into smaller blocks that are easy to reuse.
# Using return instead of only printing makes the function more flexible,
# since the value can be stored, used in other calculations, or printed later.
# Parameters also make the functions adaptable, and default values help when
# I want optional behavior without rewriting code.
# I noticed that using functions is especially useful when logic repeats,
# like validations or mathematical processes.
# Finally, I learned the difference between the main logic (program flow)
# and support functions that handle specific operations.
# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Official Documentation – Functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 2) W3Schools – Python Functions Tutorial:
#    https://www.w3schools.com/python/python_functions.asp
#
# 3) Real Python – Defining and Using Functions:
#    https://realpython.com/defining-your-own-python-function/
#
# 4) GeeksforGeeks – Python Functions:
#    https://www.geeksforgeeks.org/python-functions/
#
# 5) Programiz – Python Function Examples:
#    https://www.programiz.com/python-programming/function
#
# 6) TutorialsPoint – Python Functions:
#    https://www.tutorialspoint.com/python/python_functions.htm
#
# 7) Stack Overflow – Common Questions About Python Function Design:
#    https://stackoverflow.com/questions/tagged/python-functions
# --------------------------------------------------
# END OF CODE
# --------------------------------------------------