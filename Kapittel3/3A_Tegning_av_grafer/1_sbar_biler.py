import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

filename = "biler_300.json"
pyFilePath = Path(__file__).resolve().parent
fullFilePathName = pyFilePath.joinpath(filename)

biler_df = pd.read_json(fullFilePathName)

sns.set_theme()
plt.figure(figsize=(10, 7))
sns.barplot(biler_df, x="Merke", y="Nypris")
plt.title("Gjennomsnittlig nypris på biler")
plt.xlabel("Merke")
plt.ylabel("Nypris")

plt.show()