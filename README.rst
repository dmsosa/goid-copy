Google Images Download
######################

Python Script for 'searching' and 'downloading' hundreds of Google images to the local hard disk!

Summary
=======

This is a command line python program to search keywords/key-phrases on Google Images
and then also optionally download one or more images to your computer.
This is a small program which is ready-to-run, but still under development.
Many more features will be added to it going forward.

Wenn du mehrere als 100 hundert Bildern herunterladen mochtest, solltest du die ``Selenium`` Modul zusammen mit ``geckodriver`` installieren.

**(Tatsatlich dieses Programm wirkst ohne kein geckodriver)**

Kompatibilitat
==============

This program is compatible with both the versions of python (2.x and 3.x).
It is a download-and-run program with no changes to the file.
You will just have to specify parameters through the command line.

Installation
============

**Using pip:**

.. code-block:: bash

    $ pip install google_images_download

**Manually:**

.. code-block:: bash

    $ git clone https://github.com/hardikvasa/google-images-download.git
    $ cd google-images-download && sudo python setup.py install

Verwegung
=========

.. code-block:: bash

    $ googleimagesdownload [Arguments...]
 

Arguments
~~~~~~~~~

+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| Argument         | Short hand  | Description                                                                                                                   |
+==================+=============+===============================================================================================================================+
| keywords         | k           | Denotes the keywords/key phrases you want to search for and the directory file name.                                          |
|                  |             | Tips:                                                                                                                         |
|                  |             | * If you simply type the keyword, Google will best try to match it                                                            |
|                  |             | * If you want to search for exact phrase, you can wrap the keywords in double quotes ("")                                     |
|                  |             | * If you want to search to contain either of the words provided, use **OR** between the words.                                |
|                  |             | * If you want to explicitly not want a specific word use a minus sign before the word (-)                                     |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| suffix_keywords  | sk          | Denotes additional words added after main keyword while making the search query.                                              |
|                  |             | Useful when you have multiple suffix keywords for one keyword.                                                                |
|                  |             | The final search query would be: <keyword> <suffix keyword> dass heisst, wenn du "Hund" als Schlusswort and "Rot, Klein, Niedlich" als Nachsilben gegeben hast, das Programm um "Hund Rot, Hund Klein, und Hund Niedlich" individuell suchen wird                                                                  |
+------------------+-------------+-----------------------------------------------+
| prefix           | pre         | Prafixen, der an der beginnen jeden Wortes hinzugefugt wird, um mehrere Ergebnisse zu erhalten!                              |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| limit            | l           | Denotes number of images that you want to download. Das Programm wird es versuch, um alle Mogliche Bildern in einem Googleseite herunterladen, wenn es kein angegeben wert hast, die limitzahl 100 als Standartwert geben wird.                                                              |
+------------------+-------------+-----------------------------------------------+
| language         | la          | Auswahlen Sie in welches Sprache, die Ergebnisse erhalten mochte!                                                            |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| format           | f           | Denotes the format/extension that you want to download.                                                                       |
|                  |             | `Possible values: jpg, gif, png, bmp, svg, webp, ico`                                                                         |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| color            | c           | Denotes the color filter that you want to apply to the images.                                                                |
|                  |             | `Possible values:                                                                                                             |
|                  |             | red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown`                                              |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| color_type       | ct          | Denotes the color type you want to apply to the images.                                                                       |
|                  |             | `Possible values: full-color, black-and-white, transparent`                                                                   |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| usage_rights     | r           | Denotes the usage rights/licence under which the image is classified.                                                         |
|                  |             | `Possible values:                                                                                                             |
|                  |             | * labeled-for-reuse-with-modifications,                                                                                        |
|                  |             | * labeled-for-reuse,                                                                                                           |
|                  |             | * labeled-for-noncommercial-reuse-with-modification,                                                                           |
|                  |             | * labeled-for-nocommercial-reuse`                                                                                              |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| size             | s           | Denotes the relative size of the image to be downloaded.                                                                      |
|                  |             | `Possible values: large, medium, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP,`               |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| aspect_ratio     | a           | Denotes the aspect ration of images to download.                                                                              |
|                  |             | `Possible values: tall, square, wide, panoramic`                                                                              |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| type             | t           | Denotes the type of image to be downloaded.                                                                                   |
|                  |             | `Possible values: face,photo,clip-art,line-drawing,animated`                                                                  |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| time             | w           | Denotes the time the image was uploaded/indexed.                                                                              |
|                  |             | `Possible values: past-24-hours, past-7-days`                                                                                 |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| delay            | d           | Time to wait between downloading two images                                                                                   |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| url              | u           | Allows you search by image. It downloads images from the google images link provided                                          |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| single_image     | x           | Allows you to download one image if the complete URL of the image is provided                                                 |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| output_directory | o           | Allows you specify the main directory name. If not specified, it will default to 'downloads'                                  |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| similar_images   | si          | Reverse Image Search.                                                                                                         |
|                  |             | Searches and downloads images that are similar to the image link/url you provide.                                             |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| specific_site    | ss          | Allows you to download images with keywords only from a specific website/domain name you mention as indexed in Google Images. |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| print_urls       | p           | Print the URLs of the imageson the console. These image URLs can be used for debugging purposes                               |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| help             | h           | show the help message regarding the usage of the above arguments                                                              |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| lautlos           | lm          | Mit diese Funktionalitat, kannst du das Programm ohne Nachrichten laufen!                                                     |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| auszug           | au          | Aktivieren sie dieses Argumente, um ein JSONDatei mit der Datei den Bildern zu erstellen!                                     |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| schreibt         | sc          | Wenn du dieses Argumente geben, ein .txtdatet automatische erstellt wurde                                                     |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| pause            | p           | Geben Sie die Zeit an, die wir in zwischen jeden Anfrage wir warten sollen!                                                   |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| timeout          | to          | Geben sie die Zeit an, die wir fur jeden einzelnes socketantwort warten sollen                                                |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| extract          | ek          | Auszugen Sie, der Schlusselworten aus einer Datei oder ahnliche!                                                            |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| metadatei        | mt          | Auswahlen Sie, ob die Metadatei von der Bildern an die Fernster zu schauen                                                  |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| extract_datei    | ed          | Aktivieren Sie diese Funktion, um die Schlusselworten herauszeugen                                                          |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| sprache          | la          | Jetzt hast du die Auswahl, um in welches Sprache die Ergebnisse erhalten!                                                   |
|                  |             |                                             |
|                  |             | `Moglichen Werten: Arabic, Chinese (Vereinfacht, und viel mehrere Sprachen)`                                                |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| genaue           | ge          | Geben Sie an, die genaue Grosses der Bildern dass du erhalten mochtest                                                      |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| verschiebung     | of          | Geben Sie an, die genaue Grosses der Bildern dass du erhalten mochtest                                                      |
+------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+
| config_file       | cf          | You can pass the arguments inside a config file. This is an alternative to passing arguments on the command line directly.    |
|                   |             |                                                                                                                               |
|                   |             | Please refer to the                                                                                                           |
|                   |             | `config file format <https://github.com/hardikvasa/google-images-download/blob/master/README.rst#config-file-format>`__ below |
|                   |             |                                                                                                                               |
|                   |             | * If 'config_file' argument is present, the program will use the config file and command line arguments will be discarded     |
|                   |             | * Config file can only be in **JSON** format                                                                                  |
|                   |             | * Please refrain from passing invalid arguments from config file. Refer to the below arguments list                           |
+-------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------+

**Note:** If ``single_image`` or ``url`` parameter is not present, then keywords is a mandatory parameter. No other parameters are mandatory.


Examples
--------

Wenn du JSON Format benutzen mochtest:

Config File Format
==================

You can either pass the arguments directly from the command as in the examples below or you can pass it through a config file. Below is a sample of how a config
file looks.

You can pass more than one record through a config file. The below sample consist of two set of records. The code will iterate through each of the record and
download images based on arguments passed.

.. code:: json
    {
        "Records": [
            {
                "keywords": "apple",
                "limit": 5,
                "color": "green",
                "print_urls": true
            },
            {
                "keywords": "universe",
                "limit": 15,
                "size": "large",
                "print_urls": true
            }
        ]
    }


Mehrere Biespiele
=================

- If you are passing arguments from a config file, simply pass the config_file argument with name of your JSON file

.. code-block:: bash
    $ googleimagesdownload -cf example.json
- Simple example of using keywords and limit arguments

.. code-block:: bash




- Simple examples

``googleimagesdownload --keywords "Polar bears, baloons, Beaches" --limit 20``

-  Using Suffix Keywords allows you to specify words after the main
   keywords. For example if the ``keyword = car`` and
   ``suffix keyword = 'red,blue'`` then it will first search for
   ``car red`` and then ``car blue``

``googleimagesdownload --k "car" -sk 'red,blue,white' -l 10``

-  To use the short hand command

``googleimagesdownload -k "Polar bears, baloons, Beaches" -l 20``

-  To download images with specific image extension/format

``googleimagesdownload --keywords "logo" --format svg``

-  To use color filters for the images

``googleimagesdownload -k "playground" -l 20 -c red``

-  To use non-English keywords for image search

``googleimagesdownload -k "北极熊" -l 5``

-  To download images from the google images link

``googleimagesdownload -k "sample" -u <google images page URL>``

-  To save images in specific main directory (instead of in 'downloads')

``googleimagesdownload -k "boat" -o "boat_new"``

-  To download one single image with the image URL

``googleimagesdownload --keywords "baloons" --single_image <URL of the images>``

-  To download images with size and type constrains

``googleimagesdownload --keywords "baloons" --size medium --type animated``

-  To download images with specific usage rights

``googleimagesdownload --keywords "universe" --usage_rights labeled-for-reuse``

-  To download images with specific color type

``googleimagesdownload --keywords "flowers" --color_type black-and-white``

-  To download images with specific aspect ratio

``googleimagesdownload --keywords "universe" --aspect_ratio panoramic``

-  To download images which are similar to the image in the image URL that you provided (Reverse Image search).

``python3 pr.py -si <image url> -l 10``

-  To download images from specific website or domain name for a given keyword

``googleimagesdownload --keywords "universe" --specific_site example.com``

===> The images would be downloaded in their own sub-directories inside the main directory
(either the one you provided or in 'downloads') in the same folder you are in.

--------------
SSL Errors
----------

If you do see SSL errors on Mac for Python 3,
please go to Finder —> Applications —> Python 3 —> Click on the ‘Install Certificates.command’
and run the file.

--------------
Installing library errors
----------
 **## Permission denied while installing library **
On MAC and Linux, when you get permission denied when installing the library using pip, try doing a user install.
::
    $ pip install google_images_download --user

You can also run pip install as a superuser with ``sudo pip install google_images_download`` but it is not generally a good idea because it can cause issues with your system-level packages.

--------------
Structure
---------

Below diagram represents the code logic.

.. figure:: /img/flow-chart.png
    :alt:

--------------
Contribute
----------

Anyone is welcomed to contribute to this script.
If you would like to make a change, open a pull request.
For issues and discussion visit the
`Issue Tracker <https://github.com/hardikvasa/google-images-download/issues>`__

--------------
Disclaimer
----------

This program lets you download tons of images from Google.
Please do not download any image without violating its copyright terms.
Google Images is a search engine that merely indexes images and allows you to find them.
It does NOT produce its own images and, as such, it doesn't own copyright on any of them.
The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners,
even if they do not explicitly carry a copyright warning.
You may not reproduce copyright images without their owner's permission,
except in "fair use" cases,
or you could risk running into lawyer's warnings, cease-and-desist letters, and copyright suits.
Please be very careful before its usage!
