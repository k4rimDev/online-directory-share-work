from atexit import register
from django.contrib import admin
from . import models

@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", )
    search_fields = ("username", )
