from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from projects.services.projects import get_filtered_projects, get_projects


def paginate_projects(request: HttpRequest, projects: list, results: int) -> list:
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:  
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
        
    custom_range = custom_range_for_pagination(int(page), paginator)
    return custom_range, projects


def search_project(request: HttpRequest) -> HttpResponse:
    search_query = ''
    projects = get_projects()

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        projects = get_filtered_projects(search_query)
        print("kerim", search_query, projects)

    return search_query, projects


def custom_range_for_pagination(page: int, paginator: Paginator) -> list:
    left_index = page - 2
    if left_index < 1:
        left_index = 1
    
    right_index = page + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    return range(left_index, right_index)