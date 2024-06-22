from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, RequestLog

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'authentication_token', 'is_staff','is_superuser']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'user_type', 'authentication_token')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_active', 'is_staff')}
        ),
    )
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(RequestLog)
