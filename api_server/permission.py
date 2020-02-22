from rest_framework import permissions
from django.conf import settings

from jose import jwt, JWTError

class canCreatePoint(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            token = request.headers['Authorization'].split(' ',1)[-1]
            jwt.decode(token, settings.SECRET_KEY_TOKEN, algorithms=['HS256'])
        except (JWTError,KeyError):
            return False
        return True
