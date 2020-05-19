from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

# Create a todo model storing your todo items in a database
class TodoItem(models.Model):
    content=models.TextField()
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField() # a date

# Create a meeting model storing your meeting items in a database

class MeetingItem(models.Model):
    reason=models.TextField()           
    due_time = models.TimeField(default=timezone.now()) # a time

# Create a message model storing your messages in a database

class Message(models.Model):
    author=models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
# returns author
    def __str__(self):
        return self.author.username
#returns the last 10 messages upon reloading the chat rooms page
    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]


