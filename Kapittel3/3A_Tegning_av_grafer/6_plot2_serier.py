import matplotlib.pyplot as plt

dager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
temeraturer_uke44 = [12,14,12,16,18,20,14]
temeraturer_uke45 = [10,12,10,15,15,18,13]

plt.plot(dager, temeraturer_uke44, color="green", label="Uke 44", linewidth=2, markersize=10, marker="o")
plt.plot(dager, temeraturer_uke45, color="red",  label="Uke 45", linewidth=2, markersize=10, marker="o")

plt.title("Temperaturer uke 44 og 45")
plt.xlabel("Ukedager")
plt.ylabel("Temperaturer")
plt.legend()
plt.grid()
plt.show()
