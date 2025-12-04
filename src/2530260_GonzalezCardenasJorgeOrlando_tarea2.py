# ------------------------------------------------------------
# Manejo de números y booleanos en Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas
# Student ID: 2530260
# Group: IM 1-3
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# This document presents six programming problems designed to
# practice Python numeric types (int and float) and boolean values.
# Integers are used for whole quantities, while floats represent
# decimal values required in real-world calculations such as BMI,
# salaries or temperature conversions.
#
# Boolean values (True/False) appear naturally from comparisons such
# as >, <, ==, and they are essential for decision-making through
# conditional statements. The exercises reinforce data validation,
# including checking ranges and preventing division by zero to avoid
# runtime errors.
#
# The content includes a full description of each problem, expected
# inputs and outputs, validation rules, and three test cases per task.
# The solutions show how numeric operations, comparisons, boolean
# expressions, and type casting can be combined to solve practical
# payroll, discount, finance, and health-related problems.
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
# Problem 1:
# ------------------------------------------------------------
# Description:
# Convierte una temperatura en grados Celsius a Fahrenheit y Kelvin.
# Determina si la temperatura es alta (>= 30.0 °C).
#
# Inputs:
# - temp_c (float; temperatura en °C)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true | false
#
# Validations:
# - Verificar que temp_c pueda convertirse a float.
# - Validar que la temperatura en Kelvin no sea negativa (físicamente imposible).
# - Si la validación falla, mostrar un mensaje de error.
#
# Test cases:
# 1) Normal:
#    Input: 30
#    Output: Fahrenheit: 86.0 / Kelvin: 303.15 / High temperature: true
#
# 2) Border:
#    Input: -273.15
#    Output: Fahrenheit: -459.67 / Kelvin: 0.0 / High temperature: false
#
# 3) Error:
#    Input: -300
#    Output: Error: temperatura en Kelvin no válida.
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
try:
    temp_c = float(input("Temperature °C: ").strip())

    temp_k = temp_c + 273.15
    if temp_k < 0:
        print("Error: temperatura en Kelvin no válida.")
    else:
        temp_f = temp_c * 9/5 + 32
        is_high_temperature = (temp_c >= 30.0)

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

except ValueError:
    print("Error: ingrese un valor numérico válido.")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 2:
# ------------------------------------------------------------
# Description:
# Calcula el pago semanal de un trabajador considerando horas regulares
# y horas extra. Las horas extra se pagan al 150% de la tarifa normal.
#
# Inputs:
# - hours_worked (float; horas trabajadas en la semana)
# - hourly_rate (float; pago por hora)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true | false
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
# - En caso de error, mostrar "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: hours_worked=45, hourly_rate=100
#    Output: Regular pay: 4000 / Overtime pay: 750 / Total: 4750 / Has overtime: true
#
# 2) Border:
#    Input: hours_worked=40, hourly_rate=80
#    Output: Regular pay: 3200 / Overtime pay: 0 / Total: 3200 / Has overtime: false
#
# 3) Error:
#    Input: hours_worked=-5, hourly_rate=90
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
try:
    hours_worked = float(input("Hours worked: ").strip())
    hourly_rate = float(input("Hourly rate: ").strip())

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = (hours_worked > 40)

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 3:
# ------------------------------------------------------------
# Description:
# Determines if a customer is eligible for a discount based on being
# a student, a senior, or having a purchase equal or above 1000.0.
# Applies a 10% discount when eligible.
#
# Inputs:
# - purchase_total (float; total of the purchase)
# - is_student_text ("YES" or "NO")
# - is_senior_text ("YES" or "NO")
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - Text for student/senior must be "YES" or "NO"
# - Otherwise show "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: purchase_total=1200, is_student="NO", is_senior="NO"
#    Output: Discount eligible: true / Final total: 1080.0
#
# 2) Border:
#    Input: purchase_total=999.99, is_student="NO", is_senior="NO"
#    Output: Discount eligible: false / Final total: 999.99
#
# 3) Error:
#    Input: purchase_total=500, is_student="MAYBE", is_senior="NO"
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
try:
    purchase_total = float(input("Purchase total: ").strip())
    is_student_text = input("Is student (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior (YES/NO): ").strip().upper()

    if purchase_total < 0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 4:
# ------------------------------------------------------------
# Description:
# Reads three integers and calculates their sum, average, maximum,
# minimum, and a boolean that checks if all of them are even numbers.
#
# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - Check that all inputs can be converted to integers
# - Negative values are allowed
#
# Test cases:
# 1) Normal:
#    Input: 4, 10, 6
#    Output: Sum: 20 / Average: 6.66... / Max: 10 / Min: 4 / All even: true
#
# 2) Border:
#    Input: 1, 2, 3
#    Output: Sum: 6 / Average: 2.0 / Max: 3 / Min: 1 / All even: false
#
# 3) Error:
#    Input: "a", 5, 3
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

try:
    n1 = int(input("Enter first integer: ").strip())
    n2 = int(input("Enter second integer: ").strip())
    n3 = int(input("Enter third integer: ").strip())

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 5:
# ------------------------------------------------------------
# Description:
# Determines loan eligibility based on monthly income, monthly debt,
# and credit score. It calculates the debt ratio and checks if the
# applicant meets the minimum financial and credit requirements.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
# - If any validation fails → print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: income=10000, debt=3000, score=700
#    Output: Debt ratio: 0.3 / Eligible: true
#
# 2) Border:
#    Input: income=8000, debt=3200, score=650
#    Output: Debt ratio: 0.4 / Eligible: true
#
# 3) Error:
#    Input: income=0, debt=2000, score=600
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

try:
    monthly_income = float(input("Enter monthly income: ").strip())
    monthly_debt = float(input("Enter monthly debt: ").strip())
    credit_score = int(input("Enter credit score: ").strip())

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 6:
# ------------------------------------------------------------
# Description:
# Calculates a person's Body Mass Index (BMI) using the formula
# weight_kg / (height_m * height_m). Then determines whether the
# person is underweight, normal, or overweight based on BMI ranges.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI:" <bmi_rounded>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - If validation fails → print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: weight=70, height=1.75
#    Output: BMI: 22.86 / Underweight: false / Normal: true / Overweight: false
#
# 2) Border:
#    Input: weight=50, height=1.65
#    Output: BMI: 18.37 / Underweight: true / Normal: false / Overweight: false
#
# 3) Error:
#    Input: weight=-5, height=1.70
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

try:
    weight_kg = float(input("Enter weight in kg: ").strip())
    height_m = float(input("Enter height in meters: ").strip())

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (bmi >= 18.5 and bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_rounded)
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

except ValueError:
    print("Error: invalid input")
# ------------------------------------------------------------
# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Working with integers and floats together is essential because real-world
# calculations often need both whole numbers and decimal precision. Boolean
# comparisons help create logical decisions that guide the flow of a program.
# Validating input ranges is important to avoid impossible values and errors
# such as division by zero. Using combined conditions with and, or, and not
# teaches how to build flexible rules for different situations. These same
# patterns appear repeatedly in payroll systems, discount rules, loan
# evaluations, and many other common programming problems.
# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python documentation - Numeric Types (int, float, complex)
# 2) Python documentation - Boolean Type — bool
# 3) Python tutorial - Arithmetic, comparison, and logical operators
# 4) “Introduction to Algorithms and Programming” – Basic numeric processing
# 5) Classroom notes and articles on numeric input validation and safe calculations
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------