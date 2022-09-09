from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from users.services.users import get_all_profiles, get_profile, get_top_skills_profile, get_other_skills_profile, get_user_projects, get_all_skills_profile, get_skill, get_filtered_profiles
from users.forms import CustomUserRegisterForm, ProfileForm, SkillForm
from users.utils import search_profiles


def register_user(request: HttpRequest) -> HttpResponse:
    page = "SignUp"
    form = CustomUserRegisterForm()
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "You have been registered...")
            login(request, user)
            return redirect("edit-account")
        messages.error(request, "An error has occured during registration")

    
    context = {
        "page": page,
        "form": form,
    }
    return render(request, "users/login_register.html", context=context)

def login_user(request: HttpRequest) -> HttpResponse:
    page = "Login"
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Username is not exists")
        
        user = authenticate(request, username = username, password = password)
 
        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is incorrect!")
    context = {
        "page": page,
    }
    return render(request, "users/login_register.html", context=context)

def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "User was logged out!")
    return redirect("login")

def profiles(request: HttpRequest) -> HttpResponse:
    search_query, profiles = search_profiles(request)

    context = { 
        "profiles" : profiles,
        "search_query" : search_query,
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
  
@login_required(login_url="login")
def user_accout(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    pk = profile.id
    context = { 
        "profile": profile,
        "skills": get_all_skills_profile(pk),
        "projects": get_user_projects(pk)
    }
    return render(request, "users/account.html", context=context)

@login_required(login_url="login")
def edit_account(request: HttpRequest) -> HttpResponse: 
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile )
        if form.is_valid():
            form.save()

            return redirect("account")
             
    context = {
        "form": form,
    }
    return render(request, "users/profile_form.html", context=context )

@login_required(login_url="login")
def create_skill(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill created successfully")
            return redirect('account')
    context = {
        "form": form,
        "page": "Create Skill", 
    }
    return render(request, "users/skill_form.html", context=context)

@login_required(login_url="login")
def update_skill(request: HttpRequest, pk) -> HttpResponse:
    skill = get_skill(pk)
    form = SkillForm(instance = skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully")
            return redirect('account')
    context = {
        "form": form,
        "page": "Update Skill",
    }
    return render(request, "users/skill_form.html", context=context)

@login_required(login_url="login")
def delete_skill(request: HttpRequest, pk) -> HttpResponse:
    profile = request.user.profile 
    skill = profile.skill_set.get(pk = pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill was deleted successfully")
        return redirect('account')
    context = {
        "object": skill,
        "back_page": "account",
    }
    return render(request, "delete_template.html", context=context)