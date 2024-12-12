import igraph
from .utils import Utils
import uuid
import leidenalg as la
from conectaif.settings import MEDIA_ROOT as media

class Make_Community():

    def __init__(self, grafo):
        self.grafo = grafo
        self.vindex = Utils.make_vindex(self.grafo.vcount())

    def gerador_comunidaes_blondel(self):

        comunidades = igraph.Graph.community_multilevel(
            self.grafo.as_undirected(),
            weights=None
        )

        nome_da_imagem = f"{uuid.uuid4()}.svg"
        igraph.plot(comunidades, f"{media}/redes/comunidades/{nome_da_imagem}", bbox=(800, 350), edge_width=1, mark_groups=True, vertex_label_size=10, vertex_label=self.vindex, vertex_dist=200)

        return nome_da_imagem
    
    def gerador_comunidades_betweenness(self):

        comunidades = igraph.Graph.community_edge_betweenness(
            self.grafo.as_undirected(), 
            clusters=None,
            directed=False,
            weights=None
        ).as_clustering()

        nome_da_imagem = f"{uuid.uuid4()}.svg"
        igraph.plot(comunidades, f"{media}/redes/comunidades/{nome_da_imagem}", bbox=(800, 350), edge_width=1, mark_groups=True, vertex_label_size=10, vertex_label=self.vindex, vertex_dist=200)
        
        return nome_da_imagem
    
    def gerador_comunidades_fastgreedy(self):

        comunidades = igraph.Graph.community_fastgreedy(
            self.grafo.as_undirected(),
            weights=None
        ).as_clustering()

        nome_da_imagem = f"{uuid.uuid4()}.svg"
        igraph.plot(comunidades, f"{media}/redes/comunidades/{nome_da_imagem}", bbox=(800, 350), edge_width=1, mark_groups=True, vertex_label_size=10, vertex_label=self.vindex, vertex_dist=200)

        return nome_da_imagem
    
    def gerador_comunidades_infomap(self):

        comunidades = igraph.Graph.community_infomap(
            self.grafo.as_undirected(),
        )

        nome_da_imagem = f"{uuid.uuid4()}.svg"
        igraph.plot(comunidades, f"{media}/redes/comunidades/{nome_da_imagem}", bbox=(800, 350), edge_width=1, mark_groups=True, vertex_label_size=10, vertex_label=self.vindex, vertex_dist=200)
    
        return nome_da_imagem
    
    def gerador_comunidades_leiden(self):

        comunidades = igraph.Graph.community_leiden(
            graph=self.grafo.as_undirected(),
            objective_function='modularity',
        )

        nome_da_imagem = f"{uuid.uuid4()}.svg"
        igraph.plot(comunidades, f"{media}/redes/comunidades/{nome_da_imagem}", bbox=(800, 350), edge_width=1, mark_groups=True, vertex_label_size=10, vertex_label=self.vindex, vertex_dist=200)
    
        return nome_da_imagem