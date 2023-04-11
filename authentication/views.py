from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# authentication folder
from .models import User, TeacherProfile, StudentProfile
from .serializers import UserSerializer, UserCreateSerializer, TeacherProfileSerializer, StudentProfileSerializer

# app folder
from app.models import Course


# Login Endpoint
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# REST API Best Practices
# /api/v1/users
# - GET ( list )
# - POST ( create ) DONE

# /api/v1/users/123
# - GET ( reterive )
# - PUT or PATCH ( Update )
# - DELETE ( delete )


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all().select_related(
        "teacher_profile", "student_profile")
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddCourseToTeacherView(generics.UpdateAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer

    def put(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')
        # user_id = kwargs.get('user_id', None)
        # course_id = kwargs.get('course_id', None)

        try:
            course = Course.objects.get(id=course_id)

        except Course.DoesNotExist:
            return Response({'message': 'Course not in the database.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            teacher_profile = TeacherProfile.objects.get(user__id=user_id)

            print(teacher_profile)
            print(type(teacher_profile.courses_taught))
            if course not in teacher_profile.courses_taught.all():
                teacher_profile.courses_taught.add(course)
                teacher_profile.save()
                return Response({'message': 'Course added to teacher.'}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Course already in teacher courses.'}, status=status.HTTP_400_BAD_REQUEST)

        except TeacherProfile.DoesNotExist:
            return Response({'message': 'Teacher profile not found.'}, status=status.HTTP_404_NOT_FOUND)


class RetrieveStudentView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({'error': 'Invalid credentials'})


class EnrollCourseView(generics.UpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    @csrf_exempt
    def put(self, request, *args, **kwargs):

        user_id = kwargs.get('user_id', None)
        course_id = kwargs.get('course_id', None)
        grade = request.data.get('grade', None)
        department = request.data.get('department', None)

        if not all([user_id, course_id, grade, department]):
            return Response({'message': 'Missing parameters'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(id=course_id)

        except Course.DoesNotExist:
            return Response({'message': 'Course does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        student_profile = get_object_or_404(StudentProfile, user__id=user_id)

        if student_profile:
            student_profile.courses_attended.add(course)
            student_profile.grade = grade
            student_profile.department = department
            student_profile.save()
            return Response({'message': 'Student enrolled in course.'}, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND)
