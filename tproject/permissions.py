from rest_framework.permissions import BasePermission


class ImagePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        if request.user.is_staff:
            return True
        # check for custom permissions here
        return False
class ImagePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        if request.user.is_staff:
            return True
        level = request.user.level
        if not level:
            return False
        if level.original_url and request.method == 'GET':
            return True
        if obj.thumbnail_200 and '200' in level.thumbnail_sizes:
            return True
        if obj.thumbnail_400 and '400' in level.thumbnail_sizes:
            return True
        if level.expiring_link and obj.expiration_time:
            return True
        return False
