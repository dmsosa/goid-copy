from goidcopy import googleimagesdownload

c = googleimagesdownload()
record = c.make_record({"keywords":"Mini golf", "limit":12, "webseite":"instagram.com"})
args = c._validate_parameters(record)
totalt, totale, abpaths = c.download(record, args)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import datetime
# from urllib.parse import quote
# search = "Taj mahal"
# import argparse
# import requests
# from urllib import request
# import ssl, os, sys
# from pathlib import Path, PureWindowsPath
# import json



# parser = argparse.ArgumentParser()
# parser.add_argument('-k', '--keywords', help='delimited list input', type=str, required=False)
# parser.add_argument('-kf', '--keywords_from_file', help='extract list of keywords from a text file', type=str, required=False)
# parser.add_argument('-sk', '--suffix_keywords', help='comma separated additional words added to main keyword', type=str, required=False)
# parser.add_argument('-l', '--limit', help='delimited list input', type=str, required=False)
# parser.add_argument('-f', '--format', help='download images with specific format', type=str, required=False,
#                     choices=['jpg', 'gif', 'png', 'bmp', 'svg', 'webp', 'ico'])
# parser.add_argument('-u', '--url', help='search with google image URL', type=str, required=False)
# parser.add_argument('-x', '--single_image', help='downloading a single image from URL', type=str, required=False)
# parser.add_argument('-o', '--output_directory', help='download images in a specific directory', type=str, required=False)
# parser.add_argument('-d', '--delay', help='delay in seconds to wait between downloading two images', type=str, required=False)
# parser.add_argument('-c', '--color', help='filter on color', type=str, required=False,
#                     choices=['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink', 'white', 'gray', 'black', 'brown'])
# parser.add_argument('-ct', '--color_type', help='filter on color', type=str, required=False,
#                     choices=['full-color', 'black-and-white', 'transparent'])
# parser.add_argument('-r', '--usage_rights', help='usage rights', type=str, required=False,
#                     choices=['labled-for-reuse-with-modifications','labled-for-reuse','labled-for-noncommercial-reuse-with-modification','labled-for-nocommercial-reuse'])
# parser.add_argument('-s', '--size', help='image size', type=str, required=False,
#                     choices=['large','medium','icon','>400*300','>640*480','>800*600','>1024*768','>2MP','>4MP','>6MP','>8MP','>10MP','>12MP','>15MP','>20MP','>40MP','>70MP'])
# parser.add_argument('-t', '--type', help='image type', type=str, required=False,
#                     choices=['face','photo','clip-art','line-drawing','animated'])
# parser.add_argument('-w', '--time', help='image age', type=str, required=False,
#                     choices=['past-24-hours','past-7-days'])
# parser.add_argument('-wr', '--time_range', help='time range for the age of the image. should be in the format {"time_min":"MM/DD/YYYY","time_max":"MM/DD/YYYY"}', type=str, required=False)
# parser.add_argument('-a', '--aspect_ratio', help='comma separated additional words added to keywords', type=str, required=False,
#                     choices=['tall', 'square', 'wide', 'panoramic'])
# parser.add_argument('-si', '--similar_images', help='downloads images very similar to the image URL you provide', type=str, required=False)
# parser.add_argument('-ss', '--specific_site', help='downloads images that are indexed from a specific website', type=str, required=False)
# parser.add_argument('-p', '--print_urls', default=False, help="Print the URLs of the images", action="store_true")
# parser.add_argument('-ps', '--print_size', default=False, help="Print the size of the images on disk", action="store_true")
# parser.add_argument('-m', '--metadata', default=False, help="Print the metadata of the image", action="store_true")
# parser.add_argument('-e', '--extract_metadata', default=False, help="Dumps all the logs into a text file", action="store_true")
# parser.add_argument('-st', '--socket_timeout', default=False, help="Connection timeout waiting for the image to download", type=float)
# parser.add_argument('-th', '--thumbnail', default=False, help="Downloads image thumbnail along with the actual image", action="store_true")
# parser.add_argument('-la', '--language', default=False, help="Defines the language filter. The search results are authomatically returned in that language", type=str, required=False,
#                     choices=['Arabic','Chinese (Simplified)','Chinese (Traditional)','Czech','Danish','Dutch','English','Estonian','Finnish','French','German','Greek','Hebrew','Hungarian','Icelandic','Italian','Japanese','Korean','Latvian','Lithuanian','Norwegian','Portuguese','Polish','Romanian','Russian','Spanish','Swedish','Turkish'])
# parser.add_argument('-pr', '--prefix', default=False, help="A word that you would want to prefix in front of each image name", type=str, required=False)
# parser.add_argument('-px', '--proxy', help='specify a proxy address and port', type=str, required=False)

# dicto = {'key':3, 'pedro':4, 4:'martes'}
# print(4 in dicto)
# for i in prefixed_words:
#     search_keyword.append(i)
# print(search_keyword)
# root = 'https://www.google.com/search?q='
# base = '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch'
# closer = '&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'

# url = root+'chess'+base+closer

# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

# req1 = request.Request(url, headers=headers)
# resp1 = request.urlopen(req1)
# content = str(resp1.read())
# print(content.encode('latin1').decode())
# div = content.find()
# session = requests.Session()
# content = session.get(url, headers=headers) 
# print(content.text)


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



# # _get_similar_images()
# opt = Options()
# opt.add_experimental_option('detach', True)
# # opt.add_argument('--headless=new')
# serv = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=serv, options=opt)

# base = '&tbm=isch&sa=X&ved=2ahUKEwidnoqs_oGAAxUmVaQEHUMPDDcQ0pQJegQIDBAB&biw=1280&bih=648&dpr=1.5'
# root = 'https://www.google.com/search?q='
# url = root+'balls'+base
# driver.get(url)
# accept = driver.find_element(By.CSS_SELECTOR, 'button[jsname="b3VHJd"]')
# accept.click()
# for i in range(10):
#     driver.execute_script("window.scrollBy(0, 10000)")
#     time.sleep(2)
#     i += 1
# show_more = driver.find_element(By.CSS_SELECTOR, "input[jsaction='Pmjnye']")
# show_more.click()
# data = driver.page_source.encode('utf-8')
# print(data)
# driver.quit()

# time.sleep(2)
# imgs = driver.find_elements(By.CSS_SELECTOR, 'div[jsname="DeysSe"]')
# print(imgs)

# links = list()
# for i in imgs:
#     img = i.find_element(By.CSS_SELECTOR, 'img[jsname="Q4LuWd"]')
#     link = img.get_attribute('src')
#     links.append(link)
