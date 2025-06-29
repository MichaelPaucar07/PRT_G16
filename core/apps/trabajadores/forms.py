from django import forms
from .models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ["nombre", "apellido", "correo", "cedula", "codigo_empleado", "imagen"]
