from django.shortcuts import render
from django.http import HttpResponse
from .models import cadastro_usuario

# Create your views here.

def screenLogin(request):
    return render(request, 'usuarios/login.html')

def screenCadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        connection = cadastro_usuario()
        cursor = connection

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')

        usuario = cadastro_usuario.objects.filter(cpf=cpf).first()

        if usuario:
            return HttpResponse('Já existe uma conta cadastrada com esse cpf.')
        
        usuario = cadastro_usuario(nome=nome, email=email, senha=senha, cpf=cpf, endereco=endereco)
        usuario.save()

        connection.close()
        cursor.close()

        return HttpResponse('Cadastro realizado com sucesso')
    

    
