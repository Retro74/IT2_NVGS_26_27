import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)


sns.set_theme()
plt.figure(figsize=(8,5))

rekkefolge = biler_df.groupby("Merke")["Nåpris"].mean().sort_values().index
soyle = sns.barplot(biler_df, x="Merke", y="Nåpris", 
                    color="blue", errorbar=None, 
                    order=rekkefolge[::-1])

etiketter = [f"{round(s.get_height()/1000)}'" for s in soyle.containers[0]]

plt.bar_label(soyle.containers[0], labels=etiketter)
plt.title("Utviklingen av gjennomsnittspris")
plt.xlabel("År")
plt.ylabel("Pris")
plt.grid()
plt.show()
