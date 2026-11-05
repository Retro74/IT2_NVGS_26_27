from pathlib import Path
import csv
#Åpne en tekstfil
filename = "elever.csv"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

#fileData = []
#with open(fullFilePathName, encoding="utf-8") as fil:
#    for linje in fil:
#        fileData.append(linje.strip().split(","))

#print("Data uten csv-reader:")
#print(fileData[0])
#print(fileData[1])
#print(fileData[2])

fileData = []
with open(fullFilePathName, encoding="utf-8") as fil:
    for linje in csv.reader(fil):
        fileData.append(linje)

print("\nData med csv-reader:")
print(fileData[0])
print(fileData[1])
print(fileData[2])

utFil = pyFilePath.joinpath("sekserelever.txt")

with open(utFil, "w", encoding="utf-8") as fil:
    for rad in fileData[1:]:
        if int(rad[-1]) == 6:
            fil.write(rad[0] + "\n")
