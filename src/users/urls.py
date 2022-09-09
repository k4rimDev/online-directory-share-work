from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("inbox/", views.inbox, name="inbox"),
    path("create-message/<str:pk>/", views.create_message, name="create-message"),
    path("message/<str:pk>/", views.view_message, name="message"),
    path("logout/", views.logout_user, name="logout"),
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>", views.user_profile, name="user-profile"),
    path("account/", views.user_accout, name="account"),
    path("edit-account/", views.edit_account, name="edit-account"),
    path("create-skill/", views.create_skill, name="create-skill"),
    path("update-skill/<str:pk>/", views.update_skill, name="update-skill"),
    path("delete-skill/<str:pk>", views.delete_skill, name="delete-skill"),
]