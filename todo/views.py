from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView # default django login,logout forms
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import TodoItem, MeetingItem
from . import forms 
from . import models
from django.contrib.auth.models import User as user, Group


#For the chatroom, enter the command - docker run -p 6379:6379 -d redis:5 - to run a redis server using docker containers
def register(request):
    # use django's built in registration form and enter valid credentials to save the form details to the database
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login/')
    else:
        form = UserCreationForm()  
# render the template for thefront end for registering and pass the form details to the front end
    return render(request, 'register.html',{'form' : form})

@login_required #you can only access the app if you are logged in
def dashboard(request):
    # only if youre logged in you can access the dashboard
    if(request.user.is_authenticated):
        return render(request, 'dashboard.html')
    else:
        # youre redirected to the login page if youre not logged in
         return HttpResponseRedirect('login/')

def addTodo(request):
     #create and save a new todo item and redirect browser to /todo
    all_todo_items=TodoItem.objects.all()
    if request.method=="POST":
        form=forms.todo(request.POST)
        # saves data to the database only if its valid and redirects to the todo page
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:  
        # render the todo template and pass the todo item details to the front end
        return render(request,'todo.html',{'all_items':all_todo_items})
        
#delete a todo item
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
        # render the meeting template and pass the meeting item details to the front end
        return render(request,'meeting.html',{'all_items':all_meeting_items})
        
#delete a meeting item
def deleteMeeting(request,meeting_id):
    item_to_delete=MeetingItem.objects.get(id=meeting_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/meeting/')

#move to a chat index to enter room id
def index(request):
    return render(request, 'index.html', {})

#enter a chat room    
def room(request, room_name):
    # render the template for chat room and pass the room id details to the front end
    return render(request, 'room.html', {'room_name': room_name})

#chatup opens the public chat feature built using flask
def chatup(request):
    return render(request,'chat.html',{})