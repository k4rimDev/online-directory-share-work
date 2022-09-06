from typing import Any
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile, Skill


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

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user", )

        widgets = {
            'social_github': forms.TextInput(),
            'social_linkedin': forms.TextInput(),
            'social_twitter': forms.TextInput(),
            'social_youtube': forms.TextInput(),
            'social_website': forms.TextInput(),
        }
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"  
        exclude = ("owner", )
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SkillForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})