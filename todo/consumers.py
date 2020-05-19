import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
#  use a synchronous web socket as it is usually preferred when making a chat app
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
             #async_to_sync convers the async library functions to sync functions
            #  add room id to the channel layer on the redis server
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group when you disconnect
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from websocket
    def receive(self, text_data):
        # load content from the json dump
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author=text_data_json['author']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            { #specify the message content, and author of the message
                'type': 'chat_message',
                # message content
                'message': message, 
                # message author
                'author' : author
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']
        # Send message to WebSocket by dumping the content into a json file for parsing later on
        self.send(text_data=json.dumps({
            'message': message,
            'author' : author
        }))