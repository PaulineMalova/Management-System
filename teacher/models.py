from django.db import models

# Create your models here.
class Teacher(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	gender = models.CharField(max_length = 20)
	id_number = models.BigIntegerField()
	email = models.EmailField(max_length = 50)
	phone_number = models.CharField(max_length = 20)
	date_employed = models.DateField()
	profession = models.CharField(max_length = 50)
	subject_taught = models.CharField(max_length = 30)
	image = models.ImageField(upload_to = "profile_pictures", blank = True)

	def __str__(self):
		return self.first_name