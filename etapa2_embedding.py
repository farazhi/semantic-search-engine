import pandas as pd
from sentence_transformers import SentenceTransformer

def criar_embeddings(entrada, saida):
    # Lendo as notícias limpas
    data = pd.read_json(entrada)

    # Escolhendo o modelo
    modelo = SentenceTransformer('alfaneo/bertimbau-base-portuguese-sts')

    # Gerando os vetores númericos
    lista = data['texto'].tolist()
    vetores = modelo.encode(lista)
    data['vetor'] = vetores.tolist()

    # Exportando as notícias vetorizadas
    data.to_json(saida, orient='records', indent=2, force_ascii=False)
    print('Etapa 2 Completa!')
