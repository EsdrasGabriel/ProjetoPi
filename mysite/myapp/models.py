from django.db import models

class cadastro_usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50, blank=False, null=True)
    cpf = models.CharField(max_length=15, unique=True)
    endereco= models.CharField(max_length=150)

class anuncios_tbl(models.Model):
    id_anuncio = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    requisitos = models.TextField()