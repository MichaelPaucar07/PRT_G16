from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "nombre",
            "direccion",
            "mision",
            "vision",
            "año_fundacion",
            "RUC",
            "imagen",
        ]
