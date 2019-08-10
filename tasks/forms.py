from django import forms
from .models import Project, Task, PRIORITY


class TaskForm(forms.Form):
    text = forms.CharField(max_length=255)
    end_time = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S'])
    project = forms.CharField(max_length=255)
    priority = forms.CharField(max_length=255)

    class Meta:
        model = Task
        fields = ('text', 'end_time', 'state', 'project', 'priority')