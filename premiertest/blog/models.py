from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        verbose_name = "article"
        ordering = ['-date']

    def __str__(self):
        return self.titre
