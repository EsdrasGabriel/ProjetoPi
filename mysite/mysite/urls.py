from django.urls import path
from myapp import views

urlpatterns = [
    path('login/', views.screenLogin, name='login'),
    path('login/cadastro/', views.screenCadastro, name='cadastro')
]
