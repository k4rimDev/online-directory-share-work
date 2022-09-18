from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from projects.services.projects import get_project
from projects.forms import ProjectForm, ReviewForm
from projects.utils import search_project, paginate_projects
from projects.models import Tag


def projects(request: HttpRequest) -> HttpResponse:
    search_query, projects = search_project(request)

    """ 
    First version of handelling paginator
    """
    # page = request.GET.get('page', 1)
    results = 6

    custom_range, projects = paginate_projects(request, projects, results)
    context = {
        'projects': projects, 
        'search_query': search_query, 
        # 'paginator': paginator, 
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context=context)

def project(request: HttpRequest, pk) -> HttpResponse:
    project = get_project(pk)
    tags = project.tags.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            
            # Update project votecount
            project.get_vote_count

            messages.success(request, "Your review was successfully submitted.")

            return redirect('project', pk = project.id)
    context = {
        'project': project,
        'tags': tags,
        'form': form,
    }
    return render(request, 'projects/single-project.html', context=context)


@login_required(login_url="login")
def create_project(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        new_tags = request.POST.get("newtags").replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect("account")
    
    context = {
        'form': form,
    }

    return render(request, 'projects/project-form.html', context=context)
 

@login_required(login_url="login")
def update_project(request: HttpRequest, pk: str) -> HttpResponse: 
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        new_tags = request.POST.get("newtags").replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect("account")
    
    context = {
        'form': form,
        'project': project,
    } 

    return render(request, 'projects/project-form.html', context=context)


@login_required(login_url="login") 
def delete_project(request: HttpRequest, pk: str) -> HttpResponse:
    profile = request.user.profile
    project = profile.project_set.get(id = pk)

    if request.method  == 'POST':
        project.delete()
        return redirect("account")

    context = {
        "object": project,
        "back_page": "projects",
    }
    return render(request, 'delete_template.html', context=context)
 