from cProfile import label
from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Full name",
            "email": "Email"
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})