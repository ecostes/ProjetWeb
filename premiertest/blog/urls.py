from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('contact/', views.nouveau_contact, name='contact'),
    path('Inscription/', views.inscription),
    path('Connexion/', views.connexion),
    path('Deconnexion/', views.deconnexion, name="connexion"),
]
