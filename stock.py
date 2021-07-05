import requests
from bs4 import  BeautifulSoup

def search(url):
    headers = {
    'user-agent' : 'Mozilla/5.0'
    }
    r = requests.get(url, headers = headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text

def gethtml(text):
    soap = BeautifulSoup(text, 'html.parser')
    table = soap.find_all('tr', align = 'center')
    for i in range(len(table)):
        if i == 1:
            td = table[i]('td')
    for x in range(len(td)):
        if x == 4:
            print(td[x].text)
    

def main():
    url = 'https://tw.stock.yahoo.com/us/q?s=^DJI'
    search(url)
    gethtml(search(url))
main()