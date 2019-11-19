from django.test import TestCase
from .forms import CourseForm
import datetime
from django.test import Client
from django.urls import reverse

# Create your tests here.
class AddCourseTestCase(TestCase):
    def setUp(self):
        self.data = {
            "name": "Python",
            "duration_in_months": 10,
            "start_date": datetime.date(2019,2,11),
            "end_date": datetime.date(2019,11,15),
            "course_description": "Interesting course",
        }
        self.bad_data = {
            "name": "Python",
            "duration_in_months": 9,
            "start_date": datetime.date(2019,2,11),
            "end_date": datetime.date(2019,11,15),
            "course_description": 30,
            "teacher": "James Mwai",
        }

    def test_course_form_accepts_valid_data(self):
        form = CourseForm(self.data)
        self.assertTrue(form.is_valid())

    def test_course_form_rejects_invalid_data(self):
        form = CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_course_view(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code, 302)

    def test_add_course_view_for_bad_data(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)    
