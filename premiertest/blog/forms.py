from django import forms


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

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
