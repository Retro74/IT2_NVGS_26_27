import matplotlib.pyplot as plt

dager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
temeraturer_uke44 = [12,14,12,16,18,20,14]

plt.plot(dager, temeraturer_uke44, color="green", linewidth=2, markersize=10, marker="o")
plt.title("Temperaturer uke 44")
plt.xlabel("Ukedager")
plt.ylabel("Temperatturer")
plt.grid()
plt.show()
