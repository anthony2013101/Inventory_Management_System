class Course:
    def __init__(self, course_code, course_name, teacher):
        self.course_code = course_code
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    # Implement additional course-related methods here