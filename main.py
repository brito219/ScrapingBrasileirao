from etl.extracao.ufmg.classificacoes import ClassificacaoUFMG
from etl.extracao.ufmg.probabilidades_time import ProbabilidadesTimeUFMG
from data.conexao import Conexao


if __name__ == "__main__":
    print("Testando conexão com o SQL Server...")
    if Conexao.testar_conexao():
        print("Conexão de teste bem-sucedida!")
    else:
        print("Falha na conexão de teste.")

    # Classificações
    print("1. CLASSIFICAÇÕES")
    classificacao_extractor = ClassificacaoUFMG()
    todas_classificacoes = classificacao_extractor.extrair_todas_classificacoes()

    print("2. PROBABILIDADES")
    probabilidades_extractor = ProbabilidadesTimeUFMG()
    todas_probabilidades = probabilidades_extractor.extrair_todas_probabilidades_time()

    print(
        f"Classificações extraídas: {len([k for k, v in todas_classificacoes.items() if v is not None])}"
    )

    print(
        f"Probabilidades extraídas: {len([k for k, v in todas_probabilidades.items() if v is not None])}"
    )
