from django.urls import path
from .views import (
    ListCoursesView,
    RetrieveUpdateDestroyCoursesView,
    CreateLecturesView,
    ListLecturesView,
    RetrieveUpdateDestroyLecturesView,
    ListAnnouncementsView,
    RetrieveUpdateDestroyAnnouncementsView,
    CreateAnnouncementsView,
    AttendStudentToLectureAPI,
)


urlpatterns = [
    path("courses/", ListCoursesView.as_view(), name="course-list"),
    path(
        "courses/<int:pk>",
        RetrieveUpdateDestroyCoursesView.as_view(),
        name="courses-details",
    ),
    # Lectures API
    path("lectures/create", CreateLecturesView.as_view()),
    path("lectures/", ListLecturesView.as_view()),
    path("lectures/<int:pk>", RetrieveUpdateDestroyLecturesView.as_view()),
    # Announcements API
    path("announcements/create", CreateAnnouncementsView.as_view()),
    path("announcements/", ListAnnouncementsView.as_view()),
    path("announcements/<int:pk>", RetrieveUpdateDestroyAnnouncementsView.as_view()),
    path("attendance/", AttendStudentToLectureAPI.as_view()),
]
