# In[ ]:
# -*- coding: utf-8 -*-

#///////////////// Programm zu starten /////////////////

#die notwendig Modulen zu importieren

import time, datetime #Wie mochten es wissen, wie lang unsere Programm zu beenden annehmen
import sys, os, ssl #Sys und os Library zu importieren
from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote_plus
import argparse


#Selenium benutzen, falls es notwendig ist
from selenium import webdriver
from selenium.webdriver.common.by import By

sys.stdout.reconfigure(encoding='utf-8')
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keywords', help='Delimited keywords for searching images', required=False)
parser.add_argument('-sk', '--suffix', help='suffix keywords for searching more related images', required=False)
parser.add_argument('-l', '--limit', help='Delimited list input', required=False)
parser.add_argument('-c', '--color', help='Filtering by color', required=False, choices=[
    'red','yellow','blue','orange','violet','green','brown','white','black','gray','pink','teel','purple', 'brown'])
parser.add_argument('-ct', '--colortype', help='Filtern nach Farbenart', required=False, choices=['full-color', 'black-and-white', 'transparent'])
parser.add_argument('-u', '--url', help='Die Bildern nach Benutzerurl herunterladen werden', required=False)
parser.add_argument('-o', '--output', help='Entmoglich dir, den Name von Ausgeben zu auswahlen', required=False, type=str)
parser.add_argument('-s', '--single', help='Macht es moglich, ein einzelnes Bilder zu herunterladen', required=False, type=str)
parser.add_argument('-p', '--pause', help='Bezeicht die Zeit, dass wir warten wird zwischen Bildern', required=False, type=int)
parser.add_argument('-g', '--grosse', help='Sagt Sie, wie Grosse den Bildern sollen sind', required=False, choices=['large','medium','icon'])
parser.add_argument('-t', '--type', help='Bezeicht die Typ oder Art von Bildern dass wir finden wird', required=False, choices=['face','photo','clip-art','lineart','animated'])
parser.add_argument('-z', '--time', help='Bezeicht die Zeit, in dass den Bildern hochgeladen wurden', required=False, choices=['past-24-hours','past-7-days','past-1-month','past-1-year'])
parser.add_argument('-r', '--rechte', help='Wahlen Sie der Benutzbedingungen dieses Bildern', required=False, type=str, choices=['labled-for-reuse-with-modifications','labled-for-reuse','labled-for-noncommercial-reuse-with-modification','labled-for-nocommercial-reuse'])
parser.add_argument('-f', '--format', help='Wahlen Sie der Format der Verwendung dieses Bildern', required=False, type=str, choices=['svg', 'gif', 'jpg', 'png', 'jpeg', 'tbn', 'ico', 'webp', 'bmp'])
parser.add_argument('-a', '--ahnlich', help='Geben Sie an, ob Sie nach ahnlichen Bildern suchen mochte', required=False, type=int)
parser.add_argument('-ar', '--aspekt', help='Geben Sie an, die Ratioaspekt den Bildern aus', required=False, type=str, choices=['tall', 'wide', 'panoramic', 'square'])
parser.add_argument('-w', '--webseite', help='Geben Sie an, die Webseite vor den die Bildern herunterladen werden sollen', required=False, type=str)
# parser.add_argument('-h', '--help', help='Zeichen des Hilfebeschreibung uber alle der obigen Argumente an')
parser.add_argument('-pr', '--print', help="Zeichen Sie die URL von der gegeben Bildern!", default=False, action="store_true")
args = parser.parse_args()
#============= Parameter prufen =============

if (args.keywords is None) and (args.url is None) and (args.single is None):
    parser.error('Keywordsargument obligatorisch ist!')

if args.suffix:
    suffix_keywords = [str(i).strip() for i in args.suffix.split(",")]
else:
    suffix_keywords = None

if args.keywords:
    search_keyword = [str(i) for i in args.keywords.split(',')]
    if args.suffix:
        for i in suffix_keywords:
            search_keyword.append(args.keywords+" "+i)
if args.limit:
    limit = int(args.limit)
    if int(args.limit) >= 100:
        limit = 100
else:
    limit = 100

if args.output:
    main_dir = args.output
else:
    main_dir = 'downloads'

if args.pause:
    try:
        pause = int(args.pause)
    except ValueError:
        parser.error('Die Pause muss ein Zahl sein!')
if not args.pause: 
    pause = 0

if args.webseite:
    if "." not in args.webseite:
        parser.error("Ungultiger Webseite!")
    if " " in args.webseite:
        parser.error("Ungultiger Webseite!")
if args.print:
    printURL = 'yes'
else:
    printURL = 'no'
##============= Globalen Variablen initialisieren =============

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
ctx = ssl._create_unverified_context()


#============= Funktionen erstellen =================

def download_page(url, mode=''):
        version = (3,0)
        current_version = sys.version_info
        if current_version >= version:
            try:
                headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
                req = request.Request(url, headers=headers)
                resp = request.urlopen(req, timeout=10, context=ctx)
                if mode == 'str':
                    rawPage = str(resp.read())
                else:
                    rawPage = resp.read()
                # print(rawPage)
                return rawPage
            except Exception as err:
                print(err)
                return 'Page Not Found'

def _get_similar_images(url, n_Times):
    url = url
    req = request.Request(url, headers=headers)
    response = request.urlopen(req, None, timeout=10, context=ctx)
    data = str(response.read())
    #<a href=> finden
    c = 0
    if n_Times > 12:
        n_Times = 12
    similarImage = True
    while c < n_Times:
        start_similar_images = data.find('<h2 class="OkhOw gadasb">')
        if start_similar_images == -1:
            #Keine Ahnliche Bildern gefunden
            break
        first_similar_image = True
        while similarImage and c < n_Times:
            if first_similar_image:
                start_href = data.find('<a href="', start_similar_images)
                first_similar_image = False
            else:
                start_href = data.find('<a href="')
            end_href = data.find('"', start_href+9)
            href = data[start_href+9:end_href]
            data = data[end_href:]

            
            
            query_start = href.find('?q=')
            query_end = href.find('&amp;')
            query = href[query_start+3:query_end]
            start_a_tag = data.find('<a href="')
            end_a_tag = data.find('>', start_a_tag)
            a_tag = data[start_a_tag:end_a_tag]


            if 'class="mgK4fd"' not in a_tag:
                similarImage = False
            else:
                similarImage = True

            #Das query am unsere Schlusselwortliste hinzufugen
            global search_keyword
            search_keyword.append(unquote_plus(query))
            c += 1
def _images_get_next_item(rawPage):
    start_line = rawPage.find('<img data-src=')
    if start_line == -1:
        end_quote = 0
        link = "no links"
        return link, end_quote
    else:
        # start_line = s.find('<img data-src=')
        # start_content = s.find('imgurl=',start_line+1)
        end_content = rawPage.find('" data-ils',start_line+15)
        content_raw = str(rawPage[start_line+15:end_content])
        if 'FLAVICON' not in content_raw:
            return content_raw, end_content
        else: 
            link = 'no links'
            end_quote = 0
            return link, end_quote
def _images_get_all_images(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == 'no links':
            print('no more links')
            break
        else:
            items.append(item)
        #Alle die Items in dem List "Links" bekannt zu hinzufugen
        #Timer konnte verwendet werden, um den Anfrage fur das Herunterladen von Bildern zu verlangsamen
            page = page[end_content:]
            if len(items) > limit:
                break
    return items
def _find_search(url):
    start = url.find('q=')
    end = url.find("&tbm=")
    search_term = url[start+2:end]
    return search_term
def _find_name(url):
    imgName = url[url.rfind('/'):]
    if '?' in imgName:
        imgName = imgName[:imgName.find('?')]
    imgName = unquote_plus(imgName)
    #Extension entfernen
    imgName = imgName[:imgName.rfind('.')]
    imgName = imgName.replace(".", "-")
    return imgName
def _save_image(directory, data, imgName):
    if type(data) is not str and type(data) is not None:
        try:
            if args.format:
                target_dir = directory +"/"+ imgName + "." + args.format
                if not os.path.exists(target_dir):
                    with open(target_dir, "wb") as saver:
                        saver.write(data)
                else:print('Es gibt schon ein Bilder!')
            else:
                target_dir = directory +"/"+ imgName + ".jpg"
                
                if not os.path.exists(target_dir):
                    with open(target_dir, "wb") as saver:
                        saver.write(data)
                else: print('Es gibt schon ein Bilder!')
        except Exception as err:
            print(err, "- image not saved")
    else: print("Kein Bild, image not saved")

def _url_bauen(search):
    bauen = "&tbs="
    root = 'https://www.google.com/search?q='
    base = '&tbm=isch'
    closer = '&hl=pt&sa=X&ved=0CAIQpwVqFwoTCKDZgKG4qYADFQAAAAAdAAAAABAD&biw=1263&bih=648'

    params = {
        'color':[args.color, {'red':'ic:specific,isc:red', 'orange':'ic:specific,isc:orange', 'yellow':'ic:specific,isc:yellow', 'green':'ic:specific,isc:green', 'teal':'ic:specific,isc:teel', 'blue':'ic:specific,isc:blue', 'purple':'ic:specific,isc:purple', 'pink':'ic:specific,isc:pink', 'white':'ic:specific,isc:white', 'gray':'ic:specific,isc:gray', 'black':'ic:specific,isc:black', 'brown':'ic:specific,isc:brown'}],
        'type':[args.type, {'face':'itp:face','photo':'itp:photo','clip-art':'itp:clip-art','lineart':'itp:lineart','animated':'itp:animated'}],
        'format':[args.format, {'jpg':'ift:jpg','gif':'ift:gif','png':'ift:png','bmp':'ift:bmp','svg':'ift:svg','webp':'webp','ico':'ift:ico'}],
        'grosse':[args.grosse, {'large':'isz:l', 'medium':'isz:m', 'small':'isz:s', 'icon':'isz:i'}], 
        'rechte':[args.rechte, {'labled-for-reuse-with-modifications':'sur:fmc', 'labled-for-reuse':'sur:fc','labled-for-noncommercial-reuse-with-modification':'sur:fm','labled-for-nocommercial-reuse':'sur:f'}],
        'time':[args.time, {'past-24-hours':'qdr:d','past-7-days':'qdr:w', 'past-1-year':'qdr:y'}],
        'color-type':[args.colortype, {'full-color':'ic:color','black-and-white':'ic:gray', 'transparent':'ic:trans'}],
        'aspect_ratio':[args.aspekt,{'tall':'iar:t','square':'iar:s','wide':'iar:w','panoramic':'iar:xw'}]
          }
    
    c = 0
    for i in params:
        value = params[i][0]
        if value is not None:
            output_param = params[i][1][value]
            if c == 0:
                bauen += output_param
                c += 1
            else:
                bauen += "%2C"+output_param
    if args.webseite:
        url = root+search+",site:"+args.webseite+base+bauen+closer
    else:
        url = root+search+base+bauen+closer
    return url
def _write_txt(data, mode='item'):
    if mode == 'item':
        with open('./links.txt', 'a', encoding='utf-8') as writer:
            writer.write(str(data[0])+":"+data[1]+" = \n\n")
    if mode == 'content':
        with open('./links.txt', 'a', encoding='utf-8') as writer:
            writer.write(data +"\n\n\n")
def _create_dir(*directories):
    try: 
        dirs = list(directories)
        c = 0
        target = ""
        for i in dirs:
            if c == 0:
                target += i
            else:
                target += "/"+i
            c += 1
        os.makedirs(target)
    except OSError as e:
        if e.errno != 17:
            raise
        pass
    return target
def _set_name(dir):
    worked_name = dir
    desired_args = ['color','type','gross','rechte','time','format','colortype','aspekt','webseite']
    values = [i[1] for i in args._get_kwargs() if i[0] in desired_args and i[1] is not None]
    for value in values:
        #Ausschielssen der Domain aus dem Webseite-Namen
        if "." in value:
            value = value[:value.find('.')]
        worked_name += " - " + value
    return worked_name

def _single_image_download():
    url = args.single
    try:
        imgData = download_page(url)
    except HTTPError:
        print("HTTP Fehler!")
    except URLError:
        print("URL Fehler!")
    except IOError:
        print("IO Fehler!")
    imgName = _find_name(url)
    directory = _create_dir(main_dir)
    _save_image(directory, data=imgData, imgName=imgName)


    t1 = time.time()
    total_time = t1 - t0

    print("Bilder erfolgreich gespeichert! =====> "+imgName)
    print("Programm Erfullt in "+str(total_time)+" Sekunden")
    return

#============= Das Hauptprogramm =============

def bulk_download(search_keyword, suffix_keyword, main_dir, limit, pause, printURL):
    t0 = time.time()

    if args.output:
        main_dir = args.output
    else: main_dir = 'downloads'

    if args.single:
        _single_image_download()
    else:
        i = 0
        if args.url:
            url = args.url
            search_keyword = []
            search = _find_search(url)
            print("search", search)
            search_keyword.append(search)
            if args.ahnlich:
                _get_similar_images(args.url, args.ahnlich)
        print(search_keyword)
        while i < len(search_keyword):  

            items = list()
            #Dateiort bauen
            iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
            print (iteration)
            word = search_keyword[i]
            # Den Textdatei schreiben
            tuple = (i+1, word)
            _write_txt(tuple)

            #Suchenwort definieren
            search = quote(word)

            # Der Name der Dateiort erstellen
            dir_name = _set_name(word)

            # Der Aussgabeverzeichnisses erstellen
        
            # url = _url_bauen(search)
            url = _url_bauen(search)
            if args.ahnlich and i == 0:
                _get_similar_images(url, args.ahnlich)
                print('Total to look for > ', search_keyword)
            page = download_page(url, mode='str')
            time.sleep(0.05)
            items = items + _images_get_all_images(page)


            print ("Image Links = "+str(items))
            print ("Total Image Links = "+str(len(items)))
            print ("\n")
            #Mit die nachsten Codezeilen konnen Sie alle Links in am neues .txt Datei schreiben, denn wird an die selber verzeichnis wie Ihr Code erstellt. Sie konnen die folgende 3 Zeilen auskommentieren, um keine Datei zu schreiben 

            #/////////////////Links.txt zu erstellen/////////////
            
            #Dem Datei schreiben
            _write_txt(str(items), mode='content')
            #Dem Datei zu schliessen
            
        #Bildern speichern
            k = 0
            errors = 0
            success = 1
            while k < len(items):
                try:
                    imgURL = items[k]
                    if printURL == 'yes':
                        print("\n" + str(items[k]))
                    data = download_page(imgURL, mode='bytes')
                    imgName = word + "-" + str(k+1)
                    directory = _create_dir(main_dir, dir_name)
                    _save_image(directory, data=data, imgName=imgName)
                except HTTPError:
                    print('HTTP Error in Bild: '+str(k+1))
                    errors += 1
                    k += 1
                    continue
                except URLError:
                    print('URL Error in Bild: '+str(k+1))
                    errors += 1
                    k += 1
                    continue
                print("Bild "+str(k+1)+" gespeichert")
                success += 1
                k += 1
                print(pause, "pauseee")
                time.sleep(pause)
            i += 1
            if success < limit:
                print("Leider konnte alle " + str(limit) + " Bildern nicht heruntergeladen werden, " + str(success) + " ist alles, was wir fur diesen Suchfilter bekommen haben!")
            return errors
            
    #     /////////////////  Ende des Programm  /////////////////

if args.single:
    _single_image_download()
else:
    t0 = time.time()
    error_count = bulk_download(search_keyword, suffix_keywords, main_dir, limit, pause, printURL)
    print('Alle Bildern herunterladen\nFehler:'+str(error_count)+"\n")
    t1 = time.time() 
    total_time = t1 - t0 
    # Berechnung die Gesamtzeit, die benotig wird, um alle links von 60.000 Bilder zu crawlen, zu finden und herunterzuladen
    print("Gesamtzeitaufwand: "+ str(total_time)+ " Sekunden\n(ist die Zeit die wir verbracht haben, die Bildlinks zu finden!)")

# %%
