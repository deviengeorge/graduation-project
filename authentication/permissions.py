from rest_framework import permissions
from .models import User


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.ADMIN:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.TEACHER:
            return True
        return False


class IsAdminOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
            request.user.user_type == User.ADMIN
            or request.user.user_type == User.TEACHER
        ):
            return True
        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.STUDENT:
            return True
        return False


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAdminOrTeacherNotGETMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return IsAdminOrTeacher().has_permission(request, view)


class IsAdminNotGETMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return IsAdmin().has_permission(request, view)
