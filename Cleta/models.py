from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

  user = models.OneToOneField(User,on_delete=models.CASCADE)
  rut = models.CharField(max_length=10,blank=True)
  comuna = models.CharField(max_length=100,blank=True)
  foto_perfil = models.ImageField(upload_to='media',blank=True)

def __str__(self):
  return self.user.username
# Create your models here.
