toda vez que vc acessa um site
seu navegador faz uma requisicao pro servidor
o server responde com o codigo html
o navegador rendereiza a pagina

com clouscrapper

import cloudscraper

# Cria um "navegador" virtual
scraper = cloudscraper.create_scraper()

# Faz a requisição (como se fosse um navegador real)
response = scraper.get('https://www.mat.ufmg.br/futebol/classificacao-geral-serie-b/')

# Pega o HTML da resposta
html = response.text

ferramentas uteis legais-> control shift c pra selecionar

