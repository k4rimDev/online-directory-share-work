from django.http import HttpResponse, HttpRequest
from projects.services.projects import get_filtered_projects, get_projects

def search_project(request: HttpRequest) -> HttpResponse:
    search_query = ''
    projects = get_projects()

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        projects = get_filtered_projects(search_query)
        print("kerim", search_query, projects)

    return search_query, projects