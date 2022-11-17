from rest_framework import permissions

# safe_method = ["GET"]

class IsAdmin(permissions.BasePermission):
    message = "You are not administrator"

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list("name", flat=True)
        if request.method == "GET":
            return True
        elif "Admin" in user_groups:
            return True
        return False

class IsLecturerOrAdminOrReadOnly(permissions.BasePermission):
    message = "You are not administrator or Lecturer"

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list("name", flat=True)
        if request.method == "GET":
            return True
        elif "Lecturer" in user_groups or "Admin" in user_groups:
            return True
        return False
