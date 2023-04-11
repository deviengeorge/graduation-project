from rest_framework import generics
from rest_framework.views import APIView
from .models import Course, Lecture
from .serializers import CourseSerializer, LectureSerializer


class ListCoursesView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetrieveUpdateDestroyCoursesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ListLecturesView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class RetrieveUpdateDestroyLecturesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


# GET

class AttendanceAPI(APIView):
    def get(self, request, *args, **kwargs):
        lecture_id = int(request.data.get('lecture_id', 1))
        lecture = Lecture.objects.get(id=lecture_id)

        return LectureSerializer(data=lecture)
