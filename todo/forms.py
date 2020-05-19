from django import forms
from . import models
from django.contrib.auth.models import User, Group

#specify the necessary parameters to enter in to the fields necessary to get a vaild form,
# so data can be stored via models

class todo(forms.ModelForm):
    class Meta:
        model=models.TodoItem
        fields = ('content','due_date') #parameters to enter in to the todo model

class meeting(forms.ModelForm):
    class Meta:
        model=models.MeetingItem
        fields = ('reason','due_time') #parameters to enter in to the meeting model


