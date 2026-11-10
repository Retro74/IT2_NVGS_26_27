from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#Del F – Nye kolonner
#F1: Lag kolonnen Alder.
from datetime import date
biler_df["Alder"] = date.today().year - biler_df["Årsmodell"]
#print(biler_df)

#F2: Lag kolonnen Verdifall = Nypris - Nåpris. 
biler_df["Verdifall"] = biler_df["Nypris"] - biler_df["Nåpris"]   
#F3: Lag kolonnen VerdifallProsent. 
biler_df["VerdifallProsent"] = round(biler_df["Verdifall"]*100/biler_df["Nypris"], 2)
#F4: Finn bilen med størst prosentvis verdifall. 
print(biler_df[biler_df["VerdifallProsent"]==biler_df["VerdifallProsent"].max()])
#F5: Lag en kolonne som heter ÅrligVerdifallProsent

biler_df["ÅrligVerdifallProsent"] = round((((biler_df["Nåpris"]/biler_df["Nypris"])**(1/biler_df["Alder"]))-1)*(-100),3)
#print(biler_df)

#F6: Finn bilen med størst årlig prosentvis verdifall. 
print(biler_df[biler_df["ÅrligVerdifallProsent"]==biler_df["ÅrligVerdifallProsent"].max()])

#F7: 
print(biler_df[biler_df["ÅrligVerdifallProsent"]==biler_df["ÅrligVerdifallProsent"].min()])