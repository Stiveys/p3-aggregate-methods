class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def enroll_student(self, enrollment):
        self._enrollments.append(enrollment)