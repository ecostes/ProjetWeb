from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm


# Create your views here.

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
    if form.is_valid():
        print("Is Valid")
        article = Article()
        article.titre = form.cleaned_data["titre"]
        article.contenu = form.cleaned_data["contenu"]
        article.auteur = form.cleaned_data["auteur"]
        article.save()
        sauvegarde = True

    return render(request, 'blog/new_article.html', locals())

