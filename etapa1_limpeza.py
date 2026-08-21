import pandas as pd

def executar_limpeza(entrada, saida):
    data = pd.read_json(entrada)

    # Dicionário com a maioria das sujeiras 
    sujeira = {
        '&aacute;': 'á', '&atilde;': 'ã', '&agrave;': 'à', '&eacute;': 'é',
        '&ecirc;': 'ê', '&Eacute;': 'É', '&Iacute;': 'Í', '&iacute;': 'í',
        '&oacute;': 'ó', '&otilde;': 'õ', '&uacute;': 'ú', '&ccedil;': 'ç',
        '&amp;': '&', '&nbsp;': ' ', '<p>': '', '</p>': '', '<em>': '',
        '</em>': '', '<br/>': '', '<strong>': '', '</strong>': ''
    }

    # Substituindo usando o dicionário
    for sujo, limpo in sujeira.items():
        data['texto'] = data['texto'].str.replace(sujo, limpo, regex=False)

    # Processando o texto, limpando as múltiplas quebras de linhas, metadados e timestamps
    textos_processados = []
    for texto in data['texto']:
        texto = str(texto)
        linhas = texto.split('\n')
        if len(linhas) <= 1:
            textos_processados.append(texto)
        else:
            linhas = linhas[1:]
            if '<a href=' in linhas[-1].lower():
                linhas = linhas[:-1]
            texto_limpo = " ".join(linhas)
            textos_processados.append(texto_limpo)
    data['texto'] = textos_processados

    # Lidando com espaços e conteúdo mínimo
    data['texto'] = data['texto'].str.split().str.join(' ')
    data = data[data['texto'].str.len() > 10]

    # Salvando os dados limpos
    dados_limpos = data.to_json(orient='records', indent=2, force_ascii=False)
    # Mantendo a fidelidade com as notícias brutas, colocando um espaço após o ":"
    dados_limpos = dados_limpos.replace('":', '": ')
    
    with open(saida, "w", encoding="utf-8") as dados:
        dados.write(dados_limpos)
    print('Etapa 1 Completa!')
