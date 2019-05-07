from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('Inscription/', views.inscription),
    path('Connexion/', views.connexion),
    #path('Deconnexion/', views.deconnexion, name="connexion"),
    #Affiche l'article choisi
    path('article/<int:id_article>', views.lire, name='lire'),
    #Affiche la page d'ecriture d'un nouvel article
    path('nouvel_article/', views.new_article),
]
