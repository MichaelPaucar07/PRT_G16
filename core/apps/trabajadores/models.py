from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    codigo_empleado = models.CharField(max_length=20, unique=True)
    imagen = models.ImageField(upload_to='trabajadores/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
