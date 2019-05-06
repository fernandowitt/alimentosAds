from django.urls import path, include
from . import views

urlpatterns = [
    path('criarNovaAula/', views.criarNovaAula, name = 'criarNovaAula'),
    path('', views.aulasList, name = 'aulasList'),
    path('aula/<int:pk>', views.aula, name = 'aula')

]