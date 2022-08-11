from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .services.projects import get_projects, get_project


def projects(request: HttpRequest) -> HttpResponse:
    projects = get_projects()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context=context)

def project(request: HttpRequest, pk) -> HttpResponse:
    project = get_project(pk)
    tags = project.tags.all()
    context = {
        'project': project,
        'tags': tags,
    }
    return render(request, 'projects/single-project.html', context=context)