from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime

class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a = Student.objects.create(
            id = "1",
            first_name = "Pauline",
            last_name = "Brown",
            date_of_birth = datetime.date(1996, 9, 11),
            gender = "Female",
            registration_number = "SCT211-0002/2017",
            email = "perleebrown@gmail.com",
            phone_number = "0746574811",
            date_joined = datetime.date.today(),
        )
        self.student_b = Student.objects.create(
            id = "2",
            first_name = "Addah",
            last_name = "Brown",
            date_of_birth = datetime.date(1994, 2, 12),
            gender = "Female",
            registration_number = "SCT211-0003/2014",
            email = "addahbrown@gmail.com",
            phone_number = "0710426080",
            date_joined = datetime.date.today(),
        )
        self.python = Course.objects.create(
            name = "Python",
            duration_in_months = 9,
            start_date = datetime.date(2019,2,11),
            end_date = datetime.date(2019,11,15),
            course_description = "Backend development",
        )
        self.javascript = Course.objects.create(
            name = "Java Script",
            duration_in_months = 9,
            start_date = datetime.date(2019,2,14),
            end_date = datetime.date(2019,11,15),
            course_description = "Frontend development",
        )
        self.android = Course.objects.create(
            name = "Android",
            duration_in_months = 8,
            start_date = datetime.date(2019,3,11),
            end_date = datetime.date(2019,11,15),
            course_description = "Android apps development",
        )

    def test_student_can_join_a_course(self):
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)
    
    def test_student_can_join_multiple_courses(self):
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(), 2)
        self.student_a.courses.add(self.android)
        self.assertEqual(self.student_a.courses.count(), 3)

    def test_student_can_add_multiple_courses_at_once(self):
        self.student_b.courses.add(self.python, self.javascript, self.android)
        self.assertEqual(self.student_b.courses.count(), 3)  