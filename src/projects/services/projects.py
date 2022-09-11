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

# Get or create review for api
def get_or_create_review(pk: str, user: str, project: QuerySet) -> QuerySet:
    review, created = Review.objects.get_or_create(
        owner = user,
        project = project
    )

    return review, created