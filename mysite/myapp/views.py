from django.shortcuts import render
from .models import cadastro_usuario
# Create your views here.

def screenLogin(request):
    return render(request, 'usuarios/login.html')

def formCadastro(request):
    novo_usuario = cadastro_usuario()
    request.POST.get()

def screenCadastro(request):
    return render(request, 'usuarios/cadastro.html')
