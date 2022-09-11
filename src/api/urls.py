from django.urls import path
from api import views

urlpatterns = [
    path('', views.get_routes),
    path('projects/', views.get_projects_api),
    path('projects/<str:pk>/', views.get_project_api),
] 