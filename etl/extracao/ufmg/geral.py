import os
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class Geral:
    
    @staticmethod
    def get_classificacao_geral():

        url = os.getenv('URL_CLASSIFICACAO_GERAL')
        scrapper = cloudscraper.create_scraper()
        try:
            response = scrapper.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching classificação geral: {e}")
            return None
    
        soup = BeautifulSoup(response.content, 'html.parser')
        tabela = soup.find('table', id = 'tabelaCL' )
        
        if not tabela:
            print("Tabela não encontrada")
            return None

        linhas = tabela.find_all('tr')
        
        dados_tabela = []
        for linha in linhas:
            colunas = linha.find_all(['th', 'td'])
            dados_linha = [coluna.get_text(strip=True) for coluna in colunas]
            dados_tabela.append(dados_linha)
            
        df = pd.DataFrame(dados_tabela)
        
        print("Extração concluida")
        return df
