from scraping.classificacoes.geral import ClassificacaoGeral
from scraping.classificacoes.ultimasDezRodadas import UltimasDezRodadas

if __name__ == "__main__":
    print("Iniciando ETL")

    df_classificacao = ClassificacaoGeral.get_classificacao_geral()
    if df_classificacao is not None:
        print("\n--- Tabela de Classificação da Série B ---")
        print(df_classificacao.head())

    df_ultimas_dez = UltimasDezRodadas.get_classificacao_geral()
    if df_ultimas_dez is not None:
        print("\n--- Tabela de Classificação das Últimas 10 Rodadas da Série B ---")
        print(df_ultimas_dez.head())