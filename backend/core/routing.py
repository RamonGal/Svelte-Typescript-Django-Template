from django.conf.urls import url
from consumers.example import ExampleConsumer

websocket_urlpatterns = [
    url(r'ws/example/(?P<room_name>\w+)/$', ExampleConsumer.as_asgi()),
]
