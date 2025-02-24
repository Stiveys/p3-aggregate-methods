from lib.student import Student
from lib.course import Course
from lib.enrollment import Enrollment
from datetime import datetime

# Create students
student1 = Student("Alice")
student2 = Student("Bob")

# Create courses
course1 = Course("Math")
course2 = Course("Science")

# Create enrollments
enrollment1 = Enrollment(student1, course1, datetime(2023, 9, 1))
enrollment2 = Enrollment(student1, course2, datetime(2023, 9, 1))
enrollment3 = Enrollment(student2, course1, datetime(2023, 9, 2))

# Set grades
student1.set_grade(enrollment1, 85)
student1.set_grade(enrollment2, 90)

# Aggregate methods
print(f"Number of courses Alice is enrolled in: {student1.course_count()}")  # Output: 2
print(f"Alice's average grade: {student1.aggregate_average_grade()}")  # Output: 87.5
print(f"Enrollments per day: {Enrollment.aggregate_enrollments_per_day()}")  # Output: {datetime.date(2023, 9, 1): 2, datetime.date(2023, 9, 2): 1}