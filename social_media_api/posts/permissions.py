from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow safe methods for any request, but write methods only for the resource owner.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # For Post and Comment, check `author` attribute
        return hasattr(obj, 'author') and obj.author == request.user
