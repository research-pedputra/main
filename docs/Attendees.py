class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {super().__str__()}, Student ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Teacher: {super().__str__()}, Employee ID: {self.employee_id}"

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def list_students(self):
        print(f"Students at {self.name}:")
        for student in self.students:
            print(student)

    def list_teachers(self):
        print(f"Teachers at {self.name}:")
        for teacher in self.teachers:
            print(teacher)

def main():
    school = School("ABC School")

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. List Students")
        print("4. List Teachers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            student_id = input("Enter student ID: ")
            student = Student(name, age, student_id)
            school.add_student(student)
        elif choice == "2":
            name = input("Enter teacher's name: ")
            age = int(input("Enter teacher's age: "))
            employee_id = input("Enter employee ID: ")
            teacher = Teacher(name, age, employee_id)
            school.add_teacher(teacher)
        elif choice == "3":
            school.list_students()
        elif choice == "4":
            school.list_teachers()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()