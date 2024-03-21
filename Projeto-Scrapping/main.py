import requests
from bs4 import BeautifulSoup

prefix = "https://www.cnnbrasil.com.br/"

req = requests.get(prefix, verify=False)
site = BeautifulSoup(req.text, "html.parser")
all_links = set()

for link in site.find_all('a'):
    href = link.get('href')
    if isinstance(href, str) and href.startswith('https://www.cnnbrasil.com.br/tecnologia'):
        all_links.add(href)

# print(all_links)
