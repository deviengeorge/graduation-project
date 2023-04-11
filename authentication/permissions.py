from rest_framework import permissions
from .models import User


class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.ADMIN:
            return True
        return False


class isTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.TEACHER:
            return True
        return False


class isStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == User.STUDENT:
            return True
        return False


class isAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
