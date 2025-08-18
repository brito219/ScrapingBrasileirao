import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class Conexao:
    
    @staticmethod
    def conectar():
        
        try:
            conn_str = (
                f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
                f"SERVER={os.getenv('DB_SERVER')};"
                f"DATABASE={os.getenv('DB_NAME')};"
                f"UID={os.getenv('DB_UID')};"
                f"PWD={os.getenv('DB_PWD')};"
            )
            conn = pyodbc.connect(conn_str)
            print("Conexão estabelecida com sucesso")  
            return conn
        except pyodbc.Error as e:
            print(f"Erro de ODBC: {e}")
            return None
        except Exception as e:
            print(f"Erro ao estabelecer conexão: {e}")
            return None
    
    
    @staticmethod
    def fechar_conexao(conn):
        if conn:
            try:
                conn.close()
                print("Conexão fechada com sucesso")
            except Exception as e:
                print(f"Erro ao fechar conexão: {e}")

    @staticmethod
    def testar_conexao():
        conn = Conexao.conectar()
        if conn:
            Conexao.fechar_conexao(conn)
            print("Teste de conexão bem-sucedido")
        else:
            print("Teste de conexão falhou")