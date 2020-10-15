from django.shortcuts import render, redirect
from core.models import Evento2

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    #evento = Evento2.objects.get(id=1)
    #response = {'evento':evento}
    #return render(request, 'agenda.html', response)
    usuario = request.user
    evento = Evento2.objects.all()
    #evento = Evento2.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
