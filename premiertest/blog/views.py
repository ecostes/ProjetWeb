from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime
from .models import Article
from .forms import InscriptionForm, ConnexionForm, ArticleForm, CommentaireForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id_article):
    article = Article.objects.get(id = id_article)
    return render(request, 'blog/article.html', {'article': article})


def new_article(request):
    if not request.user.is_authenticated:
        return redirect(connexion)
    else :
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
    if not request.user.is_authenticated:
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
    else:
        return redirect(accueil)


def deconnexion(request):
    logout(request)
    return redirect(connexion)


def article_modif(request, id_article):
    article = Article.objects.get(id = id_article)
    print("Avant modif: ",article.titre)
    if request.method == "POST":
        article.titre = request.POST["titre"]
        print(article.titre)
        article.contenu = request.POST["contenu"]
        article.save()

    return render(request, 'blog/article_modif.html', {'article': article})
