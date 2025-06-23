from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_proveedor, name='listar_proveedor'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
    path('editar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]