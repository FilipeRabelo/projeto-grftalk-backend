from rest_framework import serializers
from django.conf import settings
from accounts.models import User

# p receber dados e emitir uma resposta - modificar dados - criar novos dados

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'avatar', 'nome', 'email', 'last_access']

  def to_representation(self, instance):
    data = super().to_representation(instance)
    data['avatar'] = f"{settings.CURRENT_URL}{instance.avatar}"  # modificando o objeto

    return data