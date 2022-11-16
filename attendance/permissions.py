from rest_framework import permissions

# safe_method = ["GET"]

class IsAdmin(permissions.BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return obj.author == request.user

    message = "You are not administrator"

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Admin" in user_groups:
            return True
        return False

class IsLecturer(permissions.BasePermission):
    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Lecturer" in user_groups:
            return True
        return False
