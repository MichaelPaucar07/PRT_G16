from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_producto, name='listar_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]