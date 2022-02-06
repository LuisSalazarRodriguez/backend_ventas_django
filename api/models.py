from django.db import models

from django.contrib.auth.models import User

class Linea(models.Model):
    linea_codigo = models.AutoField(primary_key=True)
    linea_nombre = models.CharField(max_length=100,verbose_name='nombre de linea')
    linea_estado = models.CharField(max_length=10,verbose_name='estado linea')
    
    def __str__(self):
        return self.linea_nombre
class Marca(models.Model):
    marca_codigo = models.AutoField(primary_key=True)
    marca_nombre = models.CharField(max_length=100,verbose_name='nombre de marca')
    marca_estado = models.CharField(max_length=10,verbose_name='estado marca')
    
    def __str__(self):
        return self.marca_nombre