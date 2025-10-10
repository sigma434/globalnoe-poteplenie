import requests
from bs4 import BeautifulSoup
import pandas as pd

f = open('text.txt', 'r', encoding='UTF-8')
text = f.read()
print(text)
f.close()

import requests
from bs4 import BeautifulSoup
import pandas as pd

def parsing():
 
    url = 'https://www.sciencedaily.com/news/earth_climate/global_warming/'
    
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")

 
    temp = bs.find_all('div', class_="latest-head")

    dict_news = {"title": [], "link": []}

    for i in temp:
        
        dict_news["title"].append(i.text)
        dict_news["link"].append(i.find("a").get('href'))

    df_news = pd.DataFrame(dict_news, columns=["title", "link"])
    
  
    print(df_news)
    return df_news
