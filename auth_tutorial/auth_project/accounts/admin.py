from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

# from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser

#
# class CustomUserAdmin(UserAdmin):
#     # add_form = CustomUserCreationForm
#     # form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'region', 'phone_number']
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
