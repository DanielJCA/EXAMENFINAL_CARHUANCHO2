from django.db import models

# Create your models here.
class Pais(models.Model):
    idpais=models.CharField(primary_key=True, max_length=6)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=10)
    poblacion=models.CharField(max_length=10)
    estado=models.CharField(max_length=10)

class Editorial(models.Model):
    ideditorial=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=10)
    url=models.CharField(max_length=10)
    imagen=models.CharField(max_length=10)
    estado=models.CharField(max_length=10)
