from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'location', 'is_verified', 'is_staff']
    list_filter = ['location', 'is_verified', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {'fields': ('phone_number', 'location', 'circonscription', 'profile_picture', 'is_verified')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations supplémentaires', {'fields': ('phone_number', 'location', 'circonscription')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
