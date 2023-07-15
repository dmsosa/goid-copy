# In[ ]:
# -*- coding: utf-8 -*-

#///////////////// Programm zu starten /////////////////

#die notwendig Modulen zu importieren

import time, datetime #Wie mochten es wissen, wie lang unsere Programm zu beenden annehmen
import sys, os, ssl #Sys und os Library zu importieren
from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import quote
import argparse

sys.stdout.reconfigure(encoding='utf-8')
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keywords', help='Delimited keywords for searching images', required=False)
parser.add_argument('-l', '--limit', help='Delimited list input', required=False)
parser.add_argument('-d', '--draw', help='Filtering by draw', required=False, const=True, action='store_const')
parser.add_argument('-c', '--color', help='Filtering by color', required=False, choices=[
    'red','yellow','blue','orange','violet','green','brown','white','black','gray','pink','teal','purple'
])
parser.add_argument('-u', '--url', help='Die Bildern nach Benutzerurl herunterladen werden', required=False, type=str)
parser.add_argument('-o', '--output', help='Entmoglich dir, den Name von Ausgeben zu auswahlen', required=False, type=str)
parser.add_argument('-s', '--single', help='Macht es moglich, ein einzelnes Bilder zu herunterladen', required=False, type=str)
parser.add_argument('-p', '--pause', help='Bezeicht die Zeit, dass wir warten wird zwischen Bildern', required=False, type=str)

args = parser.parse_args()



if (args.keywords is None) and (args.url is None) and (args.single is None):
    parser.error('Keywordsargument obligatorisch ist!')

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
#Globalen Variablen initialisieren
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
ctx = ssl._create_unverified_context()

def download_page(url):
        version = (3,0)
        current_version = sys.version_info
        if current_version >= version:
            
            try:
                headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
                req = request.Request(url, headers=headers)

                try:
                    resp = request.urlopen(req,data=None, timeout=10)
                except:
                    resp = request.urlopen(req,data=None, timeout=10, context=ctx)

                rawPage = str(resp.read())
                return rawPage
            except Exception as err:
                print(err)
def _images_get_next_item(s):
    start_line = s.find('<img data-src=')
    if start_line == -1:
        end_quote = 0
        link = "no links"
        return link, end_quote
    else:
        # start_line = s.find('<img data-src=')
        # start_content = s.find('imgurl=',start_line+1)
        end_content = s.find('" data-ils',start_line+15)
        content_raw = str(s[start_line+15:end_content])
        return content_raw, end_content
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

#Die tatsache programm

t0 = time.time()

if args.single:
    url = args.single
    try:
        os.makedirs(main_dir)
    except OSError as e:
        if e.errno != 17:
            raise
        pass
    try:
        req = request.Request(url, headers=headers)
        response = request.urlopen(req, None, timeout=10, context=ctx)
        imgName = url[(url.rfind('/')+1):]
    except HTTPError:
        print("HTTP Fehler!")
    except URLError:
        print("URL Fehler!")
    except IOError:
        print("IO Fehler!")

    if '?' in imgName:
        imgName = imgName[:(imgName.find('?'))]
    if ('.jpg' in imgName) or ('.jpeg' in imgName) or ('.png' in imgName) or ('.svg' in imgName) or ('.tbn' in imgName):
        imgOutput = imgName
    else:
        imgOutput = imgName + ".jpg"
    with open(main_dir+imgOutput, 'wb') as saver:
        data = response.read()
        saver.write(data)

    t1 = time.time()
    total_time = t1 - t0

    print("Bilder erfolgreich gespeichert! =====> "+imgOutput)
    print("Programm Erfullt in "+str(total_time)+" Sekunden")
    quit()
else:
    
    i = 0

    root = 'https://www.google.com/search?q='
    base = '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
    color_param = ('&tbs=ic:specific,isc:'+str(args.color) if args.color else '')
    draw_param = ('&tbs=ic:gray,itp:lineart' if args.draw else '')

    if args.url:
        search_keyword = str(datetime.datetime.now()).split('.')[0].split()[0]
    else:
        search_keyword = [str(i) for i in args.keywords.split(',')]

    while i < len(search_keyword):
        items = list()
        if args.url:
            url = args.url
            dir_name = search_keyword + (" - " + str(args.color) if args.color else '')
            sub_directory = os.path.join(main_dir, dir_name)
            try:
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)
            except OSError as e:
                if e.errno != 17:
                    raise
            pass
            try:
                req = request.Request(url, headers=headers)
                response = request.urlopen(req, timeout=10, context=ctx)
                data = response.read()
                imgName = url[url.rfind('/')+1:]
                if '?' in imgName:
                    imgName = imgName[:(imgName.find('?'))]
                if ('.jpg' in imgName) or ('.jpeg' in imgName) or ('.png' in imgName) or ('.svg' in imgName) or ('.tbn' in imgName):
                    imgOutput = imgName
                else:
                    imgOutput = imgName + ".jpg"
                
                saver = open(os.path.join(sub_directory,imgOutput), "wb")
                saver.write(data)
                saver.close()
                t1 = time.time()
                total_time = t1 - t0
                print("Bilder erfolglich gespeichern! ===> "+imgName+"\nProgramm erfullt in "+str(total_time)+" Sekunden")
                quit()
            except HTTPError:
                print('HTTP Fehler!')
                quit()
            except URLError:
                print('HTTP Fehler!')
                quit()
            except IOError:
                print('HTTP Fehler!')
                quit()
                
            

        else: 
            iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
            print (iteration)
            with open('./links.txt', 'a', encoding='utf-8') as info:
                info.write(str(i+1)+": "+str(search_keyword[i])+"\n")
            search_keywords = search_keyword[i]
            search = quote(search_keywords)
            dir_name = search_keywords + (" - " + str(args.color) if args.color else '')
            sub_directory = os.path.join(main_dir, dir_name)
            try:
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)
            except OSError as e:
                if e.errno != 17:
                    raise
            pass
            url = root + search + base + color_param + draw_param
        page = download_page(url)
        time.sleep(0.05)
        items = items + _images_get_all_images(page)


        print ("Image Links = "+str(items))
        print ("Total Image Links = "+str(len(items)))
        print ("\n")
        #Mit die nachsten Codezeilen konnen Sie alle Links in am neues .txt Datei schreiben, denn wird an die selber verzeichnis wie Ihr Code erstellt. Sie konnen die folgende 3 Zeilen auskommentieren, um keine Datei zu schreiben 

        #Links.txt zu erstellen
        
        #Dem Datei schreiben
        with open('./links.txt', 'a', encoding='utf-8') as info:
            info.write(str(items)+"\n\n\n")
        #Dem Datei zu schliessen
        i += 1

        t1 = time.time() 

        total_time = t1 - t0 # Berechnung die Gesamtzeit, die benotig wird, um alle links von 60.000 Bilder zu crawlen, zu finden und herunterzuladen

        print("Gesamtzeitaufwand: "+ str(total_time)+ " Sekunden")

    #Bildern speichern
        k = 0
        errors = 0
    


        while k < len(items):
            try:
                req = request.Request(items[k], headers=headers)
                response = request.urlopen(req, timeout=10, context=ctx)
                data = response.read()

                saver = open(os.path.join(sub_directory,str(k+1)+".jpg"), "wb")
                saver.write(data)
                saver.close()
                print("Bild "+str(k+1)+" gespeichert")
                k += 1
            except HTTPError:
                print('HTTP Error in Bild: '+str(k+1))
                errors += 1
                k += 1
            except URLError:
                print('URL Error in Bild: '+str(k+1))
                errors += 1
                k += 1
            # except IOError:
            #     print('IO Error in Bild: '+str(k+1))
            #     errors += 1
            #     k += 1
        print("\nAlle "+str(k+1)+" Bildern gespeichert fur "+search_keywords+", Bruder!\nFehleranzahl ===> "+str(errors))

    #     /////////////////  Ende des Programm  /////////////////



# %%
