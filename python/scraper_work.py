""" Little bit about web scraping."""

import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "http://www.thewhiskeychange.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0: Wind64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t = {}
data = []
c = 0
for x in range(1,6):
    k = requests.get('https://www.thewhiskeyexchandge.com/c/36/japanese-whiskey?pg={}&psize=24&sort=pasc'.format(x)).text
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"prduct_grid__item"})

    for product in prductlist:
        link = product.find("a",{"class":"prduct_card"}).get('href')
        prductlinks.append(baseurl + link)

for link in productlinks:
    f = request.get(link,headers=headers).text
    hub=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None
        
    try:
        about=hun.find("div",{"class":"prduct-main__description"}).text.replace('\n',"")
    except:
        about = None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating = None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name = None

    whiskey = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(whisky)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)


