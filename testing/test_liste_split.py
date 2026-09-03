from  statistics import mean
uketemperaturer = input("Skriv inn temperaturer adskilt med komma: ")
temperatur_liste = uketemperaturer.split(",")
temperatur_liste = [int(temperatur) for temperatur in temperatur_liste]
print(f"Gjennomsnitt: {mean(temperatur_liste)}")