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

sns.lineplot(biler_df, x="Årsmodell", y="Nypris", color="green", errorbar=None)
plt.title("Utviklingen av gjennomsnittspris")
plt.xlabel("År")
plt.ylabel("Pris")
plt.grid()
plt.show()
