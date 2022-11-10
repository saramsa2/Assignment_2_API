from rest_framework import serializers

from attendance.models import Semester, Class, Course, Student, Lecturer


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    semester = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    class Meta:
        model = Class
        # fields = '__all__'
        fields = ["id", "number", "semester", 'course']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        extra_kwargs={'password':{
            'wite_only': True,
            'required': True
        }}

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'
