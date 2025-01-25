import socketio
from django.conf import settings

# Create a socket.io server

socket = socketio.Server(
  cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS
)