from rest_framework import generics
from rest_framework.exceptions import JsonResponse
from rest_framework.views import APIView
from .models import Course, Lecture, Announcement
from .serializers import (
    CourseSerializer,
    LectureSerializer,
    LectureCreateSerializer,
    AttendStudentSerializer,
    AnnouncementSerializer,
)

# Permissions Classes
from authentication import permissions


# Courses Views
class ListCoursesView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetrieveUpdateDestroyCoursesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = [permissions.IsAdminOrTeacherNotGETMethod]


# Lectures Views
class CreateLecturesView(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureCreateSerializer
    permission_classes = [permissions.IsTeacher]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ListLecturesView(generics.ListAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        course_id = self.request.query_params.get("course_id")
        return Lecture.objects.filter(course=course_id)


class RetrieveUpdateDestroyLecturesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    permission_classes = [permissions.IsAdminOrTeacherNotGETMethod]


class CreateAnnouncementsView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAdminOrTeacher]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ListAnnouncementsView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        course_id = self.request.query_params.get("course_id")
        return Announcement.objects.filter(course=course_id)


class RetrieveUpdateDestroyAnnouncementsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    permission_classes = [permissions.IsAdminOrTeacherNotGETMethod]


# Attendance Views
class AttendStudentToLectureAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AttendStudentSerializer(
            data={"lecture_id": request.data.get("lecture_id")}
        )

        if serializer.is_valid():
            print(f"Lecture ID: {serializer.data['lecture_id']}")
            lecture = Lecture.objects.filter(id=serializer.data["lecture_id"]).first()
            return LectureSerializer(data=lecture)
