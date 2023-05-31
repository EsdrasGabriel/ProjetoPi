from django.shortcuts import render
from django.http import HttpResponse
from .models import cadastro_usuario


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
    return HttpResponse(render(request, 'usuarios/home.html'))