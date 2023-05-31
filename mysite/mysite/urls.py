from django.urls import path, include
from myapp import views

urlpatterns = [
    path('login/', views.screenLogin, name='login'),
    path('cadastro/', views.screenCadastro, name='cadastro'),
    path('home/', views.screenHome, name='home'),

    path('accounts/', include('allauth.urls')),
]
