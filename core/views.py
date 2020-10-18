from django.shortcuts import render, redirect
from core.models import Evento2
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario e/ou senha invalido!!!")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    #evento = Evento2.objects.get(id=1)
    #response = {'evento':evento}
    #return render(request, 'agenda.html', response)
    usuario = request.user
    evento = Evento2.objects.all()
    evento = Evento2.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento2.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

# Inclusão & Alteração
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        id_evento = request.POST.get('id_evento')
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        if id_evento:
            evento = Evento2.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo      = titulo
                evento.data_evento = data_evento
                evento.descricao   = descricao
                evento.save()
        else:
            Evento2.objects.create(titulo=titulo,
                                   data_evento=data_evento,
                                   descricao=descricao,
                                   usuario=usuario)
    return redirect('/')

#Deleção
@login_required(login_url='/login')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento2.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')
