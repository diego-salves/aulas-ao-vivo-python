import requests
from bs4 import BeautifulSoup

url = "https://www.cnnbrasil.com.br/tecnologia/apple-anuncia-data-para-wwdc-conferencia-de-desenvolvedores-saiba-mais/"

req = requests.get(url, verify=False)
site = BeautifulSoup(req.text, "html.parser")

all_content = dict()

for link in site.find_all('script'):
    var = link.getText()
    for text in var:
        if text == "https://www.cnnbrasil.com.br/tecnologia/apple-anuncia-data-para":

    print(link.getText())
