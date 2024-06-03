from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Perfil(AbstractUser):
    imagen = models.ImageField(upload_to='perfil/%Y/%m/%d', null=True, default='perfil/iconuser.png')
    portada = models.ImageField(upload_to='portada/%Y/%m/%d', null=True, default='perfil/portadauser.jpg')
    nacimiento = models.DateField(null=True)