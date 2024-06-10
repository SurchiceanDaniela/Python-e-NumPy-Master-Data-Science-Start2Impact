#importo librerie
import os 
import shutil
import csv 
import sys
import argparse

def processo_file(filenome, path, filetipo):
    #divido il filenome ogni volta che trovo un punto utilizzando la funzione split
    nome = filenome.split(".")
    #recupero la dimensione del file utlizzando la funzione getsize di os
    dimensione = os.path.getsize("{}/{}".format(path,filenome))
    #creo una var testo che memorizza il nome senza l'estensione, il tipo e la dimensione del file
    testo = "{} tipo:{} dimensioni:{}B ".format(nome[0],filetipo, dimensione)
    #stampo testo con le informazioni
    print(testo)   
    if not os.path.exists(os.path.join(directory, "recap.csv")):  
        #se non esiste
        recap_file=open(os.path.join(directory, "recap.csv"), "w")
        #creo il file 'w' sta per write 
        scrittura = csv.writer(recap_file)
        #scrivo nel file name, type, size B utilizzando la funzione writerow
        scrittura.writerow(["name", "type", "size(B)"])
        scrittura.writerow([nome[0], "{}".format(filetipo), "{}".format(dimensione)])
    else:
        #apro recap        
        recap_file=open(os.path.join(directory, "recap.csv"), "a")
        #apre in file il append 
        #scrittura = csv.writer(recap_file)
        scrittura = csv.writer(recap_file)
        #scrivo nel file il nome senza l'estensione, il tipo e la dimensione del file utilizzando la funzione writerow
        scrittura.writerow([nome[0], "{}".format(filetipo), "{}".format(dimensione)])
    recap_file.close()
        
    #se non c'è la cartella la crea
    if not os.path.isdir("{}/{}".format(path, filetipo)): 
        os.mkdir("{}/{}".format(path, filetipo))
    #sposto il file utilizzando la funzione move
    shutil.move("{}/{}".format(path, filenome), "{}/{}".format(path, filetipo))


filenome = sys.argv[1]
directory = "files"
#dizionario estensioni files
extension_files = {
        '.jpeg': 'images',
        '.jpg': 'images',
        '.png': 'images',
        '.txt': 'docs',
        '.odt': 'docs',
        '.mp3': 'audio'
}
if not os.path.isfile(os.path.join(directory, filenome)):
    #se non esiste stampo errore
    print("ERROR! {} does not exist".format(filenome))
else:
        #separo nome file da estensione
         
        name, ext = os.path.splitext(filenome)
        if ext in extension_files:
            path_file = extension_files[ext]
            processo_file(filenome, directory, path_file)
        else:
            print(filenome +" Errore: Estensione non supportata!")

