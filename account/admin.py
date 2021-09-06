from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm

CustomUser= get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreateForm
    form= CustomUserChangeForm
    model= CustomUser
    list_display= ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)