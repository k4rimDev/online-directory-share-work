from django.forms import ModelForm 
from django import forms

from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["vote_total", "vote_ratio"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), 
            'source_link': forms.TextInput(),
            'demo_link': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs) -> None:
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class' : 'input input--text',
            'placeholder': 'Enter title'
        })

        self.fields['description'].widget.attrs.update({
            'class' : 'input',
            'placeholder': 'Enter description'
        })

        self.fields['source_link'].widget.attrs.update({
            'class' : 'input input--text',
            'placeholder': 'Enter source link'
        })

        self.fields['demo_link'].widget.attrs.update({
            'class' : 'input input--text',
            'placeholder': 'Enter demo link'
        })
    