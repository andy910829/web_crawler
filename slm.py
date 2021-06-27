from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import bs4

def search(name, driver):
    time.sleep(3)
    button = driver.find_element_by_id("stkNo")
    button.click()
    time.sleep(3)
    element = driver.find_element_by_id("stkNo")
    element.send_keys(Keys.CONTROL,'A')
    element.send_keys(name)
    time.sleep(2)
    button = driver.find_element_by_id("btn-search")
    button.click()
    time.sleep(5)
    
    
    
def gethtml(url, name):
    a = name
    r = requests.get(url + "stkNo=%s"%a, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

      
# def writedown(html, file):
#     soap = BeautifulSoup(html, "html.parser")
#     str = ("本日漲停","開盤競價基準","本日跌停")
#     file.write(str)
#     for num in soap.select('tr').contents:
#         #u_list.append(num[1].string, num[2].string, num[3].string)
#         file.write(num[1].string, num[2].string, num[3].string)
    

def main():
    i = 0
    name = []
    #u_list = []

    while (True): 
        name.append(input("請輸入代號，按0結束:"))
        i = i+1 
        print(name[i-1])
        if (name[i-1] == '0'):
            name.pop()
            i = i-1
            break

    driver = webdriver.Chrome("C:\\Users\\88696\\Dropbox\\我的電腦 (LAPTOP-SVUIPIGO)\\Desktop\\chromedriver.exe")
    driver.get("https://www.twse.com.tw/zh/stockSearch/stockSearch")

    f = open("stock.txt","w",encoding = "utf-8")
 

    for count in range(i):
        search(name[count], driver)
        url = "https://www.twse.com.tw/zh/stockSearch/showStock?"
        gethtml(url, name[count])
        #writedown(gethtml(url), f)
        f.write(gethtml(url, name[count]))
    
    f.close()
main()    

