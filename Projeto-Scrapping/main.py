import requests
from bs4 import BeautifulSoup
import json


def get_all_links(url):
    """
    function
    """
    try:
        req = requests.get(url, verify=False)
        site = BeautifulSoup(req.text, "html.parser")
        all_links = set()

        for link in site.find_all('a'):
            href = link.get('href')
            if isinstance(href, str) and href.startswith('https://www.cnnbrasil.com.br/tecnologia'):
                if href == "https://www.cnnbrasil.com.br/tecnologia/":
                    continue
                else:
                    all_links.add(href)

        all_links_list = list(sorted(all_links))

        return all_links_list
    except Exception as e:
        return print(f"Error when trying to reach site: {e}")


def get_all_content(urls):
    """
    function to get all data from pages previously found
    """
    try:
        all_data = dict()
        for url in urls:
            req = requests.get(url, verify=False)
            site = BeautifulSoup(req.text, "html.parser")
            script_tags = site.find_all('script')

            for script in script_tags:
                if 'articleBody' in script.text:
                    json_data = json.loads(script.text)
                    articleBody = json_data.get('articleBody')
                    headline = json_data.get('headline')
                    mainEntity = json_data.get('mainEntityOfPage')
                    description = json_data.get('description')
                    valores = {'articleBody': articleBody,
                               'headline': headline,
                               'description': description}
                    data = {mainEntity: valores}
                    all_data.update(data)

                    # print(f'CHAVE: {data.keys()}. \n VALOR: {data.values()}')
                    break
        return all_data

    except Exception as e:
        return print(f"Error when trying to reach site: {e}")


# running functions

links = get_all_links("https://www.cnnbrasil.com.br/")
content = get_all_content(links)
print(content)
