# Prompt user for input
height = int(input("Enter the height of the triangle (number of rows): "))

# Generate right triangle pattern using nested loops
print("Right triangle pattern:")
for i in range(1, height + 1):
    print("*" * i)
