from pathlib import Path

#Åpne en tekstfil
#filename = "test.txt"
#pyFilePath = Path(__file__).resolve().parent
#fullFilePathName = pyFilePath.joinpath(filename)
#
#fileData = []
#with open(fullFilePathName, encoding="utf-8") as fil:
#    for linje in fil:
#        fileData.append(linje.strip().split(" "))
#
#print(fileData)
##Lese inn fra en csv

import csv

filename = "elever.csv"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

fileData = []
with open(fullFilePathName, encoding="utf-8") as fil:
    for linje in csv.reader(fil):
        fileData.append(linje)


for i in range(1, len(fileData)):
    fileData[i][2] = int(fileData[i][2])
    fileData[i][3] = float(fileData[i][3])
    fileData[i][4] = int(fileData[i][4])

#print(fileData)

##Oppgaver
##a) Finne gjennomsnittskarakteren til alle elevene
tmp_karaktermatrise = []
for i in range(1, len(fileData)):
    tmp_karaktermatrise.append(fileData[i][-1])
print(f"Gjennomsnittskarakteren til alle elevene er: {sum(tmp_karaktermatrise)/len(tmp_karaktermatrise)}")

##b) Finne gjennomsnittskarakteren til alle elevene med IT2
tmp_karaktermatrise = []
for i in range(1, len(fileData)):
    if fileData[i][1]=="IT2":
        tmp_karaktermatrise.append(fileData[i][-1])
print(f"Gjennomsnittskarakteren til elevene med IT2 er: {sum(tmp_karaktermatrise)/len(tmp_karaktermatrise)}")

##c) Finne gjennomsnittskarakteren til alle elevene med IT2 i 2024
tmp_karaktermatrise = []
for i in range(1, len(fileData)):
    if fileData[i][1]=="IT2" and fileData[i][2]==2024 :
        tmp_karaktermatrise.append(fileData[i][-1])
print(f"Gjennomsnittskarakteren til elevene med IT2 i 2024 er: {sum(tmp_karaktermatrise)/len(tmp_karaktermatrise)}")

##c-2) Finn høyeste og laveste fraværsprosent
laveste = fileData[1][3]
hoyeste = fileData[1][3]
for i in range(2, len(fileData)):
    if fileData[i][3]> hoyeste:
         hoyeste = fileData[i][3]
    elif fileData[i][3]< laveste:
         laveste = fileData[i][3]

print(f"Laveste fraværsprosent er: {laveste}%, høyeste er {hoyeste}%.")

##d) Finn gjennomsnittlig fraværsprosent til elevene i IT1 og IT2, hvem har høyest?
fravaer ={"IT1":[], "IT2":[], "R1":[], "R2":[]}
for i in range(1, len(fileData)):
    fravaer[fileData[i][1]].append(fileData[i][3])
print(f"Fraværet i IT1 er i snitt: {round(sum(fravaer['IT1'])/len(fravaer['IT1']), 1)}% ,\n"
      f"i IT2 er fraværet: {round(sum(fravaer['IT2'])/len(fravaer['IT2']),1)}%.")

##e) Skriv ut en liste over gjennomsnittskarakterer for elever med fraværsprosenter
##   i intervaller på [0-1%>, [1-2%> osv
fravaersprosent_karakterer = {int(fravaerpros):[]  for fravaerpros in range(int(hoyeste)+1)}
for i in range(1, len(fileData)):
    fravaersprosent_karakterer[int(fileData[i][3])].append(fileData[i][4])
#print(fravaersprosent_karakterer)

print("Fraværsprosent | Karaktersnittnitt ")
for fraversprosent, karakterer in fravaersprosent_karakterer.items():
    if len(karakterer)>0:
        print(f" [ {fraversprosent}% - {fraversprosent+1}% >   "
              f"|     {round(sum(karakterer)/len(karakterer),1)}")
      
##f) Finn gjennomsnittlig fraværsprosent for de ulike karakterene 1-6
karakter_fravaer = {karakter:[] for karakter in range(1,7)}
for i in range(1, len(fileData)):
    karakter_fravaer[fileData[i][4]].append(fileData[i][3])

print("Karakter | Fraværssnitt  ")

for karakter, fraversprosenter in karakter_fravaer.items():
    if len(fraversprosenter)>0:
        print(f"   {karakter}     "
              f"|     {round(sum(fraversprosenter)/len(fraversprosenter),1)}%")
##g) Lag en frekvensntabell for hvor mange som fikkk de ulike karakterene 1-6
karakter_frekvens = {karakter:0 for karakter in range(1,7)}
for i in range(1, len(fileData)):
    karakter_frekvens[fileData[i][4]]+=1
#print(karakter_frekvens)
##h) Lag et enkelt tekstbasert diagram for resultene i g)

for karakter, frekvens in karakter_frekvens.items():
    print(f"{karakter}: {'#'*frekvens}")

