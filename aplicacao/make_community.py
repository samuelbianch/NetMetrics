import igraph
from .utils import Utils

class Make_Community():

    def __init__(self):
        pass

    def gerador_comunidaes(self, caminho_origem, caminho_destino):
        grafo = igraph.Graph()
        grafo = grafo.Read_Edgelist(f"{caminho_origem}.txt", directed=False)

        vindex = Utils.make_vindex(grafo.vcount())

        comunidades = igraph.Graph.community_multilevel(
            grafo, weights=None)

        igraph.plot(comunidades, f"./{caminho_destino}/comunidades.png", edge_width=1, bbox=(
            800, 350), mark_groups=True, vertex_label_size=10, vertex_label=vindex, vertex_dist=200)
