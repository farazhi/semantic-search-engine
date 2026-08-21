from etapa1_limpeza import executar_limpeza
from etapa2_embedding import criar_embeddings
from etapa3_busca import executar_busca

def main():
    # Definindo os caminhos dos arquivos
    arquivo_bruto = "noticias_brutas.json"
    arquivo_limpo = "noticias_limpas.json"
    arquivo_vetorizado = "noticias_vetorizadas.json"

    # Executando o pipeline
    executar_limpeza(arquivo_bruto, arquivo_limpo)
    
    criar_embeddings(arquivo_limpo, arquivo_vetorizado)
    
    executar_busca(arquivo_vetorizado)

if __name__ == "__main__":
    main()
