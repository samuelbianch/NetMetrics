from django.contrib import admin
from .models import Artigo, Autor, Rede
# Register your models here.
class Artigos(admin.ModelAdmin):
    list_display = ('doi', 'nome_artigo')
    list_display_links = ('doi', 'nome_artigo')
    search_fields = ('autores', 'nome_artigo', )
    list_per_page = 10

class Autores(admin.ModelAdmin):
    list_display = ('nome_autor', 'link_lattes', 'data_nascimento')
    list_display_links = ('nome_autor', 'link_lattes')
    search_fields = ('nome_autor', 'cpf', )
    list_per_page = 20

class Redes(admin.ModelAdmin):
    list_display = ('criado_em', 'arquivo')
    list_display_links = None
    list_per_page = 20

admin.site.register(Artigo, Artigos)
admin.site.register(Autor, Autores)
admin.site.register(Rede, Redes)
