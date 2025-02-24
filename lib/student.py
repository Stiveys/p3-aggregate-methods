class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, enrollment):
        self._enrollments.append(enrollment)
        self._grades[enrollment] = None  # Initially no grade assigned

    def set_grade(self, enrollment, grade):
        if enrollment in self._grades:
            self._grades[enrollment] = grade

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(grade for grade in self._grades.values() if grade is not None)
        num_courses = len([grade for grade in self._grades.values() if grade is not None])
        return total_grades / num_courses if num_courses > 0 else 0