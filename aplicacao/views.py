import json
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from aplicacao.models import Autor, Rede, Artigo
from aplicacao.plotly import Gerar_Grafico
from aplicacao.serializer import AutorSerializer, ArtigoSerializer, RedeSerializer
from aplicacao.make_graph import Make_Graph
import zipfile
from io import BytesIO
import os
from conectaif import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

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

        # Salvar cada item do contexto na sessão
        for key, value in contexto.items():
            request.session[key] = value

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

def render_pdf_view(request):

    Gerar_Grafico.gerar_donut("Media Trans", float(request.session.get('mediatrans', '0')), "transmedia")
    Gerar_Grafico.gerar_donut("Reciprocidade", float(request.session.get('reciprocidade', '0')), "reciprocidade")
    Gerar_Grafico.gerar_donut("Assortatividade", float(request.session.get('assortatividade', '0')), "assortatividade")
    
    contexto = {
        "arestas": request.session.get('arestas', '0'),
        "vertices": request.session.get('vertices', '0'),
        "reciprocidade": request.session.get('reciprocidade', '0'),
        "assortatividade": request.session.get('assortatividade', '0'),
        "mediatrans": request.session.get('mediatrans', '0'),
        "imagem" : request.session.get('imagem', ''),
        "comunidade": request.session.get('comunidade', ''),
        "centralidade": request.session.get('centralidade', ''),
        "grau_max": grau_max(),
        "numero_comunidades": num_comunidades(request.session.get('comunidade', '')),
        "url_site": settings.SITE_URL
    }

    template_path = 'pdf_dados.html'
    context = contexto
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="saida_rede.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('Houve um problema ao gerar seu PDF <pre>' + html + '</pre>')
    return response

def grau_max():
    return '0'

def num_comunidades(comunidade):
    return '0'

def propriedades(request):
    return render(request, 'propriedades.html')