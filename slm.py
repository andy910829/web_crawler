from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys


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
    
    
    
def gethtml(url):
    r = requests.get(url, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

      
# def writedown(html):
#     print("")



def main():
    i = 0
    name = []

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
        url = "https://www.twse.com.tw/zh/stockSearch/stockSearch"
        gethtml(url)
        f.write(gethtml(url))

    f.close()
main()    

