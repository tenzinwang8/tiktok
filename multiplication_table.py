# Prompt user for input
number = int(input("Enter the number for multiplication table: "))
limit = int(input("Enter the limit for multiplication table: "))

# Generate multiplication table using nested loops
print(f"Multiplication table for {number} up to {limit}:")
for i in range(1, limit+1):
    print(f"{number} * {i} = {number * i}")
