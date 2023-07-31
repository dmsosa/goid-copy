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
import json


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
parser.add_argument('-to', '--timeout', help='Geben Sie an, die Zeit die wir fur an Antwort von der System warten sollen')
parser.add_argument('-pr', '--print', help="Zeichen Sie die URL von der gegeben Bildern!", default=False, action="store_true")
parser.add_argument('-sc', '--write', help="Auswahlen sie, ob ein Textdatei zu erstellen oder nicht", default=False, action="store_true")
parser.add_argument('-m', '--metadata', help="Geben Sie an, ob das Metadatei den Bildern zu gezeigt oder nicht", default=False, action="store_true")
parser.add_argument('-au', '--auszug', help="Auswahlen Sie an, ob das Metadatei den Bildern zu auszugen oder nicht", default=False, action="store_true")
parser.add_argument('-lm', '--lautlos', help="Aktivieren dieses Lautlos-Modus, um die Programm ohne Nachrichten zu laufen!", default=False, action="store_true")
parser.add_argument('-pre', '--prefix', help="Geben Sie ein Prafix an, dass an der Beginnen von jedem Suchen hinzugefugt werde!", default=False, action="store_true")
parser.add_argument('-la', '--language', help="Auswahlen in welche Sprache mochtest Du die Suchergebnisse erhalten!", choices=['Arabic','Chinese (Simplified)','Chinese (Traditional)','Czech','Danish','Dutch','English','Estonian','Finnish','French','German','Greek','Hebrew','Hungarian','Icelandic','Italian','Japanese','Korean','Latvian','Lithuanian','Norwegian','Portuguese','Polish','Romanian','Russian','Spanish','Swedish','Turkish'])
args = parser.parse_args()
#============= Parameter prufen =============

if (args.keywords is None) and (args.url is None) and (args.single is None):
    parser.error('Keywordsargument obligatorisch ist!')

if args.suffix:
    suffix_keywords = [str(i).strip() for i in args.suffix.split(",")]
    suffix_keywords.insert(0, '')
else:
    suffix_keywords = ['']

if args.keywords:
    search_keyword = [str(i) for i in args.keywords.split(',')]
else:
    search_keyword = []

if args.prefix:
    prefix = str(args.prefix).split(',')
    for i in range(len(prefix)):
        prefix[i] = prefix[i].strip()

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
if args.timeout:
    try:
        timeout = float(args.timeout)
    except TypeError:
        print("Die Zeituberschreitung ein Gleitkommazahlen sind muss!")
else: timeout = 15
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
                resp = request.urlopen(req, data=None, timeout=timeout, context=ctx)
                if mode == 'bytes':
                    rawPage = resp.read()
                else:

                    rawPage = str(resp.read().decode('utf-8'))
                return rawPage
            except Exception as err:
                print(err)
                return 'Page Not Found'
def download_image(object, dir, count, format=""):
    try: 
        url = object[1]['link']
    except KeyError:
        print('Ungultiges Objekt!')
        download_status = 'Versagen'
        download_message = 'Es tut mir leid aber wir diese Datei nicht benutzen kann'
        return object, download_status, download_message
        
    if args.print:
        print("BILDER URL:",url)
    try:
        #Seite herunterladen
        data = download_page(url, mode='bytes')
        imgName = _find_name(url)
        if format == "":
            imgName = imgName + "-" + str(count) + "." + "jpg"
        else:
            imgName = imgName + "-" + str(count) + "." + format
        img_path, save_status = _save_image(dir, data, imgName)
        #Die Gross und die Zeit definieren
        size = _get_size(img_path)
        zeit = str(datetime.datetime.now()).split('.')[0]
        object[1]['size'] = size
        object[1]['time'] = zeit
        download_status = 'Erfolg'
        download_message = 'Die Bilder '+imgName+' erfolglich gespeichert ist /// 100% herunterladen'
        return object, download_status, download_message
    except UnicodeDecodeError as err:
        download_status = 'Versagen'
        download_message = err + " in ein Bild, die nachsten versuchen..."
        return object, download_status, download_message
    except HTTPError as err:
        download_status = 'Versagen'
        download_message = err + " in ein Bild, die nachsten versuchen..."
        return object, download_status, download_message
    except URLError as err:
        download_status = 'Versagen'
        download_message = err + " in ein Bild, die nachsten versuchen..."
        return object, download_status, download_message
    except ssl.CertificateError as err:
        download_status = 'Versagen'
        download_message = err + " in ein Bild, die nachsten versuchen..."
        return object, download_status, download_message
    except IOError as err:
        download_status = 'Versagen'
        download_message = err + " in ein Bild, die nachsten versuchen..."
        return object, download_status, download_message

        

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
def _get_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        size = file_info.st_size
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "3%.1f %s"%(size, x)
            size /= 1024.0

def _get_next_item(rawPage):
    #Dieses Abfragen sind die Ziechenfolgen, nach denen wir suchen, um die Datei aus unseren Bildern zu extrahieren
    queries = {'link':['<img data-src=', '" data-ils'],
               'title':['<h3 class="bytUYc">', '</h3>'],
               'height':['data-oh="','"'],
               'width':['data-ow="','"'],
               'site':['<div class="LAA3yd">','</div>']}
    #Dateiinhalt finden
    start_line = rawPage.find(queries['link'][0])
    end_content = rawPage.find('</h3>', start_line)
    if start_line == -1:
        end_quote = 0
        img_object = "no_links"
        return img_object, end_quote
    else:
        #Link finden
        end_link = rawPage.find(queries['link'][1],start_line+len(queries['link'][0]))
        img_link = str(rawPage[start_line+len(queries['link'][0])+1:end_link])
        #Titel finden
        title_start = rawPage.find(queries['title'][0], start_line)
        title_end = rawPage.find("</h3>", title_start+len(queries['title'][0]))
        title = rawPage[title_start+len(queries['title'][0]):title_end]
        #Hoch finden
        height_start = rawPage.find(queries['height'][0], start_line)
        height_end = rawPage.find(queries['height'][1], height_start+len(queries['height'][0]))
        height = rawPage [height_start+len(queries['height'][0]):height_end]
        #Breite finden
        width_start = rawPage.find(queries['width'][0], start_line)
        width_end = rawPage.find(queries['width'][1], width_start+len(queries['height'][0]))
        width = rawPage [width_start+len(queries['width'][0]):width_end]
        #Seite finden
        site_start = rawPage.find(queries['site'][0], start_line)
        site_end = rawPage.find(queries['site'][1], site_start)
        site = rawPage[site_start+len(queries['site'][0]):site_end]
    img_object = (title[:16], {'link':img_link, 'width':width, 'height':height, 'title':title, 'site':site})
    return img_object, end_content
def _get_all_items(page, directory, index, limit):
    items = []
    count = 0
    success = 0
    error_count = 0
    searchName = directory.split('/')[-1]
    if args.write:
        tuple = (index, searchName)
        _write_txt(tuple, mode='item')
    format = (args.format if args.format else '')
    while count < limit:
        item_object, end_content = _get_next_item(page)
        if item_object == 'no_links':
            print('no more links')
            break
        else:
            page = page[end_content:]
            item_object, download_status, download_message = download_image(item_object, directory, count+1, format)
            if download_status == 'Erfolg':
                items.append(item_object)
                if not args.lautlos:
                    print(download_message)
                if args.metadata:
                    print("Bilder Metadatei:\n"+str(item_object))
                if args.write:
                    _write_txt(str(item_object))
                    if not args.lautlos:
                        print("Textdatei schreibt!")
                count += 1
                success += 1
            else:
                error_count += 1
                if not args.lautlos:
                    print(download_message)
            if args.pause:
                time.sleep(pause)
    if success < limit:
        if not args.lautlos:
            print('Es tut mir leid, aber ' + str(success) + ' ist alles, dass wir fur dieses Seite haben!')
    return items, error_count

def _find_search(url):
    start = url.find('q=')
    end = url.find("&tbm=")
    search_term = url[start+2:end]
    return search_term
def _find_name(url):
    imgName = url[url.rfind('/')+1:]
    if '?' in imgName:
        imgName = imgName[:imgName.find('?')]
    #Extension entfernen
    imgName = imgName[:imgName.rfind('.')]
    imgName = imgName.replace(".", "-")
    imgName = unquote_plus(imgName)
    return imgName
def _save_image(directory, data, imgName):
    if type(data) is not str and type(data) is not None:
        try:
            target_dir = directory +"/"+ imgName
            if not os.path.exists(target_dir):
                with open(target_dir, "wb") as saver:
                    saver.write(data)
                    save_status = 'Bilder gespeichert!'
                    return target_dir, save_status
            else: 
                save_status = 'Es gibt schon ein Bilder!'
                return target_dir, save_status
        except Exception as err:
            print(err)
            target_dir = 'no_path'
            save_status = err + " - image not saved"
            return target_dir,  save_status
    else:
        target_dir = 'no_path' 
        save_status = "Kein Datei, image not saved"
        return target_dir,  save_status

def _url_bauen(search):
    bauen = "&tbs="
    root = 'https://www.google.com/search?q='
    base = '&tbm=isch'
    if args.language:
        param = {"Arabic":"ar","Chinese (Simplified)":"zh-CN","Chinese (Traditional)":"zh-TW","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Estonian":"et","Finnish":"fi","French":"fr","German":"de","Greek":"el","Hebrew":"iw ","Hungarian":"hu","Icelandic":"is","Italian":"it","Japanese":"ja","Korean":"ko","Latvian":"lv","Lithuanian":"lt","Norwegian":"no","Portuguese":"pt","Polish":"pl","Romanian":"ro","Russian":"ru","Spanish":"es","Swedish":"sv","Turkish":"tr"}
        language = '&hl=' + param[args.language]
    else: language = '&hl=pt'
    closer = language+'&sa=X&ved=0CAIQpwVqFwoTCKDZgKG4qYADFQAAAAAdAAAAABAD&biw=1263&bih=648'
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
def _write_txt(data, mode='content'):
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
    t0 = time.time()
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

def bulk_download(search_keyword, suffix_keywords, main_dir, limit):
    t0 = time.time()
    total_errors = 0
    if args.url:
        search = _find_search(args.url)
        search_keyword.append(search)
        url = args.url
        if args.ahnlich:
            _get_similar_images(url, args.ahnlich)
    if args.prefix:
        prefixed_words = [str(j) + " " + str(i) for i in search_keyword for j in prefix]
        for i in prefixed_words:
            search_keyword.append(i)
    for suffix in suffix_keywords:
        i = 0 
        while i < len(search_keyword):
            rootword = search_keyword[i].strip()
            word = rootword + " " + suffix
            iteration = "\nSuchen nu.:" + str(i+1) + " / / == > " + word
            if not args.lautlos:
                print(iteration+"\n"+"Auswertend...")
            dir_name = _set_name(word)
            directory = _create_dir(main_dir, rootword, dir_name).strip()
            if args.url is None or i > 0:
                url = _url_bauen(quote(word))
            page = download_page(url)
            #Die Sucheliste zu vermehren
            if args.ahnlich and i == 0:
                _get_similar_images(url, args.ahnlich)
            i += 1
            items, error_count = _get_all_items(page, directory, i+1, limit)
            if args.auszug:
                if (len(items) > 0):
                    zeit = time.strftime("%d-%B-%Y", time.gmtime())
                    logs_path = 'logs/'+zeit+"/"
                    try:
                        if not os.path.exists(logs_path):
                            os.makedirs(logs_path)
                    except OSError as error:
                        print(error)
                    with open(logs_path+word+".json", "a") as js:
                        js.write(json.dumps(items, indent=4))
                    if not args.lautlos:
                        print('JSONDatei erstellen!')
                else: print("Leereres Datei, wir kann keine JSON schreiben!")
            total_errors += error_count
    t1 = time.time() 
    total_time = t1 - t0
    return total_time, total_errors

            
    #     /////////////////  Ende des Programm  /////////////////

if args.single:
    _single_image_download()
else:
    total_time, total_errors = bulk_download(search_keyword, suffix_keywords, main_dir, limit)
    print('Alle Bildern herunterladen\nFehler:'+str(total_errors)+"\n")
    # Berechnung die Gesamtzeit, die benotig wird, um alle links von 60.000 Bilder zu crawlen, zu finden und herunterzuladen
    print("Gesamtzeitaufwand: "+ str(total_time)+ " Sekunden\n(ist die Zeit die wir verbracht haben, die Bildlinks zu finden!)")

# %%
