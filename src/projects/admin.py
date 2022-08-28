from django.contrib import admin

from .models import Project, Tag, Review

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(Tag)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )


@admin.register(Review)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project', 'body',)
    search_fields = ('project', )