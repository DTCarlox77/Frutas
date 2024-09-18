from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    biografia = models.TextField(default='')
    
    def __str__(self):
        return f'Usuario: {self.username}'
    
class Fruta(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(User, related_name='FrutaUsuario', on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f'La fruta {self.nombre} tiene un precio de {self.precio}.'
