from datetime import datetime
import igraph
import time
from aplicacao.plotly import Gerar_Grafico
from .utils import Utils

class Make_Graph():

	def __init__(self, lista_arestas, direcionada):
		self.cria_arquivo(lista_arestas, direcionada)

	def cria_arquivo(self, lista_arestas, direcionada):
		today = datetime.now()
		ano = str(today.year)
		grafo = igraph.Graph()

		if today.month < 10:
			mes = "0" + str(today.month)
		else:
			mes = str(today.month)

		if today.day < 10:
			dia = "0" + str(today.day)
		else:
			dia = str(today.day)

		with open(f"media/redes/"+ ano + "/" + mes + "/" + dia + "/" + lista_arestas.name) as arquivo:
			grafo = grafo.Read_Edgelist(arquivo, directed=direcionada)
			arquivo.close()

		self.grafo = grafo

	def plot_graph(self):
		vindex = Utils.make_vindex(self.grafo.vcount())
		nome_da_imagem = str(time.time()) + ".svg"
		igraph.plot(self.grafo, "aplicacao/static/redes/" + nome_da_imagem,  bbox=(800, 350), vertex_label=vindex, margin=20, edge_arrow_size=0.3, vertex_color=(0, 0, 0), vertex_label_color=(255, 255, 255), vertex_dist=200, vertex_label_size=8)
		return nome_da_imagem

	def monta_contexto(self):
		arestas = self.grafo.ecount()
		vertices = self.grafo.vcount()
		reciprocidade = self.grafo.reciprocity()
		assortatividade = self.grafo.assortativity_degree()
		mediatrans = self.grafo.transitivity_avglocal_undirected()

		Gerar_Grafico.gerar_donut("Media Trans", mediatrans, "transmedia")
		Gerar_Grafico.gerar_donut("Reciprocidade", reciprocidade, "reciprocidade")
		Gerar_Grafico.gerar_donut("Assortatividade", assortatividade, "assortatividade")


		contexto = {
			"arestas": round(arestas,2),
			"vertices": round(vertices,2),
			"reciprocidade": round(reciprocidade,2),
			"assortatividade": round(assortatividade,2),
			"mediatrans": round(mediatrans,2),
			"imagem" : self.plot_graph()
		}

		return contexto