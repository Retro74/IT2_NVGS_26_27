import matplotlib.pyplot as plt

spill = ["Fortnite", "Minecraft", "Roblox", "AmongUs", "Valorant"]
ant_spillere_mill =[350, 300, 220, 180, 150]
game_colors = ["#7d3cff", "#ffdb58", "#ff6347", "#00cde1", "#ff4500"]

soyler = plt.bar(spill, ant_spillere_mill, color=game_colors)
plt.bar_label(soyler)
plt.title("Populære spill 2024")
plt.xlabel("Spill")
plt.ylabel("Antall spillere i mill.")

plt.show()