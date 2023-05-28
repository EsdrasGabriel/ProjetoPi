from django.shortcuts import render
from .models import cadastro_usuario
# Create your views here.

def screenLogin(request):
    return render(request, 'usuarios/login.html')

def screenCadastro(request):
    return render(request, 'usuarios/cadastro.html')

def formCadastro(request):
    novo_usuario = cadastro_usuario()
    request.POST.get()