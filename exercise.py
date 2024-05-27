# Parent class
class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class for Students
class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        # Call the constructor of the parent class
        super().__init__(name, age, cid_number)
        # Initialize specific attributes for Student
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Child class for Teachers
class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        # Call the constructor of the parent class
        super().__init__(name, age, cid_number)
        # Initialize specific attributes for Teacher
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Creating objects
# Create a Student object
student = Student(name="Alice", age=20, cid_number="S123456", student_id="1001", course="Computer Science", year=2, gpa=3.8)
student.walk()
student.study()
student.attend_class()
student.write_exam()

# Create a Teacher object
teacher = Teacher(name="Mr. Smith", age=45, cid_number="T654321", subject="Mathematics", salary=50000, department="Mathematics", designation="Senior Lecturer")
teacher.walk()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()
