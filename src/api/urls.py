from django.urls import path
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.get_routes),
    path('projects/', views.get_projects_api),
    path('projects/<str:pk>/', views.get_project_api),
    path('projects/<str:pk>/vote/', views.post_project_vote),
] 