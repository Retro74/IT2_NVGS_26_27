from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#C1: Finn alle Hyundai. 
# hyundai_df = biler_df[biler_df["Merke"]=="Hyundai"]    #1
#hyundai_df = biler_df.query('Merke == "Hyundai"')       #2
#print(hyundai_df.to_string())

#C2: Finn alle Tesla nyere enn 2023. 
#nyeTesla_df = biler_df.query("Merke=='Tesla' and Årsmodell > 2023")
#print(nyeTesla_df.to_string())

#C3: Finn alle Tesla nyere enn 2023 som koster under 500.000. 
#nyeTesla_df = biler_df.query("Merke=='Tesla' and Årsmodell > 2023 and Nåpris < 500000")
#print(nyeTesla_df.to_string())

#C4: Finn alle Tesla, Volvo eller Audi (isin()). 
#print(biler_df[biler_df["Merke"].isin(["Tesla", "Volvo", "Audi"])].to_string())        #1
#print(biler_df.query("Merke=='Tesla' or Merke=='Volvo' or Merke=='Audi'").to_string()) #2

#C5: Bruk metoden any() etter isin() for å få svar på om det finnes noen Jagurarer i lista
#if biler_df["Merke"].isin(["Jaguar"]).any():
#    print("Ja, Jaguar er i lista")
#else:
#    print("Nei, Jaguar er ikke i lista")

#C4: Finn alle biler under 100 000 kr. 
#print(biler_df.query("Nåpris < 100_000").to_string())
#print(f'Det finnes {len(biler_df.query("Nåpris < 100_000"))} biler under 100.000 kroner')
#C7: Finn alle biler under Toyota under 100 000 kr
#print(f'Det finnes {len(biler_df.query("Nåpris < 100_000 and Merke == 'Toyota'"))} Toyota under 100.000 kroner')

#C8: Finn alle biler eldre enn 10 år med nåpris under 80 000. 
#from datetime import date
#aarstall = date.today().year-10
#print(f'Det finnes {len(biler_df.query("Årsmodell > @aarstall and Nåpris < 140000"))} biler som er under 10 år og koster under 140.000 kroner')

#C9: Finn biler nyere enn 2020 under 300 000 eller nyere enn 2024 under 350 000. 
kritterie_df = biler_df.query("(Årsmodell>2020 and Nåpris<300000) or (Årsmodell>2024 and Nåpris<350000)")
print(f"Det finnes {len(kritterie_df)} biler som fyller kritteriene. \nDette er:")
print(kritterie_df.to_string())
