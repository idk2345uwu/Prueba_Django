from django.shortcuts import render

from django.shortcuts import render
from pruebaapp.forms import Formproyecto

from pruebaapp.models import integrante


def index(request):
    return render(request, 'pruebaapp\index.html')

def listadointegrantes(request):
    integrantes = integrante.objects.all()
    data = {'integrantes': integrantes}
    return render(request, 'pruebaapp\integrantes.html', data)


def agregarintegrantes(request):
    form = Formproyecto()
    if request.method == 'POST' :
        form = Formproyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'pruebaapp\ponerintegrantes.html')



# Create your views here.
