from rest_framework import generics
from rest_framework.views import APIView
from .models import Course, Lecture
from .serializers import CourseSerializer, LectureSerializer, AttendStudentSerializer


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


class AttendStudentToLectureAPI(APIView):
    # Create a New Lecture ( Teacher Prespective )
    def post(self, request, *args, **kwargs):

        validated_data = AttendStudentSerializer(
            data={"lecture_id": request.data.get('lecture_id')})
        print(validated_data)
        # lecture = Lecture.objects.create(id=lecture_id)

        # return LectureSerializer(data=lecture)


# Teacher
# create lecture
