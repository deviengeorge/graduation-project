from django.utils.module_loading import import_string
from rest_framework import serializers

# app folder
from .models import Course, Lecture

# Database Serializers


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


# Base Serializers


class AttendStudentSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        lecture_id = int(data.get('lecture_id'))

        # Perform the data validation.
        if not lecture_id:
            raise serializers.ValidationError({
                'lecture_id': 'This field is required.'
            })

        if not Lecture.objects.get(id=lecture_id):
            raise serializers.ValidationError({
                'lecture_id': 'This field is a wrong lecture_id.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'lecture_id': lecture_id,
        }
