from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['username', 'email', 'age']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
