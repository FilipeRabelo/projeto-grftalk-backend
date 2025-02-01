from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.timezone import now

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from accounts.models import User

from core.utils.exceptions import ValidationError

# fazendo login

class SignInView(APIView, Authentication):
  permission_classes = [AllowAny]

  def post(self, request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    signin = self.signin(email, password)

    if not signin:
      raise AuthenticationFailed
    
    user = UserSerializer(signin).data
    access_token = RefreshToken.for_user(signin).access_token

    return Response({
      'user': user,
      'access_token': str(access_token)
    })
  

# criando conta e fazendo login  

class SignUpView(APIView, Authentication):
  permission_classes = [AllowAny]

  def post(self, request):
    name = request.data.get('name')
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    if not name or not email or not password:
      raise AuthenticationFailed

    signup = self.signup(name, email, password)

    if not signup:
      raise AuthenticationFailed
    
    user = UserSerializer(signup).data
    access_token = RefreshToken.for_user(signup).access_token

    return Response({
      'user': user,
      'access_token': str(access_token)
    })