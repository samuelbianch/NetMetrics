from datetime import datetime
import igraph
import time

class Make_Graph():

	def __init__(self, lista_arestas, direcionada):
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

		with open("media/redes/"+ ano + mes + dia + "/" + lista_arestas.name) as arquivo:
			grafo = grafo.Read_Edgelist(arquivo, directed=direcionada)
			arquivo.close()

		self.grafo = grafo

	def plot_graph(self):

		i = 0
		vertices = self.grafo.vcount()
		vindex1=[""]*vertices

		self.arestas = self.grafo.ecount()
		self.vertices = self.grafo.vcount()
		self.reciprocidade = self.grafo.reciprocity()
		self.assortatividade = self.grafo.assortativity_degree()
		self.mediatrans = self.grafo.transitivity_avglocal_undirected()

		igraph.plot(self.grafo, "aplicacao/static/redes/" + str(time.time()) + ".svg")

	def monta_contexto(self):
		contexto = {
			"arestas": self.arestas,
			"vertices": self.vertices,
			"reciprocidade": self.reciprocidade,
			"assortatividade": self.assortatividade,
			"mediatrans": self.mediatrans,
		}

		return contexto