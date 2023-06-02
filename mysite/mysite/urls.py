from django.urls import path, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.screenLogin, name='login'),
    path('cadastro/', views.screenCadastro, name='cadastro'),
    path('home/', views.screenHome, name='home'),
    path('perfil/', views.screenPerfil, name='perfil'),
    path('CriarAnuncio/', views.screenCriar, name='CriarAnuncio'),
    path('EditarAnuncio/', views.screenEditar, name='EditarAnuncio'),
    path('EditarInformacoes', views.screenEditarInfo, name="EditarInformacoes"),
    path('DeletarAnuncio/', views.screenDeletar, name='DeletarAnuncio'),
    path('confirmacao/', views.screenConfirmacao, name="Confirmacao"),
    path('ExcluirConta/', views.screenExConta, name='ExcluirConta'),

    path('accounts/', include('allauth.urls')),
]