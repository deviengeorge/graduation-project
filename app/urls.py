from django.urls import path
from .views import (
    ListCoursesView,
    RetrieveUpdateDestroyCoursesView,
    ListLecturesView,
    RetrieveUpdateDestroyLecturesView,
    AttendanceAPI
)


urlpatterns = [
    path('courses/', ListCoursesView.as_view(), name='course-list'),
    path(
        'courses/<int:pk>',
        RetrieveUpdateDestroyCoursesView.as_view(),
        name="courses-details"
    ),
    path('lectures/', ListLecturesView.as_view()),
    path('lectures/<int:pk>', RetrieveUpdateDestroyLecturesView.as_view()),
    path('attendance/', AttendanceAPI.as_view())
]
