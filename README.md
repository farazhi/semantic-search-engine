# Semantic Search Engine (PT-BR)

## Etapas resumidas
Este projeto realiza o processamento das notícias através de 3 etapas:

**1. Limpeza:** As notícias brutas são tratadas.

**2. Embedding:** Vetorização usando o modelo BERTimbau.

**3. Busca:** Motor de busca semântica.


## Decisões
O projeto foi dividido em 4 arquivos diferentes, 3 contendo cada etapa e 1 contendo o programa principal.

**Etapa 1 (Limpeza):** Etapa focada em remover sujeiras das notícias. Foram removidas tags e entidades HTML, múltiplas quebras de linhas consecutivas, entre outros. O tratamento inicial dos textos foi realizado para garantir que o modelo de linguagem não processe lixo ou informações desnecessárias. Logo após, é retornado para a raiz do projeto um arquivo .json (noticias_limpas.json) com as notícias limpas e preparadas para a etapa 2.

**Etapa 2 (Embedding):** Foi utilizado o modelo alfaneo/bertimbau-base-portuguese-sts. A escolha se deu por ser um modelo treinado especificamente para o português do Brasil, capturando com precisão as nuances e o contexto da nossa língua, fazendo com que entenda melhor o linguajar econômico brasileiro, o que ajudará na etapa 3. Os vetores gerados são salvos (noticias_vetorizadas.json) junto com os dados para evitar reprocessamento desnecessário.

**Etapa 3 (Motor de busca semântica):** Implementada utilizando a biblioteca sentence-transformers e torch. A busca calcula a similaridade de cosseno entre o vetor da pergunta (query) e a base de vetores das notícias. São retornadas (printadas) no terminal para cada pergunta, três notícias que mais tiveram relação. A busca aceita qualquer consulta em linguagem natural enviada pelo usuário, realizando o cálculo dinâmico de similaridade semântica com a base de dados.


## Como rodar
**1. Pré-requisitos:**

Python instalado.

Git instalado na máquina (para conseguir clonar o repositório)


**2. Clonar o repositório:**

`git clone https://github.com/farazhi/semantic-search-engine.git`

`cd semantic-search-engine`


**3. Instalar Dependências:**
É fortemente recomendado criar e ativar um ambiente virtual antes de instalar as bibliotecas. No terminal da pasta do projeto, rode:

**No Windows:**

`python -m venv venv`

`venv\Scripts\activate`

**No Linux/macOS:**

`python3 -m venv venv`

`source venv/bin/activate`


Com o ambiente ativo, instale as dependências:
`pip install -r requirements.txt`


**4. Rodar o código:**

**No Windows:** `python main.py`

**No Linux/macOS:** `python3 main.py` 


O script vai processar os dados de forma sequencial e printar no terminal os resultados.


## Avaliação qualitativa
Nos testes de validação com consultas sobre temas econômicos, foi possível analisar os resultados e constatar a precisão do motor de busca:

* **Entendimento de Contexto:** O modelo entendeu o significado contextual das frases. Ao buscar por "mudanças na taxa de juros", o motor trouxe no topo notícias que mencionavam "Copom", "Selic" e "política monetária", mesmo que a palavra "juros" não estivesse no título.
* **Métricas de Confiança Coerentes:** Os percentuais de similaridade estavam bem acurados. O que era relevante ficou com uma porcentagem alta na frente, o que havia pouca ou nenhuma relação não esteve no ranking.
* **Ordenação Correta:** Em todos os testes, o primeiro lugar sempre foi a notícia mais forte e direta sobre o tema proposto, provando que o corte e a organização por relevância estão funcionando muito bem.

O projeto entrega uma solução eficiente para busca por contexto, podendo ser estendido para integração com bancos de dados vetoriais (ex: ChromaDB, Pinecone) ou pipelines de RAG
