from django.contrib import admin

from users import models


@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "username", )
    search_fields = ("username", )

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "subject",)
    search_fields = ("sender", "recipient", "subject",)
