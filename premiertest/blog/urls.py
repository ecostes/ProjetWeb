from django.urls import path
from . import views

urlpatterns = [
    #Affiche la page d'accueil
    path('', views.accueil, name='accueil'),
    #Affiche l'article choisi
    path('article/<int:id_article>', views.lire, name='lire'),
    #Affiche la page d'écriture d'un nouvel article
    path('nouvel_article/', views.new_article),
]
