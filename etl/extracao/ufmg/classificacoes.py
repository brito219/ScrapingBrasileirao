import os
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class ClassificacaoUFMG:

    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.base_url = os.getenv("UFMG_BASE_URL", "https://www.mat.ufmg.br/futebol")

        self.urls_classificacao = {
            "geral": f"{self.base_url}/classificacao-geral-serie-b/",
            "ultimas_10_rodadas": f"{self.base_url}/classificacao-das-ultimas-10-rodadas-serie-b/",
            "mandante": f"{self.base_url}/classificacao-como-mandante-serie-b/",
            "visitante": f"{self.base_url}/classificacao-como-visitante-serie-b/",
            "turno": f"{self.base_url}/classificacao-do-turno-serie-b/",
            "returno": f"{self.base_url}/classificacao-do-returno-serie-b/",
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

    def extrair_classificacao_geral(self):

        return self._extrair_tabela_generica(self.urls_classificacao["geral"])

    def extrair_classificacao_ultimas_10_rodadas(self):

        return self._extrair_tabela_generica(
            self.urls_classificacao["ultimas_10_rodadas"]
        )

    def extrair_classificacao_mandante(self):

        return self._extrair_tabela_generica(self.urls_classificacao["mandante"])

    def extrair_classificacao_visitante(self):

        return self._extrair_tabela_generica(self.urls_classificacao["visitante"])

    def extrair_classificacao_turno(self):

        return self._extrair_tabela_generica(self.urls_classificacao["turno"])

    def extrair_classificacao_returno(self):

        return self._extrair_tabela_generica(self.urls_classificacao["returno"])

    def extrair_todas_classificacoes(self):

        classificacoes = {}

        for tipo, url in self.urls_classificacao.items():
            print(f"\n🔄 Extraindo classificação: {tipo.replace('_', ' ').title()}")
            df = self._extrair_tabela_generica(url)
            classificacoes[tipo] = df

        return classificacoes
