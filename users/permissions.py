from rest_framework.permissions import BasePermission
from .models import UserType

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == UserType.MANAGER.value

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == UserType.CUSTOMER.value
