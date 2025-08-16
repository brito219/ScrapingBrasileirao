como encontrar os elementos que quero com o bsoup

por tag,

# Encontra a primeira tabela

tabela = soup.find('table')

# Encontra todas as linhas

linhas = soup.find_all('tr')

por classe,

# Encontra elemento com classe específica

tabela = soup.find('table', class\_='leaguemanager')

por id,

# Encontra elemento com ID específico

elemento = soup.find('div', id='classificacao')


como descobrir a estrutura do html dos sites-> pressionar f12

### Como extrair com BeautifulSoup:
```python
# Encontra a tabela
tabela = soup.find('table', class_='leaguemanager') pega a tabela 

# Pega todas as linhas
linhas = tabela.find_all('tr') pega as linhas da tabela 

# Para cada linha, pega o texto de cada célula
for linha in linhas:
    colunas = linha.find_all('td')
    dados = [coluna.get_text(strip=True) for coluna in colunas]
    print(dados)  # ['1', 'GOIÁS', '41', '21', ...]
```