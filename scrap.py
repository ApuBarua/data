import urllib.request
from bs4 import BeautifulSoup

address = "https://www.prothomalo.com/archive/2019-01-08"

page = urllib.request.urlopen(address)
soup = BeautifulSoup(page,"html.parser")

title = soup.find_all("span",attrs={"class":"title"})

for i in title:
    print("Title : ")
    print(i.get_text(),"\n")