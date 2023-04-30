from rest_framework import serializers

# app folder
from .models import Course, Lecture, Announcement

# Database Serializers


class LectureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ["name", "qr_exp_mins", "date", "latitude", "longitude", "course"]


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"

    def to_representation(self, instance):
        from authentication.serializers import UserCreateSerializer

        data = super().to_representation(instance)
        # data['course'] = CourseSerializer(instance.course).data
        data["teacher"] = UserCreateSerializer(instance.teacher).data
        return data


class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["pk", "name", "code", "lectures"]


class AttendStudentSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        lecture_id = int(data.get("lecture_id"))

        # Perform the data validation.
        if not lecture_id:
            raise serializers.ValidationError({"lecture_id": "This field is required."})

        if not Lecture.objects.get(id=lecture_id):
            raise serializers.ValidationError(
                {"lecture_id": "This field is a wrong lecture_id."}
            )

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            "lecture_id": lecture_id,
        }


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ["pk", "title", "description", "course"]
