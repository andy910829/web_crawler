import requests
from bs4 import BeautifulSoup
import json


def search(keyword):
    url = 'https://www.momomall.com.tw/mmlsearch/%s.html'
    headers = {
        'user-agent' : 'Mozilla/5.0'
    }
    r = requests.post(url%keyword, headers = headers, timeout = 10)
    r.raise_for_status()
    r.encoding = 'UTF-8'
    return r.text
 

def gethtml(html, list, list2):
    soap = BeautifulSoup(html, 'html.parser')
    price = soap.find_all('p',class_ = 'prdPrice')
    name = soap.find_all(class_ = 'prdName')
    for x in name:    
        list.append(x)
    for i in price:
        list2.append(i)

def printinfo(list, list2):
    for num in range(len(list)):
        print(list[num].text)
        print(list2[num].text)
               

def main():
    N_list = []
    P_list = []
    kw = input('請輸入商品名稱:')
    search(kw)
    gethtml(search(kw), N_list, P_list)
    printinfo(N_list, P_list)
    
main()
