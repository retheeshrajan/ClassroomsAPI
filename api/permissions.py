from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    message = "You must be the teacher of this class to make changes."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.teacher == request.user):
            return True
        else:
            return False