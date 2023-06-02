from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
import logging


# Create your views here.

def screenLogin(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')

        auth = cadastro_usuario.objects.filter(email=email, senha=senha).all()

        if auth:
            return HttpResponse(render(request, 'usuarios/home.html'))
        else: 
            return HttpResponse('email ou senha inválidos')


def screenCadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')


        usuarioCpf = cadastro_usuario.objects.filter(cpf=cpf).first()
        usuarioEmail = cadastro_usuario.objects.filter(email=email).first()

        if usuarioCpf:
            return HttpResponse('Já existe uma conta cadastrada com esse cpf.')
        if usuarioEmail:
            return HttpResponse('Já existe uma conta cadastrada com esse email.')
        
        usuario = cadastro_usuario(nome=nome, email=email, senha=senha, cpf=cpf, endereco=endereco)
        usuario.save()

        return HttpResponse(render(request, 'usuarios/login.html'))
    

def screenHome(request):
      anuncios = {
            'anuncios': anuncios_tbl.objects.all()
        }
      
      return HttpResponse(render(request, 'usuarios/home.html', anuncios))


def screenPerfil(request):
    return HttpResponse(render(request, 'usuarios/perfil.html'))


def screenCriar(request):
    if request.method == "GET":
        return render(request, 'usuarios/anuncios/criar/criarAnuncio.html')
    else:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        requisitos = request.POST.get('requisitos')
        anuncio_tbl = anuncios_tbl(titulo=titulo, descricao=descricao, requisitos=requisitos)
        anuncio_tbl.save()

        return HttpResponse(render(request, 'usuarios/home.html',))


def screenEditar(request):
    return render(request, 'usuarios/anuncios/editar/editarAnuncio.html')


def screenEditarInfo(request):
    if request.method == "GET":
    
        id = request.GET.get('id')
        info = anuncios_tbl.objects.get(id_anuncio=id)
        infoo = {
            'id': info.id_anuncio,
            'titulo': info.titulo,
            'descricao': info.descricao,
            'requisitos': info.requisitos,
        }
        return HttpResponse(render(request, 'usuarios/anuncios/editar/editarInformacoes.html', infoo))
    
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        requisitos = request.POST.get('requisitos')
        id = int(request.POST.get('id'))

        
        infooo = anuncios_tbl.objects.filter(id_anuncio=id).first()
        infooo.titulo = titulo
        infooo.descricao = descricao
        infooo.requisitos = requisitos
        infooo.save()

        return HttpResponse(render(request, 'usuarios/perfil.html'))
    
    else:
        pass


def screenDeletar(request):
    return render(request, 'usuarios/anuncios/deletar/deletarAnuncio.html')

# def screenExConta(request):
#     return render(request, 'usuarios/anuncios/excluirConta/excluirConta.html')