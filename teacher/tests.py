from django.test import TestCase
from .forms import TeacherForm
from django.test import Client
from django.urls import reverse
import datetime
# Create your tests here.

class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "James",
            "last_name": "Mwai",
            "gender": "Male",
            "id_number": "2789643",
            "email": "smartemwa@gmail.com",
            "phone_number": "0734267854",
            "date_employed": datetime.date(2016,9,11),
            "profession": "CTO and Co-Founder",
            "subject_taught": "Python",
        }
        self.bad_data = {
            "first_name": "James",
            "last_name": "Mwai",
            "gender": "Male",
            "id_number": "2789643",
            "email": "smartemailm",
            "phone_number": "0734267854",
            "date_employed": datetime.date(2016,9,11),
            "profession": "CTO and Co-Founder",
            "subject_taught": "Python",
        }

    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())

    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())    

    def test_add_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 302)

    def test_add_teacher_view_for_bad_data(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)
