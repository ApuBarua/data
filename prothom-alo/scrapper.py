import urllib.request
from bs4 import BeautifulSoup
import io

def scrap(address, date):
    page = urllib.request.urlopen(address)
    soup = BeautifulSoup(page,"html.parser")    
    title = soup.find_all("span",attrs={"class":"title"})

    with io.open('output/'+date+'.txt', 'a', encoding='utf-8') as file:
        for i in title:
            file.write(i.get_text())
            file.write('\n')
            # print(i.get_text(),"\n")
    if len(title) < 20:
        return False
    return True