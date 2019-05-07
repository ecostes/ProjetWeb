from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime
from .models import Article, Contact
from .forms import ContactForm, NouveauContactForm, InscriptionForm, ConnexionForm
from django.contrib.auth import *
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm


# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Girls can do it !! </h1>
        <p>Test</p>
    """)


def accueil(request):
    """ Afficher tous les articles de notre blog """

    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id_article):
    article = Article.objects.get(id = id_article)
    return render(request, 'blog/article.html', {'article': article})

#def view_article(request, id_article):

 #   return HttpResponse("<h2> Vous avez demandé l'article n°{0}".format(id_article))


def new_article(request):
    sauvegarde = False

    form = ArticleForm(request.POST or None)
    # Quoiqu'il arrive, on affiche la page du formulaire.
    if form.is_valid():
        print("Is Valid")
        article = Article()
        article.titre = form.cleaned_data["titre"]
        article.contenu = form.cleaned_data["contenu"]
        article.auteur = form.cleaned_data["auteur"]
        article.save()
        sauvegarde = True

    return render(request, 'blog/new_article.html', locals())


def inscription(request):
    sauvegarde = False
    form = InscriptionForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        mail=form.cleaned_data['mail']
        password=form.cleaned_data['password']
        user = User.objects.create_user(username, mail, password)
        user.save()
        sauvegarde=True

    return render(request, 'blog/Inscription.html', locals())

def connexion(request):
    form=ConnexionForm(request.POST or None)
    error=False
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
        else :
            error=True

    return render(request, "blog/Connexion.html", locals())

#def deconnexion(request):
 #   logout(request)
  #  return redirect("connexion")