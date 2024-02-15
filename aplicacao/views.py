from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from aplicacao.models import Autor, Rede, Artigo
from aplicacao.serializer import AutorSerializer, ArtigoSerializer, RedeSerializer
from aplicacao.make_graph import Make_Graph

def index(request):
    if request.method == 'POST' and request.FILES['rede-txt']:
        rede = request.FILES['rede-txt']

        if request.POST['direcionada'] == 'on':
            direcionada = True
        else:
            direcionada = False

        objeto_rede = Rede.objects.create(arquivo=rede)
        objeto_rede.save()

        grafo = Make_Graph(rede, direcionada)
        
        contexto = grafo.monta_contexto()

        return render(request, 'index.html', contexto)
    return render(request, 'index.html')

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

def como_fazer(self):
    return render(None, 'como_fazer.html')