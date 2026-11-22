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
soyle = sns.countplot(biler_df, x="Merke", color="green")
plt.bar_label(soyle.containers[0])
plt.title("Antall biler")
plt.xlabel("Merke")
plt.ylabel("Antall")
plt.grid()
plt.show()
