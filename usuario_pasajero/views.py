from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UsuarioPasajero
from .forms import UsuarioPasajeroForm

def index(request):
    return render(request, 'usuario_pasajero/index.html', { # CAMBIADO AQUÍ
        'usuarios': UsuarioPasajero.objects.all()
    })

def view_usuario(request, id):
    usuario = get_object_or_404(UsuarioPasajero, pk=id)
    return redirect('index')

def add(request):
    success = False
    if request.method == 'POST':
        form = UsuarioPasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = UsuarioPasajeroForm()
    else:
        form = UsuarioPasajeroForm()
    return render(request, 'usuario_pasajero/add.html', { # CAMBIADO AQUÍ
        'form': form,
        'success': success
    })

def edit(request, id):
    usuario = get_object_or_404(UsuarioPasajero, pk=id)
    success = False
    if request.method == 'POST':
        form = UsuarioPasajeroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = UsuarioPasajeroForm(instance=usuario)
    return render(request, 'usuario_pasajero/edit.html', { # CAMBIADO AQUÍ
        'form': form,
        'success': success
    })

def borrar(request, id):
    usuario = get_object_or_404(UsuarioPasajero, pk=id)
    if request.method == 'POST':
        usuario.delete()
        return HttpResponseRedirect(reverse('usuario_pasajero:index'))
    return render(request, 'usuario_pasajero/borrar.html', { # CAMBIADO AQUÍ (si decides usar una página de borrado dedicada)
        'usuario': usuario
    })