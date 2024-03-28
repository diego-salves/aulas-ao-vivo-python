import requests
from bs4 import BeautifulSoup


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
    function
    """
    try:
        req = requests.get(urls, verify=False)
        site = BeautifulSoup(req.text, "html.parser")
        all_content = dict()

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


# news_page = list(sorted(all_links))
# # sorted(news_page)
# print(news_page)
#


# for page in news_page[1]:
#     req = requests.get(page, verify=False)
#     site = BeautifulSoup(req.text, "html.parser")

# running function
all_links = get_all_links("https://www.cnnbrasil.com.br/")

print(all_links)
