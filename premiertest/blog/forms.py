from django import forms

class InscriptionForm(forms.Form):
    username=forms.CharField(max_length=100)
    mail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class ConnexionForm(forms.Form):
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

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
