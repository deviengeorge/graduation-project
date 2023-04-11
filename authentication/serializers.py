from rest_framework import serializers
from .models import User, TeacherProfile, StudentProfile

from app.serializers import CourseSerializer

from djoser.serializers import UserCreateSerializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'name', 'user_type']


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'name', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            user_type=validated_data['user_type']
        )

        user.set_password(validated_data['password'])
        user.save()

        if user.user_type == user.TEACHER:
            teacher_profile = TeacherProfile(user=user)
            teacher_profile.save()

        elif user.user_type == user.STUDENT:
            student_profile = StudentProfile(user=user)
            student_profile.save()

        return user


class TeacherProfileSerializer(serializers.ModelSerializer):
    courses_taught = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ['courses_taught']


class StudentProfileSerializer(serializers.ModelSerializer):

    courses_attended = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['courses_attended', 'grade', 'department']


class UserSerializer(serializers.ModelSerializer):
    teacher_profile = TeacherProfileSerializer(read_only=True)
    student_profile = StudentProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name',
                  'teacher_profile', 'student_profile', 'user_type']
