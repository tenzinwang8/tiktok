# Prompt the user to enter the total number of students
num_students = int(input("Enter the total number of students: "))

# Initialize a counter variable for the current student
i = 1

# Loop through each student
while i <= num_students:
    # Initialize total grade for the current student
    total_grade = 0
    
    # Prompt the user to enter the number of subjects for the current student
    num_subjects = int(input(f"Enter the number of subjects for student {i}: "))
    
    # Loop through each subject for the current student
    for j in range(1, num_subjects + 1):
        # Prompt the user to enter the grade for the current subject
        grade = float(input(f"Enter the grade of subject {j} for student {i}: "))
        
        # Accumulate the grade to calculate total grade for the current student
        total_grade += grade
    
    # Calculate the average grade for the current student
    average_grade = total_grade / num_subjects
    
    # Print the average grade for the current student
    print(f"Average grade for student {i}: {average_grade:.2f}")
    
    # Move to the next student
    i += 1
