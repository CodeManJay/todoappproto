from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import TodoItem, MeetingItem
from . import forms 
from . import models
from django.contrib.auth.models import User as user, Group


# docker run -p 6379:6379 -d redis:5

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login/')
    else:
        form = UserCreationForm()  

    return render(request, 'register.html',{'form' : form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def addTodo(request):
     #create and save a new todo item and redirect browser to /todo
    all_todo_items=TodoItem.objects.all()
    if request.method=="POST":
        form=forms.todo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:
        return render(request,'todo.html',{'all_items':all_todo_items})
        

def deleteTodo(request,todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def addMeeting(request):
     #create and save a new meeting item and redirect browser to /meeting
    all_meeting_items=MeetingItem.objects.all()
    if request.method=="POST":
        form=forms.meeting(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/meeting/')
    else:
        return render(request,'meeting.html',{'all_items':all_meeting_items})
        
def deleteMeeting(request,meeting_id):
    item_to_delete=MeetingItem.objects.get(id=meeting_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/meeting/')

def index(request):
    return render(request, 'index.html', {})
    
def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})

def chatup(request):
    return HttpResponseRedirect('http://127.0.0.1:5000/')