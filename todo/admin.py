from django.contrib import admin
from . import models
# Register your models here so you can manage them in the administration page.
admin.site.register(models.TodoItem)
admin.site.register(models.MeetingItem)
admin.site.register(models.Message)
