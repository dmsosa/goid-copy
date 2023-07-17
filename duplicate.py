##Dieses Programm die gleiche Funktion als den my.py macht, aber mit Selenium


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
from urllib.parse import quote
search = "Taj mahal"
import argparse

p = argparse.ArgumentParser()
p.add_argument('-k', '--key', required=False)
p.add_argument('-m', '--mode', required=True)
p.add_argument('-n', '--number', required=False)
arg = p.parse_args()
search_keyword = 'pepe'
wanted = ['number']
values = [i[1] for i in arg._get_kwargs() if i[1] is not None and i[0] in wanted]
print(values)
dir_name = search_keyword
for j in values:
    dir_name += (" - " + j if j is not None else '')
print(dir_name)
# opt = Options()
# opt.add_experimental_option('detach', True)
# # opt.add_argument('--headless=new')
# serv = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=serv, options=opt)

# base = '&tbm=isch&sa=X&ved=2ahUKEwidnoqs_oGAAxUmVaQEHUMPDDcQ0pQJegQIDBAB&biw=1280&bih=648&dpr=1.5'
# root = 'https://www.google.com/search?q='
# url = root+'balls'+base
# driver.get(url)
# time.sleep(2)
# accept = driver.find_element(By.CSS_SELECTOR, 'button[jsname="b3VHJd"]')
# accept.click()
# time.sleep(2)
# imgs = driver.find_elements(By.CSS_SELECTOR, 'div[jsname="DeysSe"]')
# print(imgs)

# links = list()
# for i in imgs:
#     img = i.find_element(By.CSS_SELECTOR, 'img[jsname="Q4LuWd"]')
#     link = img.get_attribute('src')
#     links.append(link)
