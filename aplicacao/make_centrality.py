import math
import uuid
import igraph

def definindo_layout(grafo, centralidade):
    layout = grafo.layout("kk")

    visual_style = {}
    visual_style["vertex_size"] = 40  # Ajustar o tamanho dos vértices
    visual_style["vertex_label"] = centralidade  # Exibir a centralidade de grau como rótulo
    visual_style["layout"] = layout
    visual_style["bbox"] = (800, 350)
    visual_style["margin"] = 20
    visual_style["vertex_dist"] = 200

    return visual_style

def gerar_grafico_grau(grafo):

    degree_centrality = grafo.degree()

    visual_style = definindo_layout(grafo, degree_centrality)

    nome_imagem = f"{uuid.uuid4()}.svg"
    igraph.plot(grafo, f"aplicacao/static/redes/centralidade/{nome_imagem}",  **visual_style)

    return nome_imagem

def gerar_grafico_betweenness(grafo):

    betweenness_centrality = grafo.betweenness()

    visual_style = definindo_layout(grafo, betweenness_centrality)

    nome_imagem = f"{uuid.uuid4()}.svg"
    igraph.plot(grafo, f"aplicacao/static/redes/centralidade/{nome_imagem}",  **visual_style)

    return nome_imagem

def gerar_grafico_closeness(grafo):

    closeness_centrality = grafo.closeness()
    closeness_centrality_rounded = [0 if math.isnan(n) else round(n, 2) for n in closeness_centrality]

    visual_style = definindo_layout(grafo, closeness_centrality_rounded)

    nome_imagem = f"{uuid.uuid4()}.svg"
    igraph.plot(grafo, f"aplicacao/static/redes/centralidade/{nome_imagem}",  **visual_style)

    return nome_imagem
