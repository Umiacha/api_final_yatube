from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerOrReadOnly(BasePermission):
    """Разрешено чтение всем пользователям.
    Изменение объекта -- только автору.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user == obj.author
        )
