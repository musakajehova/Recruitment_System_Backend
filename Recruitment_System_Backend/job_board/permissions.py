from rest_framework.permissions import BasePermission

class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'person') and (request.user.person.role in ('recruiter', 'admin') or request.user.is_superuser)
    
class IsAdministator(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'person') and (request.user.person.role == 'admin' or request.user.is_superuser)
