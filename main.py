from etl.extracao.classificacoes.geral import Geral
from etl.extracao.classificacoes.ultimasDezRodadas import UltimasDezRodadas
from etl.extracao.classificacoes.mandante import Mandante   
from etl.extracao.classificacoes.returno import Returno 
from etl.extracao.classificacoes.turno import Turno
from etl.extracao.classificacoes.visitante import Visitante
from data.conexao import Conexao

if __name__ == "__main__":
    print("Testando conexão com o SQL Server...")
    if Conexao.testar_conexao():
        print("Conexão de teste bem-sucedida!")
    else:
        print("Falha na conexão de teste.")

