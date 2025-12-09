"""
URL configuration for pweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from.import views

urlpatterns = [
    
    #Rota para pagina Inicial Raiz
    path('', views.index, name="index"),
    
    #Pagina Sobre
    path('sobre/', views.sobre, name="sobre"),
    
    #Pagina para Contatos
    path("contato/", views.contato, name="contato"), 
    
    #Pagina de Ajuda
    path("ajuda/", views.ajuda, name="ajuda"),
    
    #Pagina para exibir item por id
    path("item/<int:id>/", views.exibir_item, name="exibir_item"),
    
    #Pagina de perfil de usuario
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    
    #Pagina para exibir dia da semana
    path('diasemana/<int:numero>/', views.diasemana, name='diasemana'),
    
    #Pagina de produtos
    path('produto/', views.produtos, name='produto'),
    
    

]