from django.shortcuts import get_object_or_404, render, redirect
from .models import Trabajador
from .forms import TrabajadorForm

# Vista para crear un nuevo trabajador
def crear_trabajador(request):
    # Si la solicitud es de tipo POST, se están enviando datos mediante el formulario
    if request.method == "POST":
        # Se instancia el formulario con los datos del request, incluyendo archivos (como imágenes o documentos)
        form = TrabajadorForm(request.POST, request.FILES)
        # Validación del formulario
        if form.is_valid():
            # Guarda el nuevo registro en la base de datos
            form.save()
            # Redirige al listado de trabajadores una vez guardado
            return redirect("listar_trabajador")
    else:
        # Si la solicitud es GET, se crea un formulario vacío para completar
        form = TrabajadorForm()

    # Renderiza la plantilla del formulario de creación de trabajador
    return render(request, "crear_trabajador.html", {"form": form})


# Vista para listar todos los trabajadores registrados
def listar_trabajador(request):
    # Recupera todos los objetos del modelo Trabajador
    trabajadores = Trabajador.objects.all()
    # Renderiza la plantilla con la lista de trabajadores
    return render(
        request, "listar_trabajador.html", {"trabajadores": trabajadores}
    )


# Vista para actualizar los datos de un trabajador existente
def actualizar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == "POST":
        form = TrabajadorForm(request.POST, request.FILES, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajador')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'editar_trabajador.html', {'form': form, 'trabajador': trabajador})



# Vista para eliminar un trabajador
def eliminar_trabajador(request, pk):
    # Recupera el trabajador a eliminar mediante su clave primaria
    trabajador = Trabajador.objects.get(pk=pk)

    # Si se confirma la eliminación mediante POST
    if request.method == "POST":
        # Se elimina el trabajador de la base de datos
        trabajador.delete()
        # Redirige al listado de trabajadores tras la eliminación
        return redirect("listar_trabajador")

    # Si la solicitud es GET, muestra una plantilla de confirmación
    return render(
        request, "eliminar_trabajador.html", {"trabajador": trabajador}
    )
