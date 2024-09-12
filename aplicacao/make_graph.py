from datetime import datetime
import igraph
import time
from aplicacao.plotly import Gerar_Grafico
from .utils import Utils
from aplicacao import make_community, make_centrality

class Make_Graph():

	def __init__(self, lista_arestas, direcionada, comunidade, centralidade):
		self.cria_arquivo(lista_arestas, direcionada)
		self.comunidade_escolhida = comunidade
		self.centralidade_escolhida = centralidade

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
		layout = self.grafo.layout("kk")
		vindex = Utils.make_vindex(self.grafo.vcount())
		nome_da_imagem = str(time.time()) + ".svg"
		igraph.plot(
			self.grafo,
			"aplicacao/static/redes/" + nome_da_imagem, 
			bbox=(800, 350),
			vertex_label=vindex,
			margin=20,
			edge_arrow_size=0.8,
			vertex_color=(0, 0, 0),
			vertex_label_color=(255, 255, 255),
			vertex_dist=200,
			vertex_label_size=10,
			vertex_size=40,
			layout=layout
		)

		return nome_da_imagem
	
	def plot_comunidade_blondel(self):
		comunidade = make_community.Make_Community(grafo=self.grafo)
		nome_da_imagem = comunidade.gerador_comunidaes_blondel()
		return nome_da_imagem
	
	def plot_comunidade_betweenness(self):
		comunidade = make_community.Make_Community(grafo=self.grafo)
		nome_da_imagem = comunidade.gerador_comunidades_betweenness()
		return nome_da_imagem
		
	def plot_comunidade_infomap(self):
		comunidade = make_community.Make_Community(grafo=self.grafo)
		nome_da_imagem = comunidade.gerador_comunidades_infomap()
		return nome_da_imagem
	
	def plot_comunidade_fastgreedy(self):
		comunidade = make_community.Make_Community(grafo=self.grafo)
		nome_da_imagem = comunidade.gerador_comunidades_fastgreedy()
		return nome_da_imagem
	
	def plot_comunidade_leiden(self):
		comunidade = make_community.Make_Community(grafo=self.grafo)
		nome_da_imagem = comunidade.gerador_comunidades_leiden()
		return nome_da_imagem
	
	def plot_pontuacao_grau(self):
		return make_centrality.gerar_grafico_grau(grafo=self.grafo)
	
	def plot_pontuacao_betweenness(self):
		return make_centrality.gerar_grafico_betweenness(grafo=self.grafo)
	
	def plot_pontuacao_closeness(self):
		return make_centrality.gerar_grafico_closeness(grafo=self.grafo)

	def monta_contexto(self):
		arestas = self.grafo.ecount()
		vertices = self.grafo.vcount()
		reciprocidade = self.grafo.reciprocity()
		assortatividade = self.grafo.assortativity_degree()
		mediatrans = self.grafo.transitivity_avglocal_undirected()
		comunidade = ""
		centralidade = ""

		Gerar_Grafico.gerar_donut("Media Trans", mediatrans, "transmedia")
		Gerar_Grafico.gerar_donut("Reciprocidade", reciprocidade, "reciprocidade")
		Gerar_Grafico.gerar_donut("Assortatividade", assortatividade, "assortatividade")

		if self.comunidade_escolhida == '0':
			comunidade = self.plot_comunidade_betweenness()
		elif self.comunidade_escolhida == '1':
			comunidade = self.plot_comunidade_blondel()
		elif self.comunidade_escolhida == '2':
			comunidade = self.plot_comunidade_infomap()
		elif self.comunidade_escolhida == '3':
			comunidade = self.plot_comunidade_fastgreedy()
		elif self.comunidade_escolhida == '4':
			comunidade = self.plot_comunidade_leiden()

		if self.centralidade_escolhida == '0':
			centralidade = self.plot_pontuacao_grau()
		elif self.centralidade_escolhida == '1':
			centralidade = self.plot_pontuacao_betweenness()
		elif self.centralidade_escolhida == '2':
			centralidade = self.plot_pontuacao_closeness()

		contexto = {
			"arestas": round(arestas,2),
			"vertices": round(vertices,2),
			"reciprocidade": round(reciprocidade,2),
			"assortatividade": round(assortatividade,2),
			"mediatrans": round(mediatrans,2),
			"imagem" : self.plot_graph(),
			"comunidade": comunidade,
			"centralidade": centralidade
		}

		return contexto