from pathlib import Path
import pandas as pd

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

#E1: Hvor mange biler finnes i datasettet? 
#E2: Hvor mange ulike bilmerker finnes? 
#E3: Hvor mange ulike modeller finnes? 
#print(
#    f"Vi har "
#    f"{biler_df['Merke'].nunique()} ulike merker, "
#    f"{biler_df['Modell'].nunique()} ulike modeller og "
#    f"{biler_df['Regnr'].nunique()} unike registreringsnummer."
#)

#E4: Finn høyeste, laveste og gjennomsnittlig Nåpris. 
#print("Dyreste bil:")
#print(biler_df[biler_df["Nåpris"]==biler_df["Nåpris"].max()])
#print("Billigste bil:")
#print(biler_df[biler_df["Nåpris"]==biler_df["Nåpris"].min()])
#print("Gjenommsnittspris bil:")
#print(biler_df["Nåpris"].mean())

#E5: Lag teksten ovenfor
print(f"""
    Vi har {biler_df['Regnr'].nunique()} registerte biler. 
    Vi har {biler_df['Merke'].nunique()} ulike merker, 
    {biler_df['Modell'].nunique()} ulike modeller, 
    gjennomsnittsprisen på bilene er: {round(biler_df["Nåpris"].mean())} kroner. 
    Vi har {biler_df[biler_df["Nåpris"]>500000]['Regnr'].nunique()} som koster over 500.000 kroner,
    {biler_df[biler_df["Årsmodell"]>2020]['Regnr'].nunique()} er nyere enn 2020, og gjenneomsnittsprisen for 
    disse er {round(biler_df[biler_df["Årsmodell"]>2020]['Nåpris'].mean())} kroner.  
    For eksmepel har vi {biler_df[biler_df["Merke"]>"Toyota"]['Regnr'].nunique()} Toyota. 
    Gjennomsnittsprisen for Toyota hos oss er {round(biler_df[biler_df["Merke"]>"Toyota"]['Nåpris'].mean())} kroner.
    Vi har {biler_df.query("Merke == 'Tesla' and Årsmodell==2024")['Regnr'].nunique()} Tesla fra 2024.
    Den dyreste bilen (-ene) er:\n{biler_df[biler_df["Nåpris"]==biler_df["Nåpris"].max()].to_string()}

""")