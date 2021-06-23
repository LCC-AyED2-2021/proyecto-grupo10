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
    


def insertWordsHash(path):
    files = os.listdir(path)
    for file in files:
        f = open(file, encoding="utf8")
        lines = f.readlines()
        for line in lines:
            word = ''
            lentghL = len(line)
            for i in range(0,lentghL):
                 if line[i] != '.' and line[i] != ',' and line[i] != ' ':
                    word = word + line[i]
                 elif i<lentghL:
                    if (line[i] == '.' and line[i+1] != ' ') or (line[i] == ',' and line[i+1] != ' '):
                        word = word + line[i]
                    if line[i] == ' ':
                        print(word)
                        word = ''
            
        


    


            


