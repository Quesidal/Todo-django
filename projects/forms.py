from django import forms
from .models import Project


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=255)
    color = forms.CharField(max_length=255)

    class Meta:
        model = Project
        fields = ('name', 'color')
