from django.db import models
from .models import Autor
# Create your models here.

class Artigo(models.Model):
    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.name

    nome_artigo = models.CharField(max_length=100)
    doi = models.TextField()
    # autores = models.ForeignKey(Autor, through="" on_delete=models.CASCADE)


class Autor(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name

    nome_autor = models.CharField(max_length=100)
    link_lattes = models.TextField()
