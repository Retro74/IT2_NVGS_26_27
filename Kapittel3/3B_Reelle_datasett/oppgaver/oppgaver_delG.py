from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#G1: Gjennomsnittlig Nåpris per merke. 
#print(round(biler_df.groupby("Merke")["Nåpris"].mean()))

#G2: Høyeste Nåpris per merke. 
#print(biler_df.groupby("Merke")["Nåpris"].max().sort_values(ascending=False))

#G3: Laveste Nåpris per merke. 
#print(biler_df.groupby("Merke")["Nåpris"].min().sort_values())

#G4: Antall biler per merke. 
#print(biler_df.groupby("Merke")["Regnr"].count().sort_values(ascending=False))

#G5: Hvor mange biler finnes det pr merke for årsmodellene 2024 og 2023.
print(biler_df
      .query("Årsmodell == 2024 or Årsmodell == 2023")
      .groupby(["Merke", "Årsmodell"])["Regnr"]
      .count())

#G6: Gjennomsnittlig Nåpris per Merke og Årsmodell. 
#print(round(biler_df.groupby(["Merke", "Årsmodell"])["Nåpris"].mean().sort_values()))