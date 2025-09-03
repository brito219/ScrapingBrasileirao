from etl.extracao.ufmg.classificacoes import ClassificacaoUFMG
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

    print(f"Classificações extraídas: {len([k for k, v in todas_classificacoes.items() if v is not None])}")