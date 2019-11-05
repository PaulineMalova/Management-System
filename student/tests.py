from django.test import TestCase
from .models import Student
from .forms import StudentForm
from django.test import Client
from django.urls import reverse
import datetime

# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name = "Pauline",
            last_name = "Brown",
            date_of_birth = datetime.date(1996, 9, 11),
            gender = "Female",
            registration_number = "SCT211-0002/2017",
            email = "perleebrown@gmail.com",
            phone_number = "0746574811",
            date_joined = datetime.date.today(),
        )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())    

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name()) 

    def test_age_is_always_above_seventeen(self):
        self.assertEqual((self.student.age()>17), True)

    def test_age_is_always_below_thirty(self):
        self.assertEqual((self.student.age()<30), True)


class AddStudentTestCase(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Pauline",
            "last_name": "Brown",
            "date_of_birth": datetime.date(1996,9,11),
            "gender": "Female",
            "registration_number": "SCT211-0002/2017",
            "email": "perleebrown@gmail.com",
            "phone_number": "0746574811",
            "date_joined": datetime.date.today(),
        }
        self.bad_data = {
            "first_name": "Pauline",
            "last_name": "Brown",
            "date_of_birth": datetime.date(1996,9,11),
            "gender": "Female",
            "registration_number": "SCT211-0002/2017",
            "email": "perlgmaicom",
            "phone_number": "0746574",
            "date_joined": datetime.date.today(),
        }

    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertTrue(form.is_valid())

    def test_student_rejects_invalid_data(self):
        form = StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())    

    def test_add_student_view(self):
        client = Client() #user
        url = reverse("add_student") #app name: url_name
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
    
    def test_add_student_view_for_bad_data(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)
   