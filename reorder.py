#!/usr/bin/env python3

# Inport dei comandi di sistema (Terminale Linux)

import os, shutil, glob
from os import chdir, makedirs
from subprocess import call

#Funzione Main Principale
def Reorder(Stato):

    #Settaggio delle variabili che contengono la Directory di Partenza e della Directory di Destinazione
    from config import Script_SourceDir
    from config import Script_DestinationDir
    SourceDir = Script_SourceDir
    DestinationDir = Script_DestinationDir

    #Controllo che verifica e crea le sotto-cartelle necessarie
    if os.path.isdir(DestinationDir + 'Documents') == False:
        os.makedirs(DestinationDir + 'Documents')
    if os.path.isdir(DestinationDir + 'Projects') == False:
        os.makedirs(DestinationDir + 'Projects')
    if os.path.isdir(DestinationDir + 'Images') == False:
        os.makedirs(DestinationDir + 'Images')
    if os.path.isdir(DestinationDir + 'Videos') == False:
        os.makedirs(DestinationDir + 'Videos')

    #Call delle funzioni di Ordinamento
    if (Stato == 1):
        Reorder_Scrivania()
    elif (Stato == 2):
        Reorder_Documenti()
    elif (Stato == 3):
        Reorder_Scaricati()
    else:
        print("[--- Riordinamento Completato ---]")

#Funzione che controllo e riordina tutti i file sparsi contenuti nella Directory Scrivania
def Reorder_Scrivania():

    #Settaggio delle variabili che contengono la Directory di Partenza e della Directory di Destinazione
    from config import Scrivania_SourceDir
    from config import Script_DestinationDir
    SourceDir = Scrivania_SourceDir
    DestinationDir = Script_DestinationDir

    #Lista che contiene i file che dovranno essere spostati
    extensions = [SourceDir + "**/*.txt", SourceDir + "**/*.py", SourceDir + "**/*.bash", SourceDir + "**/*.sh", SourceDir + "**/*.html", SourceDir + "**/*.css", SourceDir + "**/*.php", SourceDir + "**/*.png", SourceDir + "**/*.jpg", SourceDir + "**/*.jpeg", SourceDir + "**/*.mp4", SourceDir + "**/*.avi", SourceDir + "**/*.mkv"]
    files = []
    for x in extensions:
        files.extend(glob.glob(x))

    #Lista che contiene tutte le cartelle che dovranno essere spostate


    #Ciclo For che sposta i file
    for element in files:
        if element.endswith('.txt'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.png'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.html'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.php'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.css'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.py'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.bash'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.sh'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.mp4'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.avi'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.mkv'):
            shutil.move(element, DestinationDir + 'Videos')
        else:
            shutil.move(element, DestinationDir)

    #Ritorno al Main con variabile Stato impostata a 2
    Reorder(2)

#Funzione che controllo e riordina tutti i file sparsi contenuti nella Directory Documenti
def Reorder_Documenti():

    #Settaggio delle variabili che contengono la Directory di Partenza e della Directory di Destinazione
    from config import Documenti_SourceDir
    from config import Script_DestinationDir
    SourceDir = Documenti_SourceDir
    DestinationDir = Script_DestinationDir

    #Lista che contiene i file che dovranno essere spostati
    extensions = [SourceDir + "**/*.txt", SourceDir + "**/*.py", SourceDir + "**/*.bash", SourceDir + "**/*.sh", SourceDir + "**/*.html", SourceDir + "**/*.css", SourceDir + "**/*.php", SourceDir + "**/*.png", SourceDir + "**/*.jpg", SourceDir + "**/*.jpeg", SourceDir + "**/*.mp4", SourceDir + "**/*.avi", SourceDir + "**/*.mkv"]
    files = []
    for x in extensions:
        files.extend(glob.glob(x))

    #Lista che contiene tutte le cartelle che dovranno essere spostate


    #Ciclo For che sposta i file
    for element in files:
        if element.endswith('.txt'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.png'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.html'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.php'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.css'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.py'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.bash'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.sh'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.mp4'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.avi'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.mkv'):
            shutil.move(element, DestinationDir + 'Videos')
        else:
            shutil.move(element, DestinationDir)

    #Ritorno al Main con variabile Stato impostata a 3
    Reorder(3)

#Funzione che controllo e riordina tutti i file sparsi contenuti nella Directory Scaricati
def Reorder_Scaricati():

    #Settaggio delle variabili che contengono la Directory di Partenza e della Directory di Destinazione
    from config import Scaricati_SourceDir
    from config import Script_DestinationDir
    SourceDir = Scaricati_SourceDir
    DestinationDir = Script_DestinationDir

    #Lista che contiene i file che dovranno essere spostati
    extensions = [SourceDir + "**/*.txt", SourceDir + "**/*.py", SourceDir + "**/*.bash", SourceDir + "**/*.sh", SourceDir + "**/*.html", SourceDir + "**/*.css", SourceDir + "**/*.php", SourceDir + "**/*.png", SourceDir + "**/*.jpg", SourceDir + "**/*.jpeg", SourceDir + "**/*.mp4", SourceDir + "**/*.avi", SourceDir + "**/*.mkv"]
    files = []
    for x in extensions:
        files.extend(glob.glob(x))

    #Lista che contiene tutte le cartelle che dovranno essere spostate


    #Ciclo For che sposta i file
    for element in files:
        if element.endswith('.txt'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.png'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('jpg'):
            shutil.move(element, DestinationDir + 'Images')
        elif element.endswith('.html'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.php'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.css'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.py'):
            shutil.move(element, DestinationDir + 'Projects')
        elif element.endswith('.bash'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.sh'):
            shutil.move(element, DestinationDir + 'Documents')
        elif element.endswith('.mp4'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.avi'):
            shutil.move(element, DestinationDir + 'Videos')
        elif element.endswith('.mkv'):
            shutil.move(element, DestinationDir + 'Videos')
        else:
            shutil.move(element, DestinationDir)

    #Ritorno al Main con variabile Stato impostata a 4
    Reorder(4)

#Call del Main per la prima volta con variabile Stato impostata a 1
Reorder(1)
