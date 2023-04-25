from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from aplicacao.models import Autor, Rede, Artigo
from aplicacao.serializer import AutorSerializer, ArtigoSerializer, RedeSerializer

def index(self):
    return render(None, 'index.html')

class AutoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os autores"""
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ArtigosViewSet(viewsets.ModelViewSet):
    """Exibe todos os artigos"""
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RedesViewSet(viewsets.ModelViewSet):
    """Exibe todas as redes criadas"""
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

def artigos_publicados(self):
    return render(None, 'artigos_publicados.html')