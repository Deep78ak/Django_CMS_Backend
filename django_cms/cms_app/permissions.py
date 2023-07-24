from rest_framework import permissions

from .models import CMSUser


class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
