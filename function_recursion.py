# Problem Statement: Write a recursive function sum_of_digits(n) that takes a
# non-negative integer n as input and returns the sum of its digits.
# For example:
# sum_of_digits(123) should return 6 because 1 + 2 + 3 = 6.
# sum_of_digits(9876) should return 30 because 9 + 8 + 7 + 6 = 30.

def sum_of_digits(n):
    # Base case: if n is a single-digit number, return n
    if n < 10:
        return n
    else:
        # Recursive case: extract the last digit, remove it from n, and recursively
        # call sum_of_digits on the remaining digits, then add the last digit
        return n % 10 + sum_of_digits(n // 10)

# Test cases
print(sum_of_digits(123))   # Output: 6
print(sum_of_digits(9876))  # Output: 30
print()

# Exercise:
# Write a recursive function reverse_string(s) that reverses the order of characters in a given
# string.
# Examples:
# If the input string is "hello", the function should return "olleh".
# If the input string is "python", the function should return "nohtyp".
# If the input string is an empty string "", the function should return an empty string "".
# The function should follow a recursive approach, meaning it should call itself with a smaller
# portion of the input until it reaches the base case.

def reverse_string(s):
    # Base case: if the string is empty or contains only one character,
    # return the string as it is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: separate the first character from the rest of the string
        # and recursively call reverse_string on the rest, then append the first character
        # to the end of the reversed string
        return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python"))  # Output: "nohtyP"
print(reverse_string(""))       # Output: ""
