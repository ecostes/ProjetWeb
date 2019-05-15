from django.db import models
from django.utils import timezone



"""class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom"""


class Article(models.Model):
    titre = models.TextField(null=True)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        verbose_name = "article"
        ordering = ['-date']

    def __str__(self):
        return self.titre
