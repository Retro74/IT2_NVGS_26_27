import matplotlib.pyplot as plt

sportsgrener = ["Fotball", "Basketball", "E-sport", "Svømming", "Ski"]
antall_utovere = [117, 45, 33, 21, 15]

plt.pie(antall_utovere, labels=sportsgrener, autopct='%1.1f%%', startangle=90)
plt.title("Fritidsintressser blandt ungdom")
plt.show()