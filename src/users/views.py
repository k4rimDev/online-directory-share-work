from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def profiles(request: HttpRequest) -> HttpResponse:
    context = { 

    }
    return render(request, "users/profiles.html", context=context)
