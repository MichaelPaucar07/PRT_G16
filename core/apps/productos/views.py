from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Vista para crear un nuevo producto
def crear_producto(request):
    # Si la solicitud es de tipo POST, se está enviando el formulario con datos
    if request.method == "POST":
        # Se instancia el formulario con los datos recibidos y posibles archivos (como imágenes)
        form = ProductoForm(request.POST, request.FILES)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda el nuevo producto en la base de datos
            form.save()
            # Redirige al usuario al listado de productos después de crear uno nuevo
            return redirect("listar_producto")
    else:
        # Si la solicitud es de tipo GET, se crea un formulario vacío para ser llenado
        form = ProductoForm()
    # Renderiza la plantilla del formulario de creación, pasando el formulario al contexto
    return render(request, "crear_producto.html", {"form": form})


# Vista para listar todos los productos registrados
def listar_producto(request):
    # Consulta todos los productos existentes en la base de datos
    productos = Producto.objects.all()
    # Renderiza la plantilla con la lista de productos
    return render(request, "listar_producto.html", {"productos": productos})


# Vista para actualizar un producto existente
def actualizar_producto(request, pk):
    # Obtiene el producto correspondiente al ID (pk) recibido como parámetro
    producto = Producto.objects.get(pk=pk)

    # Si se envía el formulario (POST), se procesan los nuevos datos
    if request.method == "POST":
        # Se instancia el formulario con los nuevos datos y el objeto existente (para actualizar)
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda los cambios en la base de datos
            form.save()
            # Redirige al listado de productos
            return redirect("listar_producto")
    else:
        # Si la solicitud es GET, se crea un formulario con los datos actuales del producto
        form = ProductoForm(instance=producto)

    # Renderiza la plantilla del formulario de actualización
    return render(request, "actualizar_producto.html", {"form": form})


# Vista para eliminar un producto
def eliminar_producto(request, pk):
    # Obtiene el producto correspondiente al ID (pk) recibido como parámetro
    producto = Producto.objects.get(pk=pk)

    # Si la solicitud es POST, se procede con la eliminación del registro
    if request.method == "POST":
        # Elimina el producto de la base de datos
        producto.delete()
        # Redirige al listado de productos tras la eliminación
        return redirect("listar_producto")
        # Si aún no se confirma la eliminación, se muestra una página de confirmación
    return render(request, "eliminar_producto.html", {"producto": producto})
