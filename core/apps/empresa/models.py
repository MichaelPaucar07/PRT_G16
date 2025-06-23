from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    mision = models.TextField()
    vision = models.TextField()
    año_fundacion = models.IntegerField()
    RUC = models.CharField(max_length=13, unique=True)
    imagen = models.ImageField(upload_to='empresa/', null=True, blank=True)

    def __str__(self):
        return self.nombre
