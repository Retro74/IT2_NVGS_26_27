import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

spill = ["Fortnite", "Minecraft", "Roblox", "AmongUs", "Valorant"]
ant_spillere_mill =[350, 300, 220, 180, 150]
df = pd.DataFrame(zip(spill, ant_spillere_mill), columns=["Spill", "Ant. spillere i mill."])
game_colors = ["#7d3cff", "#ffdb58", "#ff6347", "#00cde1", "#ff4500"]

sns.set_theme()
soyler = sns.barplot(df, x="Spill", y="Ant. spillere i mill.", palette=game_colors)
#sns.b bar_label(soyler)
plt.title("Populære spill 2024")
plt.xlabel("Spill")
plt.ylabel("Antall spillere i mill.")

plt.show()