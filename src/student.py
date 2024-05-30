class Student:
    def __init__(self, student_id, name, username, password):
        self.student_id = student_id
        self.name = name
        self.username = username
        self.password = password
        self.courses = []

    # Implement additional student-related methods here