from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm

# Vista para crear una nueva empresa
def crear_empresa(request):
    # Si el método de la solicitud es POST, significa que se envió el formulario
    if request.method == "POST":
        # Se llena el formulario con los datos recibidos, incluidos archivos (como imágenes o documentos)
        form = EmpresaForm(request.POST, request.FILES)
        # Validación del formulario
        if form.is_valid():
            # Si es válido, guarda la nueva empresa en la base de datos
            form.save()
            # Redirecciona a la vista de listado de empresas después de guardar
            return redirect("empresa:listar_empresa")
    else:
        # Si la solicitud es GET, se instancia un formulario vacío
        form = EmpresaForm()
    # Renderiza la plantilla para crear una empresa, pasando el formulario al contexto
    return render(request, "crear_empresa.html", {"form": form})


# Vista para listar todas las empresas registradas
def listar_empresa(request):
    # Obtiene todos los objetos del modelo Empresa desde la base de datos
    empresas = Empresa.objects.all()
    # Renderiza la plantilla de listado, pasando la lista de empresas al contexto
    return render(request, "empresa/listar_empresa.html", {"empresas": empresas})


# Vista para actualizar una empresa existente
def actualizar_empresa(request, pk):
    # Recupera la empresa específica a través de su clave primaria (pk)
    empresa = Empresa.objects.get(pk=pk)

    # Si el método es POST, se está enviando el formulario con cambios
    if request.method == "POST":
        # Se instancia el formulario con los nuevos datos y la instancia existente
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda los cambios realizados
            form.save()
            # Redirige nuevamente al listado de empresas
            return redirect("empresa:listar_empresa")
    else:
        # Si la solicitud es GET, se carga el formulario con los datos actuales de la empresa
        form = EmpresaForm(instance=empresa)

    # Renderiza la plantilla de actualización, pasando el formulario prellenado al contexto
    return render(request, "empresa/actualizar_empresa.html", {"form": form})


# Vista para eliminar una empresa
def eliminar_empresa(request, pk):
    # Recupera la empresa a eliminar mediante su clave primaria
    empresa = Empresa.objects.get(pk=pk)

    # Si se confirma la eliminación mediante POST, se procede a eliminar
    if request.method == "POST":
        empresa.delete()
        # Redirige al listado de empresas una vez eliminada
        return redirect("empresa:listar_empresa")
    # Si aún no se ha confirmado, muestra una página de confirmación
    return render(request, "empresa/eliminar_empresa.html", {"empresa": empresa})


def vista_nosotros(request):
    empresa = Empresa.objects.first()
    form = EmpresaForm(instance=empresa if empresa else None)

    if request.method == "POST":
        form = EmpresaForm(request.POST, request.FILES, instance=empresa if empresa else None)
        if form.is_valid():
            form.save()
            return redirect("empresa:nosotros")

    template = "nosotros.html" if empresa else "sin_empresa.html"
    return render(request, template, {
        "empresa": empresa,
        "form": form  # <-- esto es lo más importante
    })
