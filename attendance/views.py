from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from attendance.models import Semester, Class, Course, Student, Lecturer, CollegeDay
from attendance.permissions import IsAdmin
from attendance.serializers import SemesterSerializer, ClassSerializer, CourseSerializer, StudentSerializer, \
    LecturerSerializer, CollegeDaySerializer, UserSerializer


def index(request):
    return HttpResponse("This attendance API response")



class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdmin, ]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

class CollegeDayViewSet(viewsets.ModelViewSet):
    queryset = CollegeDay.objects.all()
    serializer_class = CollegeDaySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]


