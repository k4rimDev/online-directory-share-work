from django.http import HttpResponse, HttpRequest 

from users.services.users import get_filtered_profiles, get_all_profiles


def search_profiles(request: HttpRequest) -> HttpResponse:
    search_query = ''
    profiles = get_all_profiles()

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        profiles = get_filtered_profiles(search_query)
    
    return search_query, profiles