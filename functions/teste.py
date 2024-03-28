import requests
from bs4 import BeautifulSoup

url = "https://revhq.com/products/chainofstrength-theonethingthatstillholdstrue-lpcolorvinyl-cd?_pos=3&_sid=3e0eb5837&_ss=r"


def get_all_links(url):
    try:
        req = requests.get(url, verify=False)
        print(req)
        site = BeautifulSoup(req.text, "html.parser")
        #print(site)
        all_meta_content = list()

        for text in site.find_all('meta'):
            #print(text)
            all_meta_content.append(text.get('meta'))

        target_meta_data = None
        for tag in site.find_all('meta'):
            content = tag.get('content')
            if content and 'Chain Of Strength' in content:
                target_meta_data = tag
                break

        if target_meta_data:
            print("Meta tag found:")
            print(target_meta_data)

    except:
        print("qualquer coisa")


run = get_all_links(url)

print(run)
