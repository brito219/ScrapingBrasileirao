import os
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class ProbabilidadesTimeUFMG:

    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.base_url = os.getenv("UFMG_BASE_URL", "https://www.mat.ufmg.br/futebol")

        self.urls_probabilidades = {
            "campeao": f"{self.base_url}/campeao-serie-b/",
            "primeira_divisao": f"{self.base_url}/classificacao-para-primeira-divisao/",
            "rebaixamento": f"{self.base_url}/rebaixamento-serie-b/",
        }

    def _extrair_tabela_generica(self, url, id_tabela="tabelaCL"):

        try:
            response = self.scraper.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"❌ Erro ao acessar {url}: {e}")
            return None

        try:
            soup = BeautifulSoup(response.content, "html.parser")
            tabela = soup.find("table", id=id_tabela)

            if not tabela:
                print(f"❌ Tabela com ID '{id_tabela}' não encontrada em {url}")
                return None

            linhas = tabela.find_all("tr")
            dados_tabela = []

            for linha in linhas:
                colunas = linha.find_all(["th", "td"])
                dados_linha = [coluna.get_text(strip=True) for coluna in colunas]
                if dados_linha:
                    dados_tabela.append(dados_linha)

            if not dados_tabela:
                print(f"❌ Nenhum dado encontrado na tabela de {url}")
                return None

            df = pd.DataFrame(dados_tabela)
            print(f"✅ Extração concluída! {len(df)} linhas extraídas de {url}")
            return df

        except Exception as e:
            print(f"❌ Erro ao processar dados de {url}: {e}")
            return None

    def extrair_probabilidades_campeao(self):

        return self._extrair_tabela_generica(self.urls_probabilidades["campeao"])

    def extrair_probabilidades_primeira_divisao(self):

        return self._extrair_tabela_generica(
            self.urls_probabilidades["primeira_divisao"]
        )

    def extrair_probabilidades_rebaixamento(self):

        return self._extrair_tabela_generica(self.urls_probabilidades["rebaixamento"])

    def extrair_todas_probabilidades_time(self):

        probabilidades = {}

        for tipo, url in self.urls_probabilidades.items():
            print(f"\n🔄 Extraindo probabilidades: {tipo.replace('_', ' ').title()}")
            df = self._extrair_tabela_generica(url)
            probabilidades[tipo] = df

        return probabilidades
