import pandas as pd

class Make_Base():

    def __init__(self):
         pass
    
    def criador_de_base(caminho_planilha, nome_base, pagina_nome_planilha):
        # Ler a planilha de respostas
        planilha = pd.read_excel(f"{caminho_planilha}", sheet_name=pagina_nome_planilha)

        # Criar um dicionário para armazenar os amigos de cada pessoa
        amigos = {}
        nome_base = f"{nome_base}"

        # Iterar sobre as linhas da planilha
        for row in planilha.iterrows():
            aluno = row["Alunos"]
            amigos_selecionados = row["Amigos Selecionados"].split(
                ", ") if not pd.isna(row["Amigos Selecionados"]) else []

            amigos[aluno] = amigos_selecionados

        relacoes_amigos = []

        # Criar relações de amizade entre as pessoas
        for aluno, lista_amigos in amigos.items():
            numero_aluno = list(amigos.keys()).index(aluno)

            for amigo in lista_amigos:
                numero_amigo = list(amigos.keys()).index(amigo)
                if numero_aluno == numero_amigo:
                        print("O vertice ", numero_aluno, " ligou em si mesmo.")
                else:
                        relacoes_amigos.append((numero_aluno, numero_amigo))

        # Salvar as relações de amizade em um arquivo de texto
        with open(f"{nome_base}.txt", "w") as arquivo:
            for relacao in relacoes_amigos:

                arquivo.write(f"{relacao[0]} {relacao[1]}\n")

        print("Base de amigos criada com sucesso!")
