#!/usr/bin/env python3

import os, shutil, glob
from os import chdir, makedirs
from subprocess import call

###### Settaggio delle variabili che contengono la Directory di Partenza e della Directory di Destinazione ######

## Estrae la Cartella su cui è eseguito il programma
path = os.getcwd()

## Variabile che definisce la Cartella su cui è eseguito lo scrpt
Script_SourceDir = path

## Variabili utilizzate per poter identificare quali cartelle devono essere riordinate
Scrivania_SourceDir = path + '/Scrivania'
Documenti_SourceDir = path + '/Documenti'
Scaricati_SourceDir = path + '/Scaricati'

## Variabile che definisce dove tutti i file verranno spostati e riordati
Script_DestinationDir = 'Andrea/'
