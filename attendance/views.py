
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from attendance.models import Semester, Class, Course, Student, Lecturer, CollegeDay
from attendance.permissions import IsAdmin, IsLecturer
from attendance.serializers import SemesterSerializer, ClassSerializer, CourseSerializer, StudentSerializer, \
    LecturerSerializer, CollegeDaySerializer, UserSerializer, GroupSerializer, SendEmailSerializer


def index(request):
    return HttpResponse("This attendance API response")


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdmin, ]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin, ]

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin, ]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin, ]

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin, ]

class CollegeDayViewSet(viewsets.ModelViewSet):
    queryset = CollegeDay.objects.all()
    serializer_class = CollegeDaySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin, ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAdmin, ]

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def User_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def User_group(request):
    user_group = request.user.groups
    serializers = GroupSerializer(user_group, many=True)
    return Response(serializers.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Send_Email(request):
    serializer = SendEmailSerializer(request.data)
    subject = serializer.data.get("subject")
    body = serializer.data.get("body")
    receiver = serializer.data.get("receiver")
    sender = "saramsa2@gmail.com"
    send_mail(subject, body, sender, [receiver], fail_silently=False)
    return Response(serializer.data)
