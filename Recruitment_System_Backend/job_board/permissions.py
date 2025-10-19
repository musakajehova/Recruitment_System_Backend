from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model


class IsRecruiter(BasePermission):
    #def has_permission(self, request, view):
     #   return hasattr(request.user, 'person') and (request.user.person.role in ('recruiter', 'admin') or request.user.is_superuser)
    
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if hasattr(request.user, 'person'):
            return request.user.person.role in ['recruiter', 'admin']
        return False


class IsAdministator(BasePermission):
    #def has_permission(self, request, view):
        #return hasattr(request.user, 'person') and (request.user.person.role == 'admin' or request.user.is_superuser)

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if hasattr(request.user, 'person'):
            return request.user.person.role == 'admin'
        return False