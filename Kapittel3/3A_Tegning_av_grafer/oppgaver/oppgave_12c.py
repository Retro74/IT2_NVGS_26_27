import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

plt.figure(figsize=(8,5))
sns.set_theme()

# Teller antall biler av hvert merke (pandas dataSerie)
merke_antall_ds = biler_df["Merke"].value_counts().sort_index()

for merke, ant in merke_antall_ds.items():
    plt.bar(merke, ant,
        color = "red" if ant < 10 else
                "orange" if ant < 20 else
                "green" if ant < 41 else
                "orange" if ant < 50 else
                "red"
    )
    plt.text(merke,ant,ant,ha="center",va="bottom")

plt.title("Antall biler")
plt.xlabel("Merke")
plt.ylabel("Antall")

plt.grid()
plt.show()
