from etl.extracao.ufmg.geral import Geral
from etl.extracao.ufmg.ultimasDezRodadas import UltimasDezRodadas
from etl.extracao.ufmg.mandante import Mandante   
from etl.extracao.ufmg.returno import Returno 
from etl.extracao.ufmg.turno import Turno
from etl.extracao.ufmg.visitante import Visitante
from data.conexao import Conexao

if __name__ == "__main__":
    print("Testando conexão com o SQL Server...")
    if Conexao.testar_conexao():
        print("Conexão de teste bem-sucedida!")
    else:
        print("Falha na conexão de teste.")

