from pathlib import Path
#import csv
import pandas as pd

#Åpne en tekstfil
#filename = "elever.csv"
#pyFilePath = Path(__file__).resolve().parent
#fullFilePathName = pyFilePath.joinpath(filename)

#fileData = []
#with open(fullFilePathName, encoding="utf-8") as fil:
#    for linje in csv.reader(fil):
#        fileData.append(linje)

#print("\nData med csv-reader:")
#print(fileData[0])
#print(fileData[1])
#print(fileData[2])


#df = pd.DataFrame(
#    fileData[1:],
#    columns=fileData[0]
#)
#print(df)
#print(df.dtypes)

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)
#print(biler_df)
#print(biler_df.dtypes)

#print(biler_df.head(20))
#print(biler_df.tail(6))
#print(biler_df.shape)
#print(list(biler_df.columns))
#biler_df.info()
#print(biler_df.describe())


# Filtere
#print(biler_df["Merke"].head())
#print(biler_df[["Merke", "Modell"]])

#print(biler_df.loc[0:3, ["Merke", "Modell"]])

#print(biler_df.iloc[0:3, 0:2])

#Filtrering på verdier
#print(biler_df)
#print(biler_df[biler_df["Merke"] =="Tesla"])
#print(biler_df.dtypes)
#print(biler_df[(biler_df["Merke"] =="Tesla") & (biler_df["Årsmodell"] > 2020)])
#print(biler_df[(biler_df["Modell"] =="Model 3") | (biler_df["Modell"] == "Model S")])

#Sjekke om en eller flere verdier finnes i df og bruke det til filtrering
#print(biler_df[(biler_df["Merke"] =="Tesla") | (biler_df["Merke"] == "Volvo")])
#tesla_volvo_df = biler_df[biler_df["Merke"].isin(["Tesla", "Volvo"])]

##Query Filtering
#nyTesla_df = biler_df.query("Merke == 'Tesla' and Årsmodell > 2022")
#print(nyTesla_df)

## Sortering
#bilder_sort_pris = biler_df.sort_values("Nåpris", ascending=False)
#print(bilder_sort_pris.head(10))

#biler_sort_merke = biler_df.sort_values(["Merke", "Modell", "Årsmodell"], ascending=[True, True, False])
#rint(biler_sort_merke.head(20))

#print(biler_df["Merke"].value_counts())
#print(list(biler_df["Merke"].unique()))

#print(biler_df.nunique())

## Gruppering

#print(biler_df.groupby("Merke")["Nåpris"].mean())
#print(biler_df.groupby("Merke")["Nåpris"].sum())
#print(biler_df.groupby("Merke")["Nåpris"].max())
#print(biler_df.groupby("Merke")["Nåpris"].min())
#print(biler_df.groupby("Merke")["Nåpris"].count())
#print(biler_df.groupby(["Merke", "Modell"])["Nåpris"].mean())

#Legge til kolonner i df

#from datetime import date
#biler_df["Alder"] = date.today().year - biler_df["Årsmodell"]
#print(biler_df)

#Kjede operasjon
#SELECT Merke, AVG(Nåpris) AS Gjennomsitt FROM biler WHERE Årsmodell > 2024 
# GROUP BY Merke ORDER BY Gjennomsitt DESC

resulat_df = (
    biler_df.query("Årsmodell > 2024")
            .groupby("Merke")["Nåpris"]
            .mean()
            .sort_values(ascending=False)
)
#print(resulat_df)

# a) Finn de tre dyreste bilene
# b) Ta ut et dataframe med biler av merke "Hyundai"
# c) Finnes det noen Jaguar-er i bildatabasen? Få ut True/False
# d) Finn alle biler som er eldre enn 10 år med nåpris under 80.000
# e) Finn alle biler som er nyere enn 2020 og koster under 300.000, 
# eller er nyere enn 2024 og koster under 350.00
# f) Lag en  liste over alle Volvo nyere enn 2022 sorter etter Nåpris
# g) Lag en kolonne "Verdifall" på hver bil som viser prosentvis verdifall for bilen
# g) Lag en kode som skriver ut teksten:
# "Vi har <antall merker> ulike merker, <antall unike modeller>, 
# gjennomsnittsprisen på bilene er: <gjenpmsnittpris> kroner. 
# Vi har <antall biler over 500.000> som koster over 500.000. 
# <antall biler nyere enn 2020> er nyere enn 2020, og gjenneomsnittsprisenn for 
# disse er <gjensomsnittspris for bilene nyere enn 2020>.  
# h) Group by
