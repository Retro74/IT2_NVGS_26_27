from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

brukervalg = ["Merke", "Modell", "Årsmodell", "Nåpris"]
tmp_biler_df=biler_df

while True:
    print("Velg 0=quit):")
    for nr, valg in enumerate(brukervalg, start=1):
        print(nr, valg)
    brukerValgIndex = int(input(""))
    if brukerValgIndex == 0:
        break
    if brukervalg[brukerValgIndex-1] in ["Merke", "Modell"]:
        brukersokeverdi = input(f"Hvilke {brukervalg[brukerValgIndex-1]} ser du etter, skriv alle kommasepparert ").split(",")
        brukersokeverdi = [verdi.strip() for verdi in brukersokeverdi]
        print(f"{brukervalg[brukerValgIndex-1]} in {brukersokeverdi}")
        tmp_biler_df = tmp_biler_df.query(f"{brukervalg[brukerValgIndex-1]} in {brukersokeverdi}")
    else:
        brukervalgMin = input(f"Minsteverdi {brukervalg[brukerValgIndex-1]} ") 
        brukervalgMax = input(f"Maksverdi {brukervalg[brukerValgIndex-1]} ") 
        tmp_biler_df = tmp_biler_df.query(f"{brukervalg[brukerValgIndex-1]} >= {brukervalgMin} and {brukervalg[brukerValgIndex-1]} <= {brukervalgMax} ")
    brukervalg.pop(brukerValgIndex-1)


sortValues = ["Merke", "Modell", "Årsmodell", "Nåpris"]
for nr, valg in enumerate(sortValues, start=1):
    print(nr, valg)
brukerValgIndex = int(input(""))-1

print("Aktuelle modeller som passer søket ditt")
print(f"Søket ditt gav {len(tmp_biler_df)} treff, blandt {len(biler_df)} biler.")
print(tmp_biler_df.sort_values(sortValues[brukerValgIndex]))
