from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .services.projects import get_projects, get_project
from .forms import ProjectForm


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


def create_project(request: HttpRequest) -> HttpResponse:
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid( ):
            form.save()
            return redirect("projects")
    
    context = {
        'form': form,
    }

    return render(request, 'projects/project-form.html', context=context)


def update_project(request: HttpRequest, pk: str) -> HttpResponse: 
    project = get_project(pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid( ):
            form.save()
            return redirect("projects")
    
    context = {
        'form': form,
    }

    return render(request, 'projects/project-form.html', context=context)


def delete_project(request: HttpRequest, pk: str) -> HttpResponse:
    project = get_project(pk)

    if request.method == 'POST':
        project.delete()
        return redirect("projects")

    context = {
        "project": project
    }
    return render(request, 'projects/delete_project.html', context=context)