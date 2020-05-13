from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.TodoItem)
admin.site.register(models.MeetingItem)
admin.site.register(models.Message)
# admin.site.register(models.Team)
