from django.forms import ModelForm 
from django import forms

from projects.models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["owner", "vote_total", "vote_ratio", "tags"]
        widgets = {
            # 'tags': forms.CheckboxSelectMultiple(), 
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

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value", "body"]

    labels = {
        'value': 'Please your vote',
        'body': 'Add a comment with your vote'        
    }

    def __init__(self, *args, **kwargs) -> None:
        super(ReviewForm, self).__init__(*args, **kwargs)
    
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class' : 'input',
            })