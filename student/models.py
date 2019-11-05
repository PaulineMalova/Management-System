from django.db import models
from course.models import Course
import datetime
from django.core.exceptions import ValidationError

# Create your models here.
#Note the conventions
#CharField is a class inside the models thingie.
#max_length is not always required.
#Include this app in the settings.py file as part of the INSTALLED APPS - to make the app discoverable by django.
#This enables it to be converted into a database table.

# from .models import Student
# admin.site.register(Student)

#The two above are to be added to admin.py
class Student(models.Model) :  #Inheritance of attributes of another class. Model class in models.
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()  #Empty brackets because date formats are standard. No need for length declaration.
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 20)
	date_joined = models.DateField()
	courses = models.ManyToManyField(Course, blank=True, related_name="students")
	image = models.ImageField(upload_to = "profile_pictures", blank = True)

	def __str__(self):
		return self.first_name

	def full_name(self):
		return (f"{self.first_name} {self.last_name}")

	def age(self):
		now = datetime.datetime.now()
		current_year = now.year
		year_of_birth = self.date_of_birth.year
		current_age = current_year - year_of_birth
		return current_age

	def clean(self):
		now = datetime.datetime.now()
		current_year = now.year
		year_of_birth = self.date_of_birth.year
		current_age = current_year - year_of_birth
		if current_age < 17:
			raise ValidationError("Age is smaller than limit")
		if current_age > 30:
			raise ValidationError("Age is greater than limit")
