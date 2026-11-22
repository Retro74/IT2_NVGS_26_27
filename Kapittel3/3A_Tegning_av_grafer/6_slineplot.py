import matplotlib.pyplot as plt
import seaborn as sns



dager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
temeraturer_uke44 = [12,14,12,16,18,20,14]
sns.set_theme()


sns.lineplot(x=dager, y=temeraturer_uke44, color="green")
plt.title("Temperaturer uke 44")
plt.xlabel("Ukedager")
plt.ylabel("Temperatturer")
plt.grid()
plt.show()
