from django.contrib import admin

# Register your models here.
from .models import Teacher



class TeacherAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "email", "subject_taught","image")
	search_fields = ("first_name", "subject_taught")


admin.site.register(Teacher, TeacherAdmin)