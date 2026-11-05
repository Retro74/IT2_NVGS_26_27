from pathlib import Path
import csv
import pandas as pd

#Åpne en tekstfil
filename = "elever.csv"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

fileData = []
with open(fullFilePathName, encoding="utf-8") as fil:
    for linje in csv.reader(fil):
        fileData.append(linje)

#print("\nData med csv-reader:")
#print(fileData[0])
#print(fileData[1])
#print(fileData[2])


df = pd.DataFrame(
    fileData[1:],
    columns=fileData[0]
)
print(df)
