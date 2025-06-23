from django.urls import path
from . import views

app_name = 'empresa'

# apps/empresa/urls.py

from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('nosotros/', views.vista_nosotros, name='nosotros'),
    path('crear/', views.crear_empresa, name='crear_empresa'),
    path('actualizar/<int:pk>/', views.actualizar_empresa, name='actualizar_empresa'),
    path('eliminar/<int:pk>/', views.eliminar_empresa, name='eliminar_empresa'),
] 

