from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    pseudo=models.CharField(max_length=100)
    contenu=models.TextField(null=True)
    id_art=models.IntegerField()
    date = models.DateTimeField(default=timezone.now, verbose_name="Publié le")

    class Meta:
        verbose_name="Commentaire"
        ordering=['-date']

    def __str__(self):
        return self.titre