from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_trabajador, name='listar_trabajador'),
    path('crear/', views.crear_trabajador, name='crear_trabajador'),
    path('editar/<int:pk>/', views.actualizar_trabajador, name='actualizar_trabajador'),
    path('eliminar/<int:pk>/', views.eliminar_trabajador, name='eliminar_trabajador'),
]
