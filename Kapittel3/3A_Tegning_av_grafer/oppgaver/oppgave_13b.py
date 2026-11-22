import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

sns.set_theme()
merke_antall = biler_df["Merke"].value_counts()
merker_antall_andre = {"Andre": 0}
ant_biler = len(biler_df)
for merke, antall in merke_antall.items():
    if (antall*100)/ant_biler <6:
        merker_antall_andre["Andre"]+= antall
    else:
        merker_antall_andre[merke] = antall
    
plt.pie(merker_antall_andre.values(), labels=merker_antall_andre.keys() ,autopct="%1.0f%%")

plt.title("Bilmerkefordeling")
plt.show()
