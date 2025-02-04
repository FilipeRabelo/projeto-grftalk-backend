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

import uuid   # para gerar id's dinâmicos / aleatórios

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
  
#######################################################################################
  
# obter o usuário

class userView(APIView):
  def get(self, request):

    # obter o usuário / update last_access - salvar o ultimo acesso
    User.objects.filter(id=request.user.id).update(last_access=now)   # p usar o recurso de online (mostrar q esta online)

    user = UserSerializer(request.user).data

    return Response({
      'user': user
    })
  

  # upload - atualizando o usuário

  def put(sel, request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    avatar = request.FILES.get('avatar')    # qndo for para pegar arquivos

    # Initialize storage
    storage = FileSystemStorage(
      settings.MEDIA_ROOT / 'avatars',
      settings.MEDIA_URL + 'avatars'
    )

    if avatar:
      content_type = avatar.content_type
      extension = avatar.name.split('.')[-1]   # para gravar no BD qual é a extensão do arquivo

      # Validade avatar / para ver se esta no padrão correto - .png ou .jpeg
      if not content_type == 'image/png' and not content_type == 'image/jpeg':
        raise ValidationError('Somente arquivos do tipo .PNG ou .JPEG são suportados')

      # apos validação -> Save new avatar
      file = storage.save(f'{uuid.uuid4()}.{extension}', avatar)
      avatar = storage.url(file)

    # salvando os dados atualizados

    serializer = UserSerializer(request.user, data={  # enviando
      'name': name,
      'email': email,
      'avatar': avatar or request.user.avatar
    })

    if not serializer.is_valid(): # se nao for valido preciso levantar um erro
      # Deletar o arquivo 
      if avatar:
        storage.delete(avatar.split('/')[-1])