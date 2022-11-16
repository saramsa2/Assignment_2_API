from django.contrib.auth.models import User, Group
from django.core.files import File
from django.core.mail import send_mail
from django.forms import FileField
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from attendance.models import Semester, Class, Course, Student, Lecturer, CollegeDay


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CollegeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDay
        fields = ["id", "theClass", "date", "student", "attendance"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', ]

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many = True, required=False)

    class Meta:
        model = User
        fields = ["id", "username", 'password', "first_name", "last_name",'email', 'groups']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Student
        fields = ["student_id", "user", "DOB"]

    def create(self, validated_data):
        new_user = validated_data.pop("user")
        user = User.objects.create_user(**new_user)
        user.groups.add(1)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        new_user = validated_data.pop("user")
        user = User.objects.get(id=instance.user.id)
        user.first_name = new_user.get("first_name")
        user.last_name = new_user.get("last_name")
        user.email = new_user.get("email")
        user.save()
        instance.DOB = validated_data.get("DOB")
        instance.save()
        return instance

class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Lecturer
        fields = ["staff_id", "user", "DOB"]

    def create(self, validated_data):
        new_user = validated_data.pop("user")
        user = User.objects.create_user(**new_user)
        user.groups.add(2)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        return lecturer

    def update(self, instance, validated_data):
        new_user = validated_data.pop("user")
        user = User.objects.get(id=instance.user.id)
        user.email = new_user.get("email")
        user.first_name = new_user.get("first_name")
        user.last_name = new_user.get("last_name")
        user.save()
        instance.DOB = validated_data.get("DOB")
        instance.save()
        return instance

class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    receiver = serializers.EmailField()
    body = serializers.CharField()





