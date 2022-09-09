from django.http import HttpResponse, HttpRequest 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from users.services.users import get_filtered_profiles, get_all_profiles
from projects.utils import custom_range_for_pagination


def paginate_profiles(request: HttpRequest, profiles: list, results: list) -> HttpResponse:
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:  
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
        
    custom_range = custom_range_for_pagination(int(page), paginator)
    return custom_range, profiles

def search_profiles(request: HttpRequest) -> HttpResponse:
    search_query = ''
    profiles = get_all_profiles()

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        profiles = get_filtered_profiles(search_query)
    
    return search_query, profiles