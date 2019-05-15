from django import forms
from .models import Article

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
        fields = ['titre', 'contenu']

    #auteur = forms.CharField(max_length=20)
    #titre = forms.CharField(max_length=100)
    #contenu = forms.CharField(widget=forms.Textarea)


class ModifArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu']

    titre = forms.CharField(max_length=100, help_text="coucou")
    contenu = forms.CharField(widget=forms.Textarea)#, help_text=article.contenu)