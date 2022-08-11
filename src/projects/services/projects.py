from projects.models import Project, Tag, Review
from django.db.models import QuerySet

def get_projects() -> QuerySet:
    return Project.objects.all()

def get_project(id: int) -> QuerySet:
    return Project.objects.get(id = id)