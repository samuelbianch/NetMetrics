import json
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from aplicacao.models import Autor, Rede, Artigo
from aplicacao.serializer import AutorSerializer, ArtigoSerializer, RedeSerializer
from aplicacao.make_graph import Make_Graph
import zipfile
from io import BytesIO
import os
from conectaif import settings

def index(request):
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
    artigos = Artigo.objects.prefetch_related('autores')
    context = {
        'artigos': artigos
    }
    return render(None, 'artigos_publicados.html', context)

def como_fazer(self):
    return render(None, 'como_fazer.html')

def make_graph(request):
    if request.method == 'POST' and request.FILES['rede-txt']:
        rede = request.FILES['rede-txt']
        comunidade = request.POST.get('comunidade')
        centralidade = request.POST.get('centralidade')

        if request.POST.get('direcionada') == 'on':
            direcionada = True
        else:
            direcionada = False

        objeto_rede = Rede.objects.create(arquivo=rede)
        objeto_rede.save()

        grafo = Make_Graph(rede, direcionada, comunidade, centralidade)
        
        contexto = grafo.monta_contexto()

        return render(request, 'make_graph.html', contexto)
    return render(request, 'make_graph.html')

def sobre(self):
    return render(None, 'sobre.html')

def download_images(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            image_paths = data.get('image_paths', [])
        except json.JSONDecodeError:
            raise Http404("Invalid JSON data")

        if not image_paths:
            raise Http404("As imagens não foram carregadas corretamente.")
            
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for image_path in image_paths:
            zip_file.write(os.path.join(settings.STATICFILES_DIRS[0], image_path), os.path.basename(image_path))
    
    zip_buffer.seek(0)

    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=imagens.zip'
    return response