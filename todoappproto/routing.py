from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import todo.routing

# only for chat rooms feature
# reach the routing.py file in the app folder (todoappproto/todo/) 
# make it follow the url that specifies which page to move to depending on the room id and execute the functions in it

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            todo.routing.websocket_urlpatterns
        )
    ),
})