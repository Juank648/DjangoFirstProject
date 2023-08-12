from django.db import models

# Create your models here.
class Temas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class Webs(models.Model):
    tema = models.ForeignKey(Temas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, unique=True)
    ruta = models.URLField(unique=True)