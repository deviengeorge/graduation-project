from django.utils.module_loading import import_string
from rest_framework import serializers

# app folder
from .models import Course, Lecture


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    # teacher = LazyRefSerializer('authentication.serializers.UserSerializer')

    class Meta:
        model = Lecture
        fields = ['id', 'date', 'course', 'teacher']

    def to_representation(self, instance):
        from authentication.serializers import UserCreateSerializer
        data = super().to_representation(instance)
        data['teacher'] = UserCreateSerializer(instance.teacher).data
        return data
