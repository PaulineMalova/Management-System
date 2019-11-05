from django.contrib import admin

from .models import Course



class CourseAdmin(admin.ModelAdmin):
	list_display = ("name", "teacher", "course_description", "duration_in_months")
	search_fields = ("name", "teacher__first_name")

admin.site.register(Course, CourseAdmin)
