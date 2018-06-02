from rest_framework.permissions import BasePermission


class IsAuthenticatedAndAdmin(BasePermission):
    """
    Allow access to only users who are both authenticated and are admin
    """
    def has_permission(self, request, view):
        if request.method in ['POST','PUT','DELETE']:
            return request.user and request.user.is_authenticated and request.user.is_staff
        return True