import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util


def executar_busca(caminho_dados):
    # Lendo as notícias vetorizadas
    data = pd.read_json(caminho_dados)

    # Carregando o modelo novamente para codificar as perguntas
    modelo = SentenceTransformer('alfaneo/bertimbau-base-portuguese-sts')

    # Setando as 3 queries pedidas para teste. É possível trocar as queries a qualquer momento aqui
    queries = [
        "mudanças na taxa de juros",
        "mercado de trabalho e desemprego",
        "inflação e preços ao consumidor"
    ]

    # Convertendo a lista de vetores do DataFrame de volta para tensores do PyTorch 
    base_vetores = torch.tensor(data['vetor'].tolist())
    vetores_queries = modelo.encode(queries)

    # Realizando a busca semântica, o parâmetro top_k=3 faz com que o motor traga apenas os 3 resultados mais relevantes
    resultados = util.semantic_search(vetores_queries, base_vetores, top_k=3)

    # Exibição para separar e destacar os resultados da busca
    print("\n" + "="*70)
    print("RESULTADOS DA BUSCA SEMÂNTICA")
    print("="*70)

    # Fazendo um loop sobre as perguntas e resultados
    for pergunta, resultado in zip(queries, resultados):
        print(f"\n>>> {pergunta}\n")
        # Extraindo as informações de cada notícia encontrada para exibir no terminal
        for pos, item in enumerate(resultado, 1):
            indice = item['corpus_id']
            # Convertendo a pontuação de similaridade para porcentagem com 1 casa decimal
            score = f"{100 * item['score']:.1f}%"
            titulo = data['titulo'].iloc[indice]
            texto = data['texto'].iloc[indice]
            
            print(f"  {pos}. [{score}] {titulo}")
            # Exibindo apenas os primeiros 250 caracteres do texto como prévia
            print(f"     {texto[:250]}...\n")
    print("\n" + "="*70)
    print('Etapa 3 Completa!')
