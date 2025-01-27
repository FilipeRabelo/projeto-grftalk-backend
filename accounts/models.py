from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
  def create_superuser(self, email, password):
    user = self.model(
      email=self.normalize_email(email)
    )

    user.set_password(password)
    user.is_superuser = True
    user.save(using=self._db)

    return user
  

class User(AbstractBaseUser):     # abstraindo a base do usuário
  avatar = models.TextField(default="/media/avatars/default-avatar.png")
  name = models.CharField(max_length=80)
  email = models.EmailField(unique=True)
  is_superuser = models.BooleanField(default=False)
  last_access = models.DateTimeField(auto_now_add=True)

  objects = UserManager()

  USERNAME_FIELD = "email"

  # para verificar se tem permissão
  def has_perm (self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
  
  @property
  def is_staff(self):
    return self.is_superuser
  
  # nome da tabela
  class Meta:
    db_table = 'users'
