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
from urllib import request
import ssl, os, sys
from pathlib import Path, PureWindowsPath

searchUrl = 'https://www.google.com/search?q=dog&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

req1 = request.Request(searchUrl, headers=headers)
resp1 = request.urlopen(req1)
content = str(resp1.read())
print(content)
l1 = content.find('AMhZZ')
l2 = content.find('&', l1)
urll = content[l1:l2]
print('urll', urll)
newurl = "https://www.google.com/search?tbs=sbi:" + urll + "&site=search&sa=X"
req2 = request.Request(newurl, headers=headers)
resp2 = request.urlopen(req2)
print(resp2.read())
l3 = content.find('/search?sa=X&amp;q=')
l4 = content.find(';', l3 + 19)

urll2 = content[l3 + 19:l4]
print('urll2', urll2)

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
#                 }

# search_keyword = ['pepe']
# ctx = ssl._create_unverified_context()
# def _get_similar_images():
#     url =  'https://www.google.com/search?q=bears&tbm=isch&hl=de&tbs=itp:animated&sa=X&ved=0CAQQpwVqFwoTCJDb8rX3nIADFQAAAAAdAAAAABAD&biw=1263&bih=648#imgrc=miwZI7W5W69sGM'
#     req = request.Request(url, headers=headers)
#     response = request.urlopen(req, None, timeout=10, context=ctx)
#     s = str(response.read())
#     start = s.find('<a class="wXeWr islib nfEiy"')
#     href = s.find('')
#     print(start)
#     print(s[start:start+10])
    # while len(s) > 10:
    #     start_line = s.find('rg_di')
    #     if start_line == -1:  # If no links are found then give an error!
    #         end_quote = 0
    #         link = "no_links"
    #         print(link)
    #     start_line = s.find('"class="rg_meta"')
    #     start_content = s.find('"ou"', start_line + 1)
    #     end_content = s.find(',"ow"', start_content + 1)
    #     content_raw = str(s[start_content + 6:end_content - 1])
    #     print("content////////////\n\n\n\n\n\n\n\n/////////////",content_raw)
    #     s = s[end_content:]

    #<a href=> finden
    

    #Query erhalten



# _get_similar_images()
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
