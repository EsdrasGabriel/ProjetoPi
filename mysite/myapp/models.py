from django.db import models

class cadastro_usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50, blank=False, null=True)
    cpf = models.CharField(max_length=14)
    endereco= models.CharField(max_length=150)