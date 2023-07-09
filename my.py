#///////////////// Programm zu starten /////////////////

#die notwendig Modulen zu importieren

from urllib import request, response, error, parse #Urllib Library fur die Request machen
import time #Wie mochten es wissen, wie lang unsere Programm zu beenden annehmen
import sys #Sys Library zu importieren

search_keyword = ['bola', 'aufmerksamkeit']
keywords = ['', ' high quality', ' in real life', ' how to draw']

def download_page(url):
        version = (3,0)
        current_version = sys.version_info
        if current_version >= version:
            try:
                headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                }
                req = request.Request(url, headers=headers)
                resp = request.urlopen(req)
                rawPage = str(resp.read())
                return rawPage
            except Exception as err:
                print(err)
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_di"')
        start_content = s.find('imgurl=',start_line+1)
        end_content = s.find('&amp;',start_content+1)
        content_raw = str(s[start_content+7:end_content])
        return content_raw, end_content
def _images_get_all_images(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == 'no links':
             break
        else:
            items.append(item)
        #Alle die Items in dem List "Links" bekannt zu hinzufugen
            time.sleep(1)
        #Timer konnte verwendet werden, um den Anfrage fur das Herunterladen von Bildern zu verlangsamen
            page = page[end_content:]
        return items

#Die tatsache programm

t0 = time.time()

i = 0
while i < len(search_keyword):
    items = list()
    iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
    print (iteration)
    search_keywords = search_keyword[i]
    search = search_keywords.replace(' ', '%20')
    j = 0 
    while j < len(keywords):
        root = 'https://www.google.com/search?q='
        base = '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        coded_keyword = keywords[j].replace(' ', '%20')
        url = root + search + keywords[j] + '' + base
        page = download_page(url)
        items = items + _images_get_all_images(page)
        j += 1
        print ("Image Links = "+str(items))
        print ("Total Image Links = "+str(len(items)))
        print ("\n")
        i = i+1

        #Mit die nachsten Codezeilen konnen Sie alle Links in am neues .txt Datei schreiben, denn wird an die selber verzeichnis wie Ihr Code erstellt. Sie konnen die folgende 3 Zeilen auskommentieren, um keine Datei zu schreiben 

        #Links.txt zu erstellen
        info = open('./links.txt', 'a', encoding='utf-8')
        #Dem Datei schreiben
        info.write(str(i)+": "
                   +str(search_keyword[i-1])+": \n"+
                   str(items)+"\n\n\n")
        #Dem Datei zu schliessen
        info.close()
        
        t1 = time.time() 

        total_time = t1 - t0 # Berechnung die Gesamtzeit, die benotig wird, um alle links von 60.000 Bilder zu crawlen, zu finden und herunterzuladen

        print("Gesamtzeitaufwand: "+ str(total_time)+ " Sekunden")

# /////////////////  Ende des Programm  /////////////////


