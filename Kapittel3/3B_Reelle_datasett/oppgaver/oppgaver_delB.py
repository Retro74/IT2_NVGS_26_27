from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)
#B1: Skriv ut alle bilmerker. 
#print(biler_df["Merke"].to_string())

#B2: Lag en liste av alle registeringsnumrene. Tips bruk metsoden to_list().
#regnr_liste = biler_df["Regnr"].to_list()
#print(regnr_liste)

#B3: Lag en DataFrame med Merke, Modell og Nåpris. 
#merke_modell_pris_df = biler_df[["Merke", "Modell", "Nåpris"]]
#print(merke_modell_pris_df)

#B4: Skriv ut merke og modell for de 10 første bilene (loc/iloc). 
print("10 første biler, Merke og Modell med loc:")
print(biler_df.loc[0:10,["Merke", "Modell"]])
print("\n10 første biler, Merke og Modell med iloc:")
print(biler_df.iloc[0:11, 0:2])