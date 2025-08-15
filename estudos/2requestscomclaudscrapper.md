# pip3 install cloudscraper beautifulsoup4
from bs4 import BeautifulSoup
import cloudscraper

# create a cloudscraper instance
scraper = cloudscraper.create_scraper( ; sempre tem que criar o scrapper, especificar o browser, se é web ou etc é opcional
    browser={
        "browser": "chrome",
        "platform": "windows",
    },
)

# specify the target URL
url = "https://opensea.io/rankings"  ; normalmente vou colocar no .env os urls, deixa mais limpo o codigo

# request the target website
response = scraper.get(url) ; isso aqui é da biblioteca requests, vou estudar e colocar num repo separado -> estudos requests

# get the response status code
print(f"The status code is {response.status_code}")

# parse the returned HTML
soup = BeautifulSoup(response.text, "html.parser")

# get the description element
page_description = soup.select_one(".font-semibold.text-display-md.leading-display-md")

# print the description text
print(page_description.text)