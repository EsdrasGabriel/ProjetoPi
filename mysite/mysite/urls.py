from django.urls import path, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('', views.screenRedirect, name='redirect'),
    path('login/', views.screenLogin, name='login'),
    path('cadastro/', views.screenCadastro, name='cadastro'),
    path('home/', views.screenHome, name='home'),
    path('home/search/', views.screenSearchHome, name='search'),
    path('perfil/', views.screenPerfil, name='perfil'),
    path('perfil/CriarAnuncio/', views.screenCriar, name='CriarAnuncio'),
    path('perfil/EditarAnuncio/', views.screenEditar, name='EditarAnuncio'),
    path('perfil/EditarAnuncio/EditarInformacoes/', views.screenEditarInfo, name="EditarInformacoes"),
    path('perfil/DeletarAnuncio/', views.screenDeletar, name='DeletarAnuncio'),
    path('perfil/DeletarAnuncio/Confirmacao/', views.screenConfirmacao, name="Confirmacao"),
    path('ExcluirConta/', views.screenExConta, name='ExcluirConta'),
    path('Home/', views.screenHomeFree, name='HomeFree'),


    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]