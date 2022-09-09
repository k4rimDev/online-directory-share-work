from projects.models import Project, Tag, Review
from django.db.models import QuerySet, Q


# Get all projects
def get_projects() -> QuerySet:
    return Project.objects.all()

# Get filtered projects
def get_filtered_projects(search_query: str) -> QuerySet:
    tags = Tag.objects.filter(name__icontains=search_query)
    print('asfasf', search_query)
    return Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
 
# Get one project
def get_project(id: int) -> QuerySet:
    return Project.objects.filter(id = id)[0]