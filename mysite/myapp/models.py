from django.db import models

class cadastro_usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=12)
    endereco = models.CharField(max_length=150)
    data_de_nascimento = models.DateField(auto_now=False, auto_now_add=False)