from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Article, Contact
from .forms import ContactForm, NouveauContactForm, ArticleForm


# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)


def accueil(request):
    """ Afficher tous les articles de notre blog """

    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id):
    """ Afficher un article complet """
    pass # Le code de cette fonction est donné un peu plus loin.


def view_article(request, id_article):

    if int(id_article)>100:
        raise Http404

    return HttpResponse("<h2> Vous avez demandé l'article n°{0}".format(id_article))


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    list = Article.objects.all()
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1} \n Nom : {2} "
            .format(month, year, list[0].titre)

    )


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


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

