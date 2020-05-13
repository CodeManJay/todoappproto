from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.
class TodoItem(models.Model):
    content=models.TextField()
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField() # a date

class MeetingItem(models.Model):
    reason=models.TextField()           
    due_time = models.TimeField(default=timezone.now()) # a time

class Message(models.Model):
    author=models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]

User = get_user_model()

# class Team(models.Model):
#     groupname=models.TextField()
