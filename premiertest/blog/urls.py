from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('Inscription/', views.inscription),
    path('Connexion/', views.connexion),
    path('Deconnexion/', views.deconnexion, name="deconnexion"),
    path('article/<int:id_article>', views.lire, name='lire'),
    path('nouvel_article/', views.new_article),
    path('article_modif/<int:id_article>', views.article_modif, name='modif'),
]
