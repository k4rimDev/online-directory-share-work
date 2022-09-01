from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomUserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

from .services.users import get_all_profiles, get_profile, get_top_skills_profile, get_other_skills_profile, get_user_projects


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
            return redirect("profiles")
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
