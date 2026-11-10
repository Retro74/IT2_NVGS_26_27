from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#H1: Hvilket merke har høyest gjennomsnittspris? 
#print(biler_df.groupby("Merke")["Nåpris"].mean().sort_values(ascending=False))

#H2: Hvilket merke har størst gjennomsnittlig verdifall?
#biler_df["VerdifallProsent"] = ((biler_df["Nypris"] - biler_df["Nåpris"])/ biler_df["Nypris"])
#print(biler_df.groupby("Merke")["VerdifallProsent"].mean().sort_values(ascending=False))

#H3: Finn billigste bil for hvert merke.
#print(biler_df.groupby("Merke")["Nåpris"].min().sort_values())

#H4: La brukeren kunne velge hvilke merker han vil se billigste bil av.
merker = input("Skriv inn hvilke merker du vil se billigste av (kommaseparert): ").split(",")
merker = [merke.strip() for merke in merker]

print(f"De billiste bilene for {", ".join(merker)} er: ")

print(biler_df.loc[
        biler_df
            .query(f"Merke in {merker}")
            .groupby("Merke")["Nåpris"]
            .idxmin()
            ]
      )


