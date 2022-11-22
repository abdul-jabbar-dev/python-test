import requests
import re
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'

get_res = requests.get(url).text.encode('utf-8').decode('ascii', 'ignore')
get_xml = BeautifulSoup(get_res, 'lxml')
get_table = get_xml.find(class_='wikitable')

xml_text = get_table.find_all('tr')[1:]
for tag in xml_text:
    try:
        model_string = tag.find_all(['td', 'th'])[0].a.text.split(' ')[1]
        models  = model_string = re.sub(r"\D", "", model_string)
        print(models)
    except:
        pass
