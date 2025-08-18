from scraping.classificacoes.geral import Geral
from scraping.classificacoes.ultimasDezRodadas import UltimasDezRodadas
from scraping.classificacoes.mandante import Mandante   
from scraping.classificacoes.returno import Returno 
from scraping.classificacoes.turno import Turno
from scraping.classificacoes.visitante import Visitante
from db.conexao import Conexao

if __name__ == "__main__":
    print("Iniciando ETL")

    df_classificacao = Geral.get_classificacao_geral()
    if df_classificacao is not None:
        print("\n--- Tabela de Classificação da Série B ---")
        print(df_classificacao.head())

    df_ultimas_dez = UltimasDezRodadas.get_classificacao_geral()
    if df_ultimas_dez is not None:
        print("\n--- Tabela de Classificação das Últimas 10 Rodadas da Série B ---")
        print(df_ultimas_dez.head())
        
    df_mandante = Mandante.get_classificacao_mandante()
    if df_mandante is not None:
        print("\n--- Tabela de Classificação dos Mandantes da Série B ---")
        print(df_mandante.head())

    df_returno = Returno.get_classificacao_returno()
    if df_returno is not None:
        print("\n--- Tabela de Classificação do Returno da Série B ---")
        print(df_returno.head())

    df_turno = Turno.get_classificacao_turno()
    if df_turno is not None:
        print("\n--- Tabela de Classificação do Turno da Série B ---")
        print(df_turno.head())

    df_visitante = Visitante.get_classificacao_visitante()
    if df_visitante is not None:
        print("\n--- Tabela de Classificação dos Visitantes da Série B ---")
        print(df_visitante.head())
        
    # No seu main.py (temporariamente para teste)

    print("Testando conexão com o SQL Server...")
    if Conexao.testar_conexao():
        print("Conexão de teste bem-sucedida!")
    else:
        print("Falha na conexão de teste.")

