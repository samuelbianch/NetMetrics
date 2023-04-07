from igraph import * 
#from cairo import *
import nltk
from nltk.metrics.spearman import *
import scipy.stats as stats


grafo = Graph()
grafo = grafo.Read_Edgelist('rede-cora\subelj_cora\\base.txt', directed=True)



i = 0
vertices = grafo.vcount()
vindex1=[""]*vertices
vindex2=[""]*vertices
vindex3=[""]*vertices
vindex4=[""]*vertices
vindex5=[""]*vertices
vindex6=[""]*vertices
vindex7=[""]*vertices


#arq = open('rede-cora\subelj_cora\saida.txt', 'w')

arestas = grafo.ecount()
vertices = grafo.vcount()
reciprocidade = grafo.reciprocity()
assortatividade = grafo.assortativity_degree()
mediatrans = grafo.transitivity_avglocal_undirected()

print("Vértices = ", vertices)
print("Arestas = ", arestas)

'''arq.write("Numero de arestas:")
arq.write(str(arestas))
arq.write("\nNumero de vertices:")
arq.write(str(vertices))
arq.write("\nReciprocidade:")
arq.write(str(reciprocidade))
arq.write("\nAssortatividade:")
arq.write(str(assortatividade))
arq.write("\nTransitividade Media:")
arq.write(str(mediatrans))'''

while i < vertices:
	vindex1[i] = i
	vindex2[i] = i
	vindex3[i] = i
	vindex4[i] = i
	vindex5[i] = i
	vindex6[i] = i
	vindex7[i] = i
	i = i+1

plot(grafo, "Rede-Cora.svg", bbox=(800, 700), margin=20, vertex_label=vindex1, edge_arrow_size=0.3, vertex_color=(255, 0, 0), vertex_label_color=(225, 225, 0), vertex_label_size=1, vertex_dist=200)

'''grau = grafo.degree()
grau, vindex1 = (list(x) for x in zip(*sorted(zip(grau, vindex1), reverse=True)))


pagerank = grafo.pagerank()
pagerank, vindex2 = (list(x) for x in zip(*sorted(zip(pagerank, vindex2), reverse=True)))

hub = grafo.hub_score()
hub, vindex3 = (list(x) for x in zip(*sorted(zip(hub, vindex3), reverse=True)))

authority = grafo.authority_score()
authority, vindex4 = (list(x) for x in zip(*sorted(zip(authority, vindex4), reverse=True)))

close = grafo.closeness()
close, vindex5 = (list(x) for x in zip(*sorted(zip(close, vindex5), reverse=True)))

bet = grafo.betweenness()
bet, vindex6 = (list(x) for x in zip(*sorted(zip(bet, vindex6), reverse=True)))

auto = grafo.evcent()
auto, vindex7 = (list(x) for x in zip(*sorted(zip(auto, vindex7), reverse=True)))

arq.write("\n\nGrau - Pagerank:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex2))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex2)
arq.write(str(tau))

arq.write("\n\nGrau - Hub:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex3))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex3)
arq.write(str(tau))

arq.write("\n\nGrau - Authority:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex4))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex4)
arq.write(str(tau))

arq.write("\n\nGrau - Closeness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex5))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex5)
arq.write(str(tau))

arq.write("\n\nGrau - Beetwiness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex6))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex6)
arq.write(str(tau))

arq.write("\n\nGrau - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex1),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex1, vindex7)
arq.write(str(tau))

arq.write("\n\nPagerank - Hub:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex2),ranks_from_sequence(vindex3))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex2, vindex3)
arq.write(str(tau))

arq.write("\n\nPagerank - Authority:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex2),ranks_from_sequence(vindex4))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex2, vindex4)
arq.write(str(tau))

arq.write("\n\nPagerank - Closeness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex2),ranks_from_sequence(vindex5))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex2, vindex5)
arq.write(str(tau))

arq.write("\n\nPagerank - Betweeness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex2),ranks_from_sequence(vindex6))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex2, vindex6)
arq.write(str(tau))

arq.write("\n\nPagerank - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex2),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex2, vindex7)
arq.write(str(tau))

arq.write("\n\nHub - Authority:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex3),ranks_from_sequence(vindex4))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex3, vindex4)
arq.write(str(tau))

arq.write("\n\nHub - Closeness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex3),ranks_from_sequence(vindex5))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex3, vindex5)
arq.write(str(tau))

arq.write("\n\nHub - Betwenness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex3),ranks_from_sequence(vindex6))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex3, vindex6)
arq.write(str(tau))

arq.write("\n\nHub - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex3),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex3, vindex7)
arq.write(str(tau))

arq.write("\n\nAuthority - Closeness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex4),ranks_from_sequence(vindex5))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex4, vindex5)
arq.write(str(tau))

arq.write("\n\nAuthority - Betwenness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex4),ranks_from_sequence(vindex6))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex4, vindex6)
arq.write(str(tau))

arq.write("\n\nAuthority - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex4),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex4, vindex7)
arq.write(str(tau))

arq.write("\n\nCloseness - Betwenness:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex5),ranks_from_sequence(vindex6))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex5, vindex6)
arq.write(str(tau))

arq.write("\n\nCloseness - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex5),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex5, vindex7)
arq.write(str(tau))

arq.write("\n\nBetwenness - Eigenvector:\n\n")
#print list(ranks_from_sequence(vindex1))
spearman = spearman_correlation(ranks_from_sequence(vindex6),ranks_from_sequence(vindex7))
arq.write(str(spearman))
arq.write("\n")
tau, p_value = stats.kendalltau(vindex6, vindex7)
arq.write(str(tau))

arq.close()'''
