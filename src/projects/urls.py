from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('single-project/<str:pk>', views.project, name='project')
]