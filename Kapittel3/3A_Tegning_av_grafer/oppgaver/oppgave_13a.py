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
plt.pie(merke_antall.values, labels=merke_antall.index, autopct="%1.0f%%")

plt.title("Bilmerkefordeling")
plt.show()
