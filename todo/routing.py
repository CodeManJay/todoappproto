from django.urls import re_path

from . import consumers
# direct to the particular chat room URL of the room id entered
websocket_urlpatterns = [
    # url is chat room id specific
    # use the front end rendered when directed to this URL to the backend, written in the consumers.py file 
    re_path(r'^ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]