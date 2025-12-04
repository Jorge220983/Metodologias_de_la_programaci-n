# ------------------------------------------------------------
# Manejo de strings en Python
# ------------------------------------------------------------
# Name: Jorge Orlando González Cárdenas
# Student ID: 2530260
# Group: IM 1-3
#
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
"""
 In Python, a string is an immutable text data type used to store
 sequences of characters. Because strings cannot be modified directly,
 every transformation (replace, slice, or format) creates a new value.
 Basic operations such as concatenation, slicing, length measurement,
 pattern searching, and text formatting make strings essential for
 handling input and output in most programs.
 Validating and normalizing user text (using strip(), lower(),
 split(), replace(), etc.) prevents formatting errors and ensures that
 the program processes clean and consistent data. This document
 includes six problems that demonstrate text processing, validation,
 formatting, and classification using multiple string methods.
 Each problem contains descriptions, inputs, outputs, validations, 
 and three test cases, followed by conclusions and references.
"""
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
# Problem 1: Full name formatter (name + initials)
# ------------------------------------------------------------
# Description:
# This program receives a full name in a single string, cleans extra
# spaces, normalizes capitalization, and prints the formatted name
# in Title Case. It also extracts and displays the initials of each
# word in the name (e.g., J.C.T.).
#
# Inputs:
# - full_name (string): a complete name that may contain extra spaces,
#   mixed capitalization, or lower/upper case inconsistency.
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - The input must not be empty after using strip().
# - It must contain at least two separate words.
# - It cannot be only blank spaces.
#
# Test cases:
# 1) Normal:
#    Input: "juan carlos tovar"
#    Output: Formatted name: Juan Carlos Tovar
#            Initials: J.C.T.
#
# 2) Border:
#    Input: "   aNuar  toVar   "
#    Output: Formatted name: Ana Tovar
#            Initials: A.T.
#
# 3) Error:
#    Input: "    "
#    Output: Error: invalid input
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

full_name = input("Enter full name: ").strip()

# Validation: empty string
if len(full_name) == 0:
    print("Error: invalid input")
else:
    words = full_name.split()

    # Validation: must have at least two words
    if len(words) < 2:
        print("Error: invalid input")
    else:
        # Normalize name
        formatted_name = " ".join(words).title()

        # Extract initials
        initials = ""
        for w in words: 
            initials += w[0].upper() + "."

        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")

# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# ------------------------------------------------------------
# Description:
# This program validates whether an email address has a correct basic
# structure. It checks that the text contains exactly one '@', has at
# least one dot after the '@', and contains no spaces. If valid, the
# program also extracts and prints the email domain.
#
# Inputs:
# - email_text (string): the email address entered by the user.
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - The input must not be empty after strip().
# - The string must contain exactly one '@'.
# - The string must not contain spaces (" ").
# - There must be at least one dot after the '@'.
#
# Test cases:
# 1) Normal:
#    Input: "user123@gmail.com"
#    Output: Valid email: true
#            Domain: gmail.com
#
# 2) Border:
#    Input: "  test.user@outlook.mx  "
#    Output: Valid email: true
#            Domain: outlook.mx
#
# 3) Error:
#    Input: "user@@mail.com"
#    Output: Valid email: false
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

email_text = input("Enter email: ").strip()

# Validation: empty input
if len(email_text) == 0:
    print("Valid email: false")

# Validation: must not contain spaces
elif " " in email_text:
    print("Valid email: false")

# Validation: must contain exactly one '@'
elif email_text.count("@") != 1:
    print("Valid email: false")

else:
    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]  # slice after '@'

    # Validation: domain must contain at least one dot
    if "." not in domain_part:
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {domain_part}")

# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# ------------------------------------------------------------
# Description:
# This program checks if a phrase is a palindrome. It removes spaces
# and converts everything to lowercase before comparing the text with
# its reversed version. If both are equal, the phrase is a palindrome.
#
# Inputs:
# - phrase (string): any text entered by the user.
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - Optional: prints the normalized phrase.
#
# Validations:
# - The input must not be empty after strip().
# - After removing spaces, the length must be at least 3 characters.
#
# Test cases:
# 1) Normal:
#    Input: "Anita lava la tina"
#    Output: Is palindrome: true
#
# 2) Border:
#    Input: "  oso  "
#    Output: Is palindrome: true
#
# 3) Error:
#    Input: "  "
#    Output: Is palindrome: false
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

phrase = input("Enter phrase: ").strip()

# Validation: empty input
if len(phrase) == 0:
    print("Is palindrome: false")
else:
    # Normalize: lowercase + remove spaces
    normalized = phrase.lower().replace(" ", "")

    # Validation: must have at least 3 characters
    if len(normalized) < 3:
        print("Is palindrome: false")
    else:
        # Reverse using slicing
        reversed_text = normalized[::-1]

        if normalized == reversed_text:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")

# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# ------------------------------------------------------------
# Description:
# This program analyzes a sentence by normalizing the text, splitting
# it into words, and showing basic statistics such as the number of
# words, the first and last word, and the shortest and longest word.
#
# Inputs:
# - sentence (string): a sentence entered by the user.
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - The input must not be empty after strip().
# - After splitting, there must be at least one word.
#
# Test cases:
# 1) Normal:
#    Input: "Python is very powerful"
#    Output: Word count: 4
#            First word: Python
#            Last word: powerful
#            Shortest word: is
#            Longest word: powerful
#
# 2) Border:
#    Input: "   hello   "
#    Output: Word count: 1
#            First word: hello
#            Last word: hello
#            Shortest word: hello
#            Longest word: hello
#
# 3) Error:
#    Input: "   "
#    Output: No valid words
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

sentence = input("Enter sentence: ").strip()

# Validation: empty input
if len(sentence) == 0:
    print("No valid words")
else:
    words = sentence.split()

    # Validation: check if list is empty
    if len(words) == 0:
        print("No valid words")
    else:
        # Basic stats
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        # Find shortest and longest words (simple loop)
        shortest = words[0]
        longest = words[0]

        for word in words:
            if len(word) < len(shortest):
                shortest = word
            if len(word) > len(longest):
                longest = word

        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")
# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 5: Password strength classifier
# ------------------------------------------------------------
# Description:
# This program classifies a password as weak, medium, or strong using
# simple rules based on length and character types. The program checks
# if the password contains uppercase letters, lowercase letters,
# digits, and symbols.
#
# Inputs:
# - password_input (string): the password entered by the user.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password must not be empty.
# - Length is checked using len().
#
# Rules used (simple version):
# - Weak: length < 8 OR only letters (all lowercase or all uppercase).
# - Medium: length >= 8 and has mix of letters or digits.
# - Strong: length >= 8 and includes at least:
#           * one uppercase
#           * one lowercase
#           * one digit
#           * one symbol (!, @, #, etc.)
#
# Test cases:
# 1) Normal:
#    Input: "Hello123!"
#    Output: Password strength: strong
#
# 2) Border:
#    Input: "abcd1234"
#    Output: Password strength: medium
#
# 3) Error:
#    Input: ""
#    Output: Error: empty password
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

password_input = input("Enter password: ")

# Validation: empty password
if len(password_input.strip()) == 0:
    print("Error: empty password")
else:
    # Flags for types of characters
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password_input:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True

    # Classification
    length = len(password_input)

    if length < 8:
        print("Password strength: weak")
    else:
        if has_upper and has_lower and has_digit and has_symbol:
            print("Password strength: strong")
        else:
            print("Password strength: medium")

# ------------------------------------------------------------
# ------------------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# ------------------------------------------------------------
# Description:
# Generates a product label on one line with the format:
# Product: <NAME> | Price: $<PRICE>
# The final label must be exactly 30 characters long.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - A single label of exactly 30 characters
# - Shown inside quotes so spaces are visible
#
# Validations:
# - product_name must not be empty after strip()
# - price_value must be a positive number
# - If too long, cut to 30 characters; if short, pad with spaces
#
# Test cases:
# 1) Normal:
#    Input: product_name="Apple", price_value="12.5"
#    Output: "Product: Apple | Price: $12.5  "
#
# 2) Border:
#    Input: product_name="UltraMegaSuperProductName", price_value="999"
#    Output: first 30 characters only
#
# 3) Error:
#    Input: product_name="", price_value="abc"
#    Output: error messages
#
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

# Validate product name
if not product_name:
    print("Error: product name cannot be empty.")

# Validate price (allow one decimal point)
elif not price_value.replace(".", "", 1).isdigit():
    print("Error: price must be a positive number.")

else:
    price = float(price_value)

    if price <= 0:
        print("Error: price must be positive.")
    else:
        # Build base label
        label = f"Product: {product_name} | Price: ${price}"

        # Make label exactly 30 characters
        if len(label) > 30:
            label = label[:30]      # cut extra characters
        else:
            label = label.ljust(30) # pad with spaces

        print(f'Label: "{label}"')
# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Working with strings is essential because most user inputs and
# program outputs are text, so knowing how to clean and format them
# is critical. Functions like lower(), strip(), and split() help
# normalize text, making comparisons more accurate and avoiding
# unexpected errors. Validations play an important role because
# they prevent invalid or messy data from entering the program.
# I also learned that strings are immutable, so every change creates
# a new string, and slices give a simple way to extract or modify
# specific parts without using complex operations.
# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Documentation – Built-in Types: Text Sequence Type — str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Python Official Tutorial – Chapter on Strings
#    https://docs.python.org/3/tutorial/introduction.html#strings
#
# 3) "Automate the Boring Stuff with Python" – Al Sweigart
#    Sections on string manipulation and input validation.
#
# 4) Real Python – Articles about string methods and best practices
#    https://realpython.com/python-strings/
#
# 5) "Introduction to Algorithms and Programming" – Course notes
#    Chapters on text processing, slicing, and basic algorithms.
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------

