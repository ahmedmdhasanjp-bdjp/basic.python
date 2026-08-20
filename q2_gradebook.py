class Student:
    next_id = 1

    def __init__(self, name, grade, email=None):
        self.student_id = Student.next_id
        Student.next_id += 1
        self.name = name
        self.grade = grade
        self.email = email
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Email: {self.email}"

class GradeBook:

    def __init__(self):
        self.students = []

    def add_student(self, name, grade, email=None):
        student = Student(name, grade, email)
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        for student in self.students:
            print(student)

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                return
        print("Student not found.")

    def update_grade(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.grade = new_grade
                print("Grade updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

gradebook = GradeBook()

gradebook.add_student("Tanvir", "A", "tanvir@email.com")

gradebook.add_student("Nusrat", "B+")

gradebook.add_student("Rakib", "A-", "rakib@email.com")

gradebook.view_students()

print("\n-- Search --")

gradebook.search_student(2)

print("\n-- Update --")

gradebook.update_grade(3, "A")

print("\n-- Delete --")

gradebook.delete_student(2)

gradebook.view_students()