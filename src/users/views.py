from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .services.users import get_all_profiles, get_profile, get_top_skills_profile, get_other_skills_profile, get_user_projects


def profiles(request: HttpRequest) -> HttpResponse:
    context = { 
        "profiles" : get_all_profiles(),
    }
    return render(request, "users/profiles.html", context=context)

def user_profile(request: HttpRequest, pk) -> HttpResponse:
    context = {
        "profile": get_profile(pk),
        "top_skills": get_top_skills_profile(pk),
        "other_skills": get_other_skills_profile(pk),
        "user_projects": get_user_projects(pk),
    }

    return render(request, "users/user-profile.html", context=context)
