import requests
from bs4 import BeautifulSoup
import time
import os


def search(keyword):
    try:
        url = 'https://www.momomall.com.tw/mmlsearch/%s.html'
        headers = {
            'user-agent' : 'Mozilla/5.0'     
        }
        r = requests.post(url%keyword, headers = headers, timeout = 10)
        r.raise_for_status()
        r.encoding = 'UTF-8'
        return r.text
    except:
        print('檢查網路問題!')
 

def gethtml(html, list, list2):
    try:
        soap = BeautifulSoup(html, 'html.parser')
        price = soap.find_all('p', class_ = 'prdPrice')
        name  = soap.find_all(class_ = 'prdName')
        for x in name:    
            list.append(x)
        for i in price:
            list2.append(str(i))
    except:
        print('出現錯誤')

def writeinfo(list, list2, f):
    priz = []
    for num in range(len(list)):
        f.write('商品名稱:')
        f.write(str(list[num].text))
        f.write('\n')
        f.write('商品價格:')
        priz.append('')
        a = list2[num].find('$')
        b = list2[num].find('</b>')
        for i in range(a, b):
            priz[num] += list2[num][i]
        f.write(priz[num])
        f.write('\n')
                

def main():
    N_list = []
    P_list = []
    f = open('momo.txt', 'w', encoding = 'utf-8')
    kw = input('請輸入商品名稱:')
    search(kw)
    gethtml(search(kw), N_list, P_list)
    writeinfo(N_list, P_list, f)
    f.close()
    print('下載完成')
    os.system('pause')
    
main()
