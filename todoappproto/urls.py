"""todoappproto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))           
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView,LogoutView
from todo.consumers import ChatConsumer

from todo.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('register/login/',LoginView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('dashboard/', dashboard),
    path('dashboard', dashboard),
    path('todo/',addTodo),
    path('addTodo',addTodo),
    path('dashboard/todo/',addTodo),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
    path('meeting/',addMeeting),
    path('addMeeting',addMeeting),
    path('dashboard/meeting/',addMeeting),
    path('deleteMeeting/<int:meeting_id>/',deleteMeeting),
    path('dashboard/index/',index),
    path('index/',index),
    path('<str:room_name>/',room),
    path('chat/<str:room_name>/',room),
    path('http://127.0.0.1:5000/',chatup)

    
]
