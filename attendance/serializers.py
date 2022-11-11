from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from attendance.models import Semester, Class, Course, Student, Lecturer, CollegeDay


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    # semester = serializers.StringRelatedField(read_only=True)
    # course = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Class
        # fields = '__all__'
        fields = ["id", "number", "semester", 'course', "student"]

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
        fields = ["id", "username", 'password', 'groups']

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

class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Lecturer
        fields = ["staff_id", "user", "DOB"]

    def create(self, validated_data):
        new_user = validated_data.pop("user")
        user = User.objects.create_user(**new_user)
        user.groups.add(2)
        student = Lecturer.objects.create(user=user, **validated_data)
        return student
