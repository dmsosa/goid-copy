# :sunrise: Google Images Downloader

Allereste Readme.MD fur dieses Repo.

Lassen wir von anderen inspirieren.

Das ist eine Kopie des Codes, dessen Autor hadikvasa ist, ich empfehle ihn
wirklich, weil ich im Moment sein Repo verwende, um Programmieren zu lernen.

## Zusammenfassung

Dies ist ein Kopie, die Python Programms um nach Schlusselworten in Google Bilder zu suchen und dann optional auch alle Bilder herunterzuladen


## Compatibility

Dieses Kopie in Python 3.11.0 geschreiben ist und kann auf jeder Version von Python 3.X ausgefuhrt weden. Es handelt sich um ein Download-and-Run-Programm mit einigen Anderungen je nachdem, auf welchem Gerat Sie die App verwenden.


Dieses Kopie in Python 3.11.0 geschreiben ist und kann auf jeder Version von Python 3.X ausgefuhrt weden. Es handelt sich um ein Download-and-Run-Programm mit einigen Anderungen je nachdem, auf welchem Gerat Sie die App verwenden.
Dieses Kopie in Python 3.11.0 geschreiben ist und kann auf jeder Version von Python 3.X ausgefuhrt weden. Es handelt sich um ein Download-and-Run-Programm mit einigen Anderungen je nachdem, auf welchem Gerat Sie die App verwenden.


--- 
## Installation

**pip benutzen**

```

$ pip install goidcopy

```

**Manuell**

```

$ git clone https://github.com/duvilearning/goidcopy.git

$ cd goidcopy && sudo py setup.py install


```

## Wie kann mann dieses Script benutz?

1. Dieses Repo an dein lokale Festplatte herunterladen
2. Offnen Sie das Terminal (fur Mac/Linux Betriebssysteme) oder die Eingabeaufforderung (fur Windows-Betriebssysteme) und navigieren Sie zum Speicherort der Datei "google-images-download.py" auf Ihrer lokalen Festplatte.
3. Geben Sie einen der folgenden Befehle ein

### Verwerdung
---
`py my.py [Argumente...]`


| Argument | Abkurzung | Beschreibung |
| --- | :---: | --- |
| **keywords** | k | Gibt die Worter an, nach denen Sie suchen mochten. <br> Tips: <br> * Wenn du einfach die Wort schreibst, wird Google am besten versuchen, es abzugleichen <br> * Wenn Sie nach einer genaue Phrase suchen mochten, konnen Sie die Wort in doppelte Anfuhrungszeichen ("") setzen <br> * Wenn Sie dein suchen um eines der angegebenen Worter abzugleichen mochtest, schreibt Sie *OR* zwischen den Wortern. <br> * Wenn sie ein bestimmtest Wort explizit nicht mochten, schreibt Sie ein Minuszeichen (-) von dem Wort. |
| **suffix** | sk | Geben Sie zusatzliche Nachsilben, um noch mehr Bildern zu erhalten. Es ist nutzlich, wenn sie zum verwandten Ergebnisse suchen mochtest. <br> Die endgultige Suchanfrage wurde wie folgt aussehen: "<keyword> <suffix keyword>"
| **limit** | l | Bezeicht die Bildernnummer, die du erhalten mochtest |
| **color** | c | Bezeicht die Farbe, an die die Bilderergebnisse erhalten mochte <br> Mogliche Werte: red, blue, yellow, green, orange, pink, violet, teal, black, white, gray |
| **url** | u | Mit diese, kann man die spezielle URL von den Bildern herunterladen werden |
| **single** | s | Ermoglicht dir, ein einzelnes Bilder nach dem gegeben URL herunterladen |
| **pause** | p | Ermoglicht dir, ein Zeitspanne zu geben, um jeden herunter zu erwarten |
| **output** | o | Auswahlen Sie die Ort, wo die Bildern speichern werden |
| **type** | t | Entdecken Sie, welches Types die Bildern sind! |
| **time** | z | Ermoglicht dir, ein Zeitspanne zu geben, um jeden herunter zu erwarten |
| **rechte** | r | Erkennen Sie, wer die rechten von jeden Bildern habe! <br> Mogliche Ergegnisse:  labled-for-reuse-with-modifications, labled-for-reuse, labled-for-noncommercial-reuse-with-modification, labled-for-nocommercial-reuse |
| **grosse** | g | Schaust Du, wie grosse die Bildern sind <br> Mogliche Ergegnisse:  small, medium, large, icon |

**Anmerkung** Wenn es gibt kein `url` oder `single` Argument, nur die Keywordsfeld ist obligatorisch. Keine andere Argumente obligatorisch ist.

## Beispiele

Wenn Sie python 2.X installieren hast

`python google-images-download.py --keywords "Polar bears, baloons, Beaches" --limit 20`

Wenn Sie python 3.X installieren hast

`python3 google-images-download.py --keywords "Polar bears, baloons, Beaches" --limit 20`

Um die Abkurzung zu benutz

`python google-images-download.py -k "Polar bears, baloons, Beaches" -l 20`

Um die Farbe oder Zeichnungfilter zu benutz

`python google-images-download.py -k "playground" -l 20 -c red`

* Um Bildern mit Typ und Grosse Merkmalen herunterladen

`python google-images-download.py --keywords "baloons" --grosse medium --type animated`

* Um Bildern mit Verwendungrechten zu herunter

`python google-images-download.py --keywords "universe" --rechte labled-for-reuse`

===> Die Bildern in ihren eigenen Verzeichnissen im selben Ort wie die Pythondatei heruntergeladen werden

---
>>>>>>> topic

## SSLFehler

Wenn Sie SSL-Fehler auf dem Mac für Python 3 sehen, gehen Sie bitte zum Finder —> Anwendungen —> Python 3 —> Klicken Sie auf den Befehl "Zertifikate installieren" und führen Sie die Datei aus.


## Beitragen oder Arbeiten Sie mit uns zusammen

Jeder ist herzlich eingeladen, zu diesem Script beizutragen. Wenn Sie eine Anderung vornehmen mochten, offnen Sie einen Pullrequest. Fur Probleme und Diskussionen besuchen Sie den Issue Tracker *link*

## :exclamation: Verzichtserklarung :exclamation:

Dieses Programm entmoglicht dich hundert, vielleicht tausend Bildern von Google zu herunterladen. Bitte bedank dich nicht dass ich alle diese grosse Absatz kopieren werde. Danke Sehr! 



/Duvi/

