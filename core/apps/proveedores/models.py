from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
    @property
    def bandera_url(self):
        mapa = {
            'Ecuador': 'ec',
            'Colombia': 'co',
            'Chile': 'cl',
            'Estados Unidos': 'us',
            'España': 'es',
            'Argentina': 'ar',
            'México': 'mx',
            'Perú': 'pe',
        }
        codigo = mapa.get(self.pais, 'unknown')
        return f"https://flagcdn.com/24x18/{codigo}.png"