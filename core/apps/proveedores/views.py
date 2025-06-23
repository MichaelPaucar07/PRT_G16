from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm

# Vista para crear un nuevo proveedor
def crear_proveedor(request):
    # Si el método de la solicitud es POST, se están enviando datos desde el formulario
    if request.method == "POST":
        # Se instancia el formulario con los datos recibidos
        form = ProveedorForm(request.POST)
        # Se valida que los datos ingresados sean correctos
        if form.is_valid():
            # Si el formulario es válido, se guarda el nuevo proveedor en la base de datos
            form.save()
            # Redirige al usuario al listado de proveedores una vez guardado
            return redirect("listar_proveedor")
    else:
        # Si el método es GET, se genera un formulario vacío para mostrar en pantalla
        form = ProveedorForm()
    # Renderiza la plantilla de creación, enviando el formulario como contexto
    return render(request, "crear_proveedor.html", {"form": form})


# Vista para listar todos los proveedores
def listar_proveedor(request):
    # Consulta todos los registros existentes del modelo Proveedor
    proveedores = Proveedor.objects.all()
    # Renderiza la plantilla con la lista de proveedores
    return render(
        request, "listar_proveedor.html", {"proveedores": proveedores}
    )


# Vista para actualizar la información de un proveedor existente
def actualizar_proveedor(request, pk):
    # Obtiene el proveedor a actualizar, usando su clave primaria (pk)
    proveedor = Proveedor.objects.get(pk=pk)

    # Si el método es POST, se están enviando los datos modificados
    if request.method == "POST":
        # Se instancia el formulario con los datos enviados y se vincula al proveedor existente
        form = ProveedorForm(request.POST, instance=proveedor)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda los cambios realizados sobre el proveedor
            form.save()
            # Redirige al listado de proveedores tras actualizar
            return redirect("listar_proveedor")
    else:
        # Si la solicitud es GET, se cargan los datos actuales en el formulario para editar
        form = ProveedorForm(instance=proveedor)

    # Renderiza la plantilla del formulario de actualización
    return render(request, "actualizar_proveedor.html", {"form": form})


# Vista para eliminar un proveedor
def eliminar_proveedor(request, pk):
    # Obtiene el proveedor que se desea eliminar mediante su clave primaria
    proveedor = Proveedor.objects.get(pk=pk)

    # Si la solicitud es POST, se confirma la eliminación
    if request.method == "POST":
        # Elimina el proveedor de la base de datos
        proveedor.delete()
        # Redirige al listado de proveedores una vez eliminado
        return redirect("listar_proveedor")

    # Si la solicitud es GET, se muestra una pantalla de confirmación
    return render(
        request, "eliminar_proveedor.html", {"proveedor": proveedor}
    )
