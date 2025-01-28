from accounts.models import User
from django.contrib.auth.hashers import check_password, make_password

class Authentication:
  
  def signin(self, email: str, password: str) -> User | bool:  # tipando variavel
    user = User.objects.filter(email=email).first() # pegando o usuário e colocando na variavel user

    if user and check_password(password, user.password):
      return user

    return False  # se falso retorna o bool  

  
  def signup(self, name: str, email: str, password: str) -> User | bool:
    if User.objects.filter(email=email).exists():   # se o email existir - retorna FALSE
      return False
    
    user = User.objects.create(
      name=name,
      email=email,
      password=make_password(password)    # salvando como hash no db
    )

    return user