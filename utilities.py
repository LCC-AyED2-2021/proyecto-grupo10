from algo1 import concat
import os
from typing import List


def check_file_count(path):
    files = os.listdir(path)
    for names in files:
        print(names)
    file_count = len(files)
    print("La cantidad de archivos en la carpeta es " + str(file_count))

    return file_count

def get_files(pathDirectory):
    files = os.listdir(pathDirectory)
    return files


def line_to_line(pathFiles):
    f = open(pathFiles, encoding="utf8")
    lines = f.readlines()

    for line in lines:
        convertLineToWords(line)


def printWordsInEveryFile(path):
    print("Imprimiendo palabras")
    files = get_files(path)
    for file in files:
        line_to_line(file)


def convertLineToWords(Line):
    word = ''
    lentghL = len(Line)
    for i in range(0,lentghL):
        if Line[i] != '.' and Line[i] != ',' and Line[i] != ' ':
            word = word + Line[i]
        elif i<lentghL:
             if (Line[i] == '.' and Line[i+1] != ' ') or (Line[i] == ',' and Line[i+1] != ' '):
                 word = word + Line[i]
             if Line[i] == ' ':
                 ##insertamos la palabra
                 print(word)
                 word = ''


            


