from rest_framework import permissions


class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        print(request.user and request.user.is_authenticated)
        return True

    def has_object_permission(self, request, view, obj):
        print( obj.user == request.user)
        return True
