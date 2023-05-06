from django.urls import path, include
from djoser.urls import jwt

from .views import (
    CreateUserView,
    ListUsersView,
    RetrieveUpdateDestroyUserView,
    AddCourseToTeacherView,
    RetrieveStudentView,
    EnrollCourseView,
    LoginView,
)

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Authentication with Djoser JWT
    path("auth/register", CreateUserView.as_view(), name="user-create"),
    path("auth/refresh", TokenRefreshView.as_view(), name="user-refresh"),
    path("auth/verify", TokenVerifyView.as_view(), name="user-verify"),
    path("auth/login", LoginView.as_view(), name="user-login"),
    path("users/", ListUsersView.as_view(), name="user-list"),
    # Retrieve => POST
    # Update => PUT
    # Destory => DELETE
    path("users/<int:pk>", RetrieveUpdateDestroyUserView.as_view(), name="user-detail"),
    path(
        "teachers/<int:user_id>/add_course/<int:course_id>/",
        AddCourseToTeacherView.as_view(),
        name="teacher-course",
    ),
    path(
        "students/<int:user_id>/retrieve/",
        RetrieveStudentView.as_view(),
        name="student-retrieve",
    ),
    path(
        "students/<int:user_id>/enroll_course/<int:course_id>/",
        EnrollCourseView.as_view(),
        name="student-enroll",
    ),
]
