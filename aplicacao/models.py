from django.db import models

class Autor(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome_autor

    nome_autor = models.CharField(max_length=100)
    link_lattes = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    resumo = models.TextField(blank=True)
    data_nascimento = models.DateTimeField()

class Artigo(models.Model):
    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.nome_artigo

    nome_artigo = models.CharField(max_length=200)
    doi = models.TextField(blank=True, help_text='Link para acesso ao trabalho')
    autores = models.ManyToManyField(Autor)
    resumo = models.TextField(blank=True)


class Rede(models.Model):
    class Meta:
        verbose_name = "Rede"
        verbose_name_plural = "Redes"

    def __str__(self):
        return self.criado_em.strftime('%Y-%m-%d %H:%M:%S')

    arquivo = models.FileField(upload_to='redes/%Y/%m/%d')
    criado_em = models.DateTimeField(auto_now_add=True)

