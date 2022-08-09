from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def projects(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects/projects.html')

def project(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects/single-project.html')