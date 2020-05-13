from django import forms
from . import models
from django.contrib.auth.models import User, Group
class todo(forms.ModelForm):
    class Meta:
        model=models.TodoItem
        fields = ('content','due_date')

class meeting(forms.ModelForm):
    class Meta:
        model=models.MeetingItem
        fields = ('reason','due_time')

# class team(forms.ModelForm):
#     class Meta:
#         models=models.Team
#         fields = ('groupname',)


