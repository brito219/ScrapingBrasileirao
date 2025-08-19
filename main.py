from scraping.classificacoes.geral import Geral
from scraping.classificacoes.ultimasDezRodadas import UltimasDezRodadas
from scraping.classificacoes.mandante import Mandante   
from scraping.classificacoes.returno import Returno 
from scraping.classificacoes.turno import Turno
from scraping.classificacoes.visitante import Visitante
from db.conexao import Conexao

if __name__ == "__main__":
    print("Testando conexão com o SQL Server...")
    if Conexao.testar_conexao():
        print("Conexão de teste bem-sucedida!")
    else:
        print("Falha na conexão de teste.")

