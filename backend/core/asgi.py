# The imports are not on top of the file,
# because to import some things durring build we need os.environ
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

import django
django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from .routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    ),
})
