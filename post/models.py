from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publicaciones(models.Model):
    autor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='publicaciones_hechas')
    titulo=models.TextField()
    contenido=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)