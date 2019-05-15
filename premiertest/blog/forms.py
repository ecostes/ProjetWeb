from django import forms
from .models import Article, Commentaire


class InscriptionForm(forms.Form):
    username=forms.CharField(max_length=100)
    mail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


class ConnexionForm(forms.Form):
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'auteur', 'contenu', 'date']

    auteur = forms.CharField(max_length=20)
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields=['pseudo', 'contenu','id_art', 'date']

    pseudo=forms.CharField(max_length=100)
    contenu=forms.CharField(widget=forms.Textarea)
    id_art=forms.IntegerField()

