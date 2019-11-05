from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer
from student.models import Student
from teacher.models import Teacher
from course.models import Course

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer