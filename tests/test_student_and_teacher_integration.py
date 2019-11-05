from teacher.models import Teacher
from student.models import Student
from course.models import Course
from django.test import TestCase
import datetime

class StudentTeacherTestCase(TestCase):
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

    def test_one_trainer_and_many_students_can_have_one_course(self):
        self.student_a.courses.add(self.python)
        self.student_b.courses.add(self.python)
        self.python.teacher = self.teacher_a
    
    def test_one_trainer_and_many_students_can_have_many_course(self):
        self.student_b.courses.add(self.python, self.electronics, self.hardware_design)   
        self.electronics.teacher = self.teacher_b
        self.hardware_design.teacher = self.teacher_b
        self.python.teacher = self.teacher_a
        