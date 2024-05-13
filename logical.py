# logical.py

# AND operator examples
x = 5
y = 15

# Example 1
result1 = (x > 3) and (x < 10)
print("Example 1 (AND):", result1)

# Example 2
result2 = (y > 10) and (y % 5 == 0)
print("Example 2 (AND):", result2)

# OR operator examples
# Assume x and y are defined as before

# Example 1
result3 = (x < 3) or (x > 10)
print("Example 1 (OR):", result3)

# Example 2
result4 = (y > 10) or (y % 2 == 0)
print("Example 2 (OR):", result4)

# NOT operator examples
# Assume x and y are defined as before

# Example 1
result5 = not (x > 3 and x < 10)
print("Example 1 (NOT):", result5)

# Example 2
result6 = not (y > 10 and y % 5 == 0)
print("Example 2 (NOT):", result6)

# Exercise: Eligibility for movie ticket discount

# Ask for user input
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

# Check eligibility for discount
if age <= 12:
    print("You are eligible for a discount on the movie ticket.")
elif 13 <= age <= 18 and is_student == "yes":
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount on the movie ticket.")
