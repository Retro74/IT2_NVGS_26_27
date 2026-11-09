from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)
#A1: Skriv ut de 10 første og 10 siste radene (head(), tail()). 
#print(biler_df.head(10))

#A2: Finn antall rader og kolonner (shape). 
rader, kolonner = biler_df.shape
#print(f"Datasettet har {kolonner} kolonner.")
#print(f"Datasettet har {rader} rader.")

#A3: Skriv ut alle kolonnenavn (columns). 
#alleKolonneNavn = list(biler_df.columns)
#for nummer,  kolonneNavn in enumerate(alleKolonneNavn, start=1):
#    print(f"{nummer}. {kolonneNavn}")

#A4: Finn datatypene til kolonnene (dtypes/info()). 
#print("info():")
#biler_df.info()
#print("\ndtypes:")
#print(biler_df.dtypes)
#A5: Skriv ut slik:
alleKolonneNavn = list(biler_df.columns)
for kolonnenavn in alleKolonneNavn:
    match biler_df[kolonnenavn].dtypes:
        case "str":
            print(f"{kolonnenavn} er tekst")
        case "int64":
            print(f"{kolonnenavn} er et heltall")
        case "float":
            print(f"{kolonnenavn} er et desimaltall")
        case _:
            print(f"{kolonnenavn} er definert som {biler_df[kolonnenavn].dtypes}")
                  

