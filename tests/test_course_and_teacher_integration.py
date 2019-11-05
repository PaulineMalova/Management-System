from course.models import Course
from teacher.models import Teacher
from django.test import TestCase
import datetime

class CourseTeacherTestCase(TestCase):
    def setUp(self):
        self.teacher_a = Teacher.objects.create(
            first_name = "James",
            last_name = "Mwai",
            gender = "Male",
            id_number = "2789643",
            email = "smartemwa@gmail.com",
            phone_number = "0734267854",
            date_employed = datetime.date(2016,9,11),
            profession = "CTO and Co-Founder",
            subject_taught = "Python",
        )
        self.teacher_b = Teacher.objects.create(
            first_name = "Barre",
            last_name = "Yassin",
            gender = "Male",
            id_number = "2989643",
            email = "akliyobarre@gmail.com",
            phone_number = "0787347854",
            date_employed = datetime.date(2016,9,11),
            profession = "Product Designer and Founder",
            subject_taught = "Electronics",
        )
        self.python = Course.objects.create(
            name = "Python",
            duration_in_months = 9,
            start_date = datetime.date(2019,2,11),
            end_date = datetime.date(2019,11,15),
            course_description = "Backend development",
        )
        self.electronics = Course.objects.create(
            name = "Electronics",
            duration_in_months = 9,
            start_date = datetime.date(2019,2,14),
            end_date = datetime.date(2019,11,15),
            course_description = "Arduino",
        )
        self.hardware_design = Course.objects.create(
            name = "Hardware Design",
            duration_in_months = 8,
            start_date = datetime.date(2019,3,11),
            end_date = datetime.date(2019,11,15),
            course_description = "Design thinking and fusion",
        )

    def test_course_can_have_one_teacher(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher, self.teacher_a)

    def test_course_cannot_have_many_teachers(self):
        self.python.teacher = self.teacher_a
        self.python.teacher = self.teacher_b
        self.assertFalse(self.python.teacher==self.teacher_a)

    def test_many_courses_can_have_one_trainer(self):
        self.electronics.teacher = self.teacher_b
        self.hardware_design.teacher = self.teacher_b
        self.assertEqual(self.electronics.teacher, self.hardware_design.teacher)
        