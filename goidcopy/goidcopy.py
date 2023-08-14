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

##============= Globalen Variablen initialisieren =============

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
ctx = ssl._create_unverified_context()


#============= Klasse erstellen =================
class googleimagesdownload:
    def __init__(self):
        pass
#============= Funktionen erstellen =============

    def _validate_parameters(self, record):
        parser = argparse.ArgumentParser()
        if (record['keywords'] is None) and (record['url'] is None) and (record['single'] is None) and (record['extract'] is None):
            parser.error('Keywordsargument obligatorisch ist!\n\nBitte schau mal unsere GitHub Dokumentation, um das Program richtig benutz!\n\nwww.github.com\\duvi\\goidcopy')

        if record['suffix']:
            if record['suffix'] == 'random':
                suffix_keywords = ['course', 'college', 'school', 'for beginners', 'professional', 'curiosities', 'friendly', 'to learn', 'from 0 to hero', 'as it is', 'cool photos']
            else:
                suffix_keywords = [str(i).strip() for i in record['suffix'].split(",")]
                suffix_keywords.insert(0, '')
        else:
            suffix_keywords = ['']

        if record['keywords']:
            search_keyword = [str(i) for i in record['keywords'].split(',')]
        else:
            search_keyword = []

        if record['prefix']:
            if record['prefix'] == 'random':
                prefix = ['Real', 'Normal', 'Big', 'Small', 'Little', 'Pro', 'Pre', 'Post', 'Basic', 'Intermediate', 'Advance', 'How to']
            else:
                prefix = str(record['prefix']).split(',')
                for i in range(len(prefix)):
                    prefix[i] = prefix[i].strip()
        else: prefix = None
        if record['extract']:
            fname = str(record['extract'])
            with open(fname, 'r', encoding='utf-8') as fhand:
                if '.csv' in fname:
                    for line in fhand:
                        if line in ['\n', '\r\n']:
                            pass
                        else:
                            search_keyword.append(line.replace('\n', '').replace('\r', ''))
                elif '.txt' in fname:
                    for line in fhand:
                        if line in ['\n', '\r\n']:
                            pass
                        else:
                            search_keyword.append(line.replace('\n', '').replace('\r', ''))
                else:
                    print('Ungultiges Datei, bitte Geben Sie ein TXT oder CSV Art von Datei ein!\nAusgangen...')
                    sys.exit()
        if record['limit']:
            limit = int(record['limit'])
        else:
            limit = 100

        if record['output']:
            main_dir = record['output']
        else:
            main_dir = 'downloads'

        if record['pause']:
            try:
                pause = int(record['pause'])
            except ValueError:
                parser.error('Die Pause muss ein Zahl sein!')
        else: 
            pause = 0.05

        if record['webseite']:
            if "." not in record['webseite']:
                parser.error("Ungultiger Webseite!")
            if " " in record['webseite']:
                parser.error("Ungultiger Webseite!")
            webseite = record['webseite']
        else: webseite = None
        if record['print']:
            printURL = 'yes'
        else:
            printURL = 'no'
        if record['timeout']:
            try:
                timeout = float(record['timeout'])
            except TypeError:
                print("Die Zeituberschreitung ein Gleitkommazahlen sind muss!")
        else: timeout = 15

        if record['time'] and record['timerange']:
            print("Fehler, Du kannst nur von Zeit oder Zeitbereich benutz, Du kannst nicht gleichzeitig sie benutz!")
            quit()

        if record['timerange']:
            ranges = str(record['timerange']).split()
            timerange = {'time_min':ranges[0], 'time_max':ranges[1]}
            timerange = str(timerange).replace("'","\"")
        else: timerange = None
        if record['genaue'] and record['grosse']:
            parser.error("Du kannst nicht gleichzeitig die Genaue Grosse und Grosse benutz!")
        validated_vars = {'search_keyword': search_keyword, 'suffix':suffix_keywords, 'prefix':prefix, 'limit':limit, 'main_dir':main_dir, 'pause':pause, 'printURL':printURL, 'timeout':timeout, 'timerange':timerange, 'webseite':webseite}
        return validated_vars

    def download_over_limit(self, url):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        try:
            opt = Options()
            opt.add_argument('--headless=new')
            serv = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=serv, options=opt)
            driver.get(url)
            #Kefken azekptieren
            accept = driver.find_element(By.CSS_SELECTOR, 'button[jsname="b3VHJd"]')
            accept.click()
            for i in range(10):
                driver.execute_script("window.scrollBy(0, 10000)")
                time.sleep(0.5)
                i += 1
            try:
                show_more = driver.find_element(By.CSS_SELECTOR, "input[jsaction='Pmjnye']")
                show_more.click()
            except: 
                print('Keine mehrere Bildern hier!')
            rawPage = driver.page_source
            return rawPage
        except Exception as err:
            return 'Seite Nicht Gefunden'

    def download_page(self, url, timeout, mode=''):
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
                    page = 'Page Not Found'
                    return page
    def download_image(self, object, dir, count, timeout, URLprint, format=""):
        try: 
            url = object[1]['link']
        except KeyError:
            print('Ungultiges Objekt!')
            download_status = 'Versagen'
            download_message = 'Es tut mir leid aber wir diese Datei nicht benutzen kann'
            return object, download_status, download_message
        if URLprint == "yes":
            print("BILDER URL:",url)
        try:
            #Seite herunterladen
            data = self.download_page(url, timeout, mode='bytes')
            imgName = self._find_name(url)
            if data == 'Page Not Found':
                download_status = 'Versagen'
                download_message = "URL error in ein Bild, die nachsten versuchen..."
                return object, download_status, download_message
            if format == "":
                imgName = imgName + "-" + str(count) + "." + "jpg"
            else:
                imgName = imgName + "-" + str(count) + "." + format
            img_path, save_status = self._save_image(dir, data, imgName)
            #Die Gross und die Zeit definieren
            size = self._get_size(img_path)
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

            

    def _get_similar_images(self, url, n_Times, searches):
        url = url
        error_count = 0
        req = request.Request(url, headers=headers)
        response = request.urlopen(req, None, timeout=10, context=ctx)
        data = response.read().decode('utf-8')
        search_keyword = searches
        if url == 'Page Not Found':
            error_count += 1
            header = 'Keine Ahnliche Bildern gefunden'
            return header, search_keyword, error_count
        c = 0
        if n_Times > 12:
            n_Times = 12
        while c < n_Times:
            similarImage = True
            start_similar_images = data.find('<h2 class="OkhOw gadasb">')
            header = data[start_similar_images+25:data.find("</h2>", start_similar_images)]
            if start_similar_images == -1:
                print('Keine Ahnliche Bildern gefunden')
                break
            first_similar_image = True
            while similarImage and c < n_Times:
                if first_similar_image:
                    start_href = data.find('href="', start_similar_images)
                    first_similar_image = False
                else:
                    start_href = data.find('href="')
                end_href = data.find('"', start_href+9)
                href = data[start_href+9:end_href]
                end_a_tag = data.find('">', start_href)
                a_tag = data[start_href:end_a_tag]

                if 'class="mgK4fd"' not in a_tag:
                    similarImage = False
                else:
                    similarImage = True
                query_start = href.find('?q=')
                query_end = href.find('&amp;')
                query = href[query_start+3:query_end]
                data = data[end_href:]

                #Das query am unsere Schlusselwortliste hinzufugen
                search_keyword.append(unquote_plus(query))
                c += 1
        return header, search_keyword, error_count
    def _get_size(self, file_path):
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            size = file_info.st_size
            for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    return "3%.1f %s"%(size, x)
                size /= 1024.0

    def _get_next_item(self, rawPage, retrieved_links, limit):
        #Dieses Abfragen sind die Ziechenfolgen, nach denen wir suchen, um die Datei aus unseren Bildern zu extrahieren
        queries = {'link':[('<img data-src=', 'src="'), ('" data-ils', '"')],
                'title':['<h3 class="bytUYc">', '</h3>'],
                'height':['data-oh="','"'],
                'width':['data-ow="','"'],
                'site':['<div class="LAA3yd">','</div>']}
        img_link = None
        #Link finden
        while True:
            if img_link in retrieved_links:
                rawPage = rawPage[end_content:]
            start_line = rawPage.find('class="bRMDJf islir"')
            end_content = rawPage.find('</h3>', start_line)
            if start_line == -1:
                end_quote = 0
                img_object = "no_links"
                return img_object, end_quote, retrieved_links
            if limit <= 100:
                link_start = rawPage.find(queries['link'][0][0], start_line)
                link_end = rawPage.find(queries['link'][1][0],link_start+len(queries['link'][0][0]))
                img_link = str(rawPage[link_start+len(queries['link'][0][0])+1:link_end])
                if img_link not in retrieved_links:
                    break
            else:
                link_start = rawPage.find(queries['link'][0][1], start_line)
                link_end = rawPage.find(queries['link'][1][1],link_start+len(queries['link'][0][1]))
                img_link = str(rawPage[link_start+len(queries['link'][0][1]):link_end])
                if img_link not in retrieved_links:
                    break
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
        #Objekt erstellen
        img_object = (title[:16], {'link':img_link, 'width':width, 'height':height, 'title':title, 'site':site})
        retrieved_links.append(img_object[1]['link'])
        return img_object, end_content, retrieved_links
    def _get_all_items(self, page, directory, index, constructor):
        items = []
        retrieved = []
        count = 0
        success = 0
        error_count = 0
        searchName = directory.split('/')[-1]
        limit = constructor['limit']
        pause = constructor['pause']
        format = constructor['format']
        write = constructor['write']
        lautlos = constructor['lautlos']
        metadata = constructor['metadata']
        timeout = constructor['timeout']
        printURL = constructor['printURL']
        abpath = []
        if write:
            tuple = (index, searchName)
            self._write_txt(tuple, mode='item')
        if page == 'Page Not Found':
            error_count += 1
            return items, error_count
        while count < limit:
            item_object, end_content, retrieved = self._get_next_item(page, retrieved, limit)
            if item_object == 'no_links':
                print('no more links')
                break
            else:
                page = page[end_content:]
                item_object, download_status, download_message = self.download_image(item_object, directory, count+1, timeout, printURL, format)
                if download_status == 'Erfolg':
                    items.append(item_object)
                    if not lautlos:
                        print(download_message)
                    if metadata:
                        print("Bilder Metadatei:\n"+str(item_object))
                    if write:
                        self._write_txt(str(item_object))
                        if not lautlos:
                            print("Textdatei schreibt!")
                    abpath.append(item_object[1]['link'])
                    count += 1
                    success += 1
                else:
                    error_count += 1
                    if not lautlos:
                        print(download_message)
                time.sleep(pause)
        if success < limit:
            if not lautlos:
                print('Es tut mir leid, aber ' + str(success) + ' ist alles, dass wir fur dieses Seite haben!')
        return items, abpath, error_count

    def _find_search(self, url):
        start = url.find('q=')
        end = url.find("&tbm=")
        search_term = url[start+2:end]
        return search_term
    def _find_name(self, url):
        imgName = url[url.rfind('/')+1:]
        if '?' in imgName:
            imgName = imgName[:imgName.find('?')]
        #Extension entfernen
        imgName = imgName[:imgName.rfind('.')]
        imgName = imgName.replace(".", "-")
        imgName = unquote_plus(imgName)
        return imgName
    def _save_image(self, directory, data, imgName):
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

    def _url_bauen(self, constructor, mode=''):
        bauen = "&tbs="
        root = 'https://www.google.com/search?q='
        base = '&tbm=isch'
        if constructor['language']:
            lang = str(constructor['language'])
            param = {"Arabic":"ar","Chinese (Simplified)":"zh-CN","Chinese (Traditional)":"zh-TW","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Estonian":"et","Finnish":"fi","French":"fr","German":"de","Greek":"el","Hebrew":"iw ","Hungarian":"hu","Icelandic":"is","Italian":"it","Japanese":"ja","Korean":"ko","Latvian":"lv","Lithuanian":"lt","Norwegian":"no","Portuguese":"pt","Polish":"pl","Romanian":"ro","Russian":"ru","Spanish":"es","Swedish":"sv","Turkish":"tr"}
            language = '&hl=' + param[lang]
        else: language = '&hl=pt'
        closer = language+'&sa=X&ved=0CAIQpwVqFwoTCKDZgKG4qYADFQAAAAAdAAAAABAD&biw=1263&bih=648'
        params = {
            'color':[constructor['color'], {'red':'ic:specific,isc:red', 'orange':'ic:specific,isc:orange', 'yellow':'ic:specific,isc:yellow', 'green':'ic:specific,isc:green', 'teal':'ic:specific,isc:teel', 'blue':'ic:specific,isc:blue', 'purple':'ic:specific,isc:purple', 'pink':'ic:specific,isc:pink', 'white':'ic:specific,isc:white', 'gray':'ic:specific,isc:gray', 'black':'ic:specific,isc:black', 'brown':'ic:specific,isc:brown'}],
            'type':[constructor['type'], {'face':'itp:face','photo':'itp:photo','clip-art':'itp:clip-art','lineart':'itp:lineart','animated':'itp:animated'}],
            'format':[constructor['format'], {'jpg':'ift:jpg','gif':'ift:gif','png':'ift:png','bmp':'ift:bmp','svg':'ift:svg','webp':'webp','ico':'ift:ico'}],
            'grosse':[constructor['grosse'], {'large':'isz:l', 'medium':'isz:m', 'small':'isz:s', 'icon':'isz:i','>400*300':'isz:lt,islt:qsvga','>640*480':'isz:lt,islt:vga','>800*600':'isz:lt,islt:svga','>1024*768':'visz:lt,islt:xga','>2MP':'isz:lt,islt:2mp','>4MP':'isz:lt,islt:4mp','>6MP':'isz:lt,islt:6mp','>8MP':'isz:lt,islt:8mp','>10MP':'isz:lt,islt:10mp','>12MP':'isz:lt,islt:12mp','>15MP':'isz:lt,islt:15mp','>20MP':'isz:lt,islt:20mp','>40MP':'isz:lt,islt:40mp','>70MP':'isz:lt,islt:70mp'}], 
            'rechte':[constructor['rechte'], {'labeled-for-reuse-with-modifications':'sur:fmc', 'labeled-for-reuse':'sur:fc','labeled-for-noncommercial-reuse-with-modification':'sur:fm','labeled-for-nocommercial-reuse':'sur:f'}],
            'time':[constructor['time'], {'past-24-hours':'qdr:d','past-7-days':'qdr:w', 'past-1-year':'qdr:y'}],
            'color-type':[constructor['colortype'], {'full-color':'ic:color','black-and-white':'ic:gray', 'transparent':'ic:trans'}],
            'aspect_ratio':[constructor['aspekt'],{'tall':'iar:t','square':'iar:s','wide':'iar:w','panoramic':'iar:xw'}]
            }
        if constructor['genaue']:
            sizes = [x.strip() for x in constructor['genaue'].split(',')]
            grosseParam = ",isz:ex,iszw:"+sizes[0]+",iszh:"+sizes[1]
        else: grosseParam = ''

        
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
        if constructor['timerange']:
            js = json.loads(constructor['timerange'])
            zeitbereich = '&cdr:1,cd_min:' + js['time_min'] + ',cd_max:' + js['time_max']
        else: zeitbereich = ''

        if constructor['webseite']:
            url = root+constructor['search']+",site:"+constructor['webseite']+base+bauen+grosseParam+closer+zeitbereich
        else:
            url = root+constructor['search']+base+bauen+grosseParam+closer+zeitbereich
        if mode == 'normalize':
            url = root+constructor['search']+base+closer
        return url
    def _write_txt(self, data, mode='content'):
        if mode == 'item':
            with open('./links.txt', 'a', encoding='utf-8') as writer:
                writer.write(str(data[0])+":"+data[1]+" = \n\n")
        if mode == 'content':
            with open('./links.txt', 'a', encoding='utf-8') as writer:
                writer.write(data +"\n\n\n")
    def _create_dir(self, *directories):
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
    def _set_name(self, dir, record):
        worked_name = dir
        desired_args = ['color','type','gross','rechte','time','format','colortype','aspekt','webseite']
        values = [i for i in record.values() if i in desired_args and i is not None]
        for value in values:
            #Ausschielssen der Domain aus dem Webseite-Namen
            if "." in value:
                value = value[:value.find('.')]
            worked_name += " - " + value
        return worked_name

    def _single_image_download(self, record, vars):
        t0 = time.time()
        url = record['single']
        main_dir = vars['main_dir']
        timeout = vars['timeout']
        format = record['format']
        try:
            imgData = self.download_page(url, timeout, mode='bytes')
        except HTTPError:
            print("HTTP Fehler!")
            t1 = time.time()
            total_time = t1 - t0
            download_status = "Fehler!"
            return total_time, download_status
        except URLError:
            print("URL Fehler!")
            t1 = time.time()
            total_time = t1 - t0
            download_status = "Fehler!"
            return total_time, download_status
        except IOError:
            print("IO Fehler!")
            t1 = time.time()
            total_time = t1 - t0
            download_status = "Fehler!"
            return total_time, download_status
        if format:
            imgName = self._find_name(url)+'.'+str(format)
        else:
            imgName = self._find_name(url)+'.jpg'
        directory = self._create_dir(main_dir)
        target_dir, download_status = self._save_image(directory, data=imgData, imgName=imgName)


        t1 = time.time()
        total_time = t1 - t0

        return total_time, download_status

    def download(self, record, vars):
        search_keyword = vars['search_keyword']
        suffix_keywords = vars['suffix']
        prefix = vars['prefix']
        main_dir = vars['main_dir']
        printURL = vars['printURL']
        webseite = vars['webseite']
        limit = vars['limit']
        pause = vars['pause']
        timerange = vars['timerange']
        timeout = vars['timeout']
        format = (record['format'] if record['format'] else '')
        write = record['write']
        lautlos = record['lautlos']
        metadata = record['metadata']
        genaue = record['genaue']
        abpaths = {}

        t0 = time.time()
        total_errors = 0
        error_count = 0
        if record['url']:
            search = self._find_search(record['url'])
            search_keyword.append(search)
            url = record['url']
            if record['ahnlich']:
                header, search_keyword, errors = self._get_similar_images(record['language'], record['ahnlich'], search_keyword)
                if errors > 0:
                    error_count += 1
        if record['prefix']:
            prefixed_words = [str(j) + " " + str(i) for i in search_keyword for j in prefix]
            for i in prefixed_words:
                search_keyword.append(i)
        for suffix in suffix_keywords:
            i = 0 
            while i < len(search_keyword):
                rootword = search_keyword[i].strip()
                word = rootword + " " + suffix
                iteration = "\nSuchen nu.:" + str(i+1) + " / / == > " + word
                if not record['lautlos']:
                    print(iteration+"\n"+"Auswertend...")
                dir_name = self._set_name(word, record)
                directory = self._create_dir(main_dir, dir_name).strip()
                if record['url'] is None or i > 0:
                    bauen = record
                    bauen['timerange'] = timerange
                    bauen['search'] = quote(word)
                    bauen['genaue'] = genaue
                    url = self._url_bauen(bauen)
                if limit <= 100:
                    page = self.download_page(url, timeout=timeout)
                else: 
                    page = self.download_over_limit(url)
                #Die Sucheliste zu vermehren
                if page != 'Page Not Found':
                    if record['ahnlich'] and i == 0:
                        url = self._url_bauen(bauen, mode='normalize')
                        header, search_keyword, errors = self._get_similar_images(url, record['ahnlich'], search_keyword)
                        if errors > 0:
                            error_count += 1
                        if not record['lautlos']:
                            print(header, search_keyword.pop(0))
                    i += 1
                    constructor = {'limit':limit, 'pause':pause, 'format':format, 'write':write, 'lautlos':lautlos, 'metadata':metadata, 'timeout':timeout, 'printURL':printURL}
                    items, abpath, error_count = self._get_all_items(page, directory, i, constructor)
                    if record['abpath']: abpaths[word] = abpath
                    if record['auszug']:
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
                            if not record['lautlos']:
                                print('JSONDatei erstellen!')
                        else: print("Leereres Datei, wir kann keine JSON schreiben!")
                else: 
                    error_count += 1
                total_errors += error_count
        t1 = time.time() 
        total_time = t1 - t0
        return total_time, total_errors, abpaths
    
    def make_arguments(self, dictionary):
        args_list = ["keywords","extract","suffix","prefix","limit","format","url","single","output","pause","color","colortype","rechte","grosse","type","time","timerange","aspekt","ahnlich","webseite","print","metadata","auszug","timeout","language", "lautlos", "write", "genaue", "abpath"]
        if __name__ != '__main__':
            record = {}
            for i in args_list:
                if i not in dictionary:
                    record[i] = None
                else:
                    record[i] = dictionary[i]
            variables = self._validate_parameters(record)
            return record, variables
# ======================= Alle Funktionen initialisierten =================================

def user_input():
    config = argparse.ArgumentParser()
    config.add_argument('-cf', '--config_file', help='config file name', default='', type=str, required=False)
    config.add_argument('-k', '--keywords', help='Delimited keywords for searching images', required=False)
    config.add_argument('-ek', '--extract', help='Worten, aus ein Datei oder Ahnlich erhalten!', required=False)
    config.add_argument('-sk', '--suffix', help='suffix keywords for searching more related images, kannst du auch Zufallprinzip auswahlen, um mit einigen Vorschalgen, die wir fur sie haben nachzusehen!', required=False)
    config.add_argument('-l', '--limit', help='Delimited list input', required=False)
    config.add_argument('-co', '--color', help='Filtering by color', required=False, choices=[
        'red','yellow','blue','orange','violet','green','brown','white','black','gray','pink','teel','purple', 'brown'])
    config.add_argument('-ct', '--colortype', help='Filtern nach Farbenart', required=False, choices=['full-color', 'black-and-white', 'transparent'])
    config.add_argument('-u', '--url', help='Die Bildern nach Benutzerurl herunterladen werden', required=False)
    config.add_argument('-o', '--output', help='Entmoglich dir, den Name von Ausgeben zu auswahlen', required=False, type=str)
    config.add_argument('-s', '--single', help='Macht es moglich, ein einzelnes Bilder zu herunterladen', required=False, type=str)
    config.add_argument('-p', '--pause', help='Bezeicht die Zeit, dass wir warten wird zwischen Bildern', required=False, type=int)
    config.add_argument('-g', '--grosse', help='Sagt Sie, wie Grosse den Bildern sollen sind', required=False, choices=['large','medium','icon','>400*300','>640*480','>800*600','>1024*768','>2MP','>4MP','>6MP','>8MP','>10MP','>12MP','>15MP','>20MP','>40MP','>70MP'])
    config.add_argument('-t', '--type', help='Bezeicht die Typ oder Art von Bildern dass wir finden wird', required=False, choices=['face','photo','clip-art','lineart','animated'])
    config.add_argument('-z', '--time', help='Bezeicht die Zeit, in dass den Bildern hochgeladen wurden', required=False, choices=['past-24-hours','past-7-days','past-1-month','past-1-year'])
    config.add_argument('-r', '--rechte', help='Wahlen Sie der Benutzbedingungen dieses Bildern', required=False, type=str, choices=['labeled-for-reuse-with-modifications','labeled-for-reuse','labeled-for-noncommercial-reuse-with-modification','labeled-for-nocommercial-reuse'])
    config.add_argument('-f', '--format', help='Wahlen Sie der Format der Verwendung dieses Bildern', required=False, type=str, choices=['svg', 'gif', 'jpg', 'png', 'jpeg', 'tbn', 'ico', 'webp', 'bmp'])
    config.add_argument('-a', '--ahnlich', help='Geben Sie an, ob Sie nach ahnlichen Bildern suchen mochte', required=False, type=int)
    config.add_argument('-ar', '--aspekt', help='Geben Sie an, die Ratioaspekt den Bildern aus', required=False, type=str, choices=['tall', 'wide', 'panoramic', 'square'])
    config.add_argument('-w', '--webseite', help='Geben Sie an, die Webseite vor den die Bildern herunterladen werden sollen', required=False, type=str)
    config.add_argument('-to', '--timeout', help='Geben Sie an, die Zeit die wir fur an Antwort von der System warten sollen')
    config.add_argument('-pr', '--print', help="Zeichen Sie die URL von der gegeben Bildern!", default=False, action="store_true")
    config.add_argument('-sc', '--write', help="Auswahlen sie, ob ein Textdatei zu erstellen oder nicht", default=False, action="store_true")
    config.add_argument('-m', '--metadata', help="Geben Sie an, ob das Metadatei den Bildern zu gezeigt oder nicht", default=False, action="store_true")
    config.add_argument('-au', '--auszug', help="Auswahlen Sie an, ob das Metadatei den Bildern zu auszugen oder nicht", default=False, action="store_true")
    config.add_argument('-lm', '--lautlos', help="Aktivieren dieses Lautlos-Modus, um die Programm ohne Nachrichten zu laufen!", default=False, action="store_true")
    config.add_argument('-pre', '--prefix', help="Geben Sie ein Prafix an, dass an der Beginnen von jedem Suchen hinzugefugt werden!, kannst du es auch zufallig auswahlen!", type=str)
    config.add_argument('-la', '--language', help="Auswahlen in welche Sprache mochtest Du die Suchergebnisse erhalten!", choices=['Arabic','Chinese (Simplified)','Chinese (Traditional)','Czech','Danish','Dutch','English','Estonian','Finnish','French','German','Greek','Hebrew','Hungarian','Icelandic','Italian','Japanese','Korean','Latvian','Lithuanian','Norwegian','Portuguese','Polish','Romanian','Russian','Spanish','Swedish','Turkish'], type=str)
    config.add_argument('-zb', '--timerange', help="Geben Sie die Zeitbereich an, inzwischen unseres Bilder hochgeladen wurden, format {'time_min':'MM/DD/YYYY','time_min':'MM/DD/YYYY'}'")
    config.add_argument('-ge', '--genaue', help="Geben Sie die Genaue Grosse, dass du die Bildern erhalten mochtest", type=str, required=False)
    config.add_argument('-ap', '--abpath', help="Auswahlen Sie, ob dass die Linken des Bildern erhalten mochtest", required=False, action="store_true")
    config_file_check = config.parse_known_args()
    object_check = vars(config_file_check[0])
    records = []
    #Argumente von Configdatei ausshalten
    if object_check['config_file'] != '':
        args_list = ["keywords","extract","suffix","prefix","limit","format","url","single","output","pause","color","colortype","rechte","grosse","type","time","timerange","aspekt","ahnlich","webseite","print","metadata","auszug","timeout","language", "lautlos", "write","genaue", "abpath"]
        json_file = json.load(open(config_file_check[0].config_file))
        for record in range(0,len(json_file['Records'])):
            arguments = {}
            for i in args_list:
                arguments[i] = None
            for key, value in json_file['Records'][record].items():
                arguments[key] = value
    #Argumente von Benutzerfernster auszugen
    else:    
        args = config.parse_args()
        arguments = vars(args)

    records.append(arguments)
    records_count = len(records)
    return records          


    #     /////////////////  Hauptteil des Programm  /////////////////

def main():
    records = user_input()
    for i in range(len(records)):
        if records[i]['single']:
            downloader = googleimagesdownload()
            variables = downloader._validate_parameters(records[i])
            print('Dateisuch nummer: ', str(i+1))
            total_time, download_status = downloader._single_image_download(records[i], variables)
            if not records[i]['lautlos']:
                print('Aufgewendet Gesamtzeit: ' + str(total_time) + "\nHerunterladungstatus: " + download_status)
        else:
            downloader = googleimagesdownload()
            variables = downloader._validate_parameters(records[i])
            print('Dateisuch nummer: ', str(i+1))
            total_time, total_errors = downloader.download(records[i], variables)
            if not records[i]['lautlos']:
                print('Aufgewendet Gesamtzeit: ' + str(total_time) + "\Fehler: " + str(total_errors))
    
if __name__ == '__main__':
    main()


