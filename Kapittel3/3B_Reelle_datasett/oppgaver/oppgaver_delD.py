from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#D1: Finn de tre dyreste bilene. 
#print("De tre dyreste bilene er:")
#print(biler_df.sort_values("Nåpris", ascending=False).head(3))

#D2: Sorter alle biler etter Nåpris synkende. 
#print(biler_df.sort_values("Nåpris", ascending=False).to_string())
#D3: Sorter etter Merke, Modell og Årsmodell. 
#print(biler_df.sort_values(["Merke","Modell", "Årsmodell"], ascending=[True, True, False]).to_string())
#D4: Lag en liste over alle Volvo nyere enn 2022 sortert etter Nåpris. 
kritterier_df=biler_df.query("Merke=='Volvo' and Årsmodell > 2022").sort_values(["Nåpris"], ascending=False)
print(f"Det finnes {len(kritterier_df)} biler for dette søket. \nDette er:")
print(kritterier_df.to_string())