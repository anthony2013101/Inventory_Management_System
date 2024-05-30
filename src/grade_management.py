from student import Student
from course import Course

class GradeManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    # Implement grade management methods here

    def add_student(self, student):
        self.students.append(student)

    # Add more grade management methods as needed