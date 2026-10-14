def bergn_salg(*priser):
    prisliste = list(priser)
    prisliste.sort()
    rabatt_indeks = len(prisliste)//3 
    print(f"Antall varer: {len(prisliste)}")
    #print(f"Bergner rabatt av:{prisliste[:rabatt_indeks]}")
    print(f"Rabatt: {sum(prisliste[:rabatt_indeks])} kroner")
    print(f"Rabatt: {round(sum(prisliste[:rabatt_indeks])*100/sum(prisliste))}%")
    #print(f"Bergner pris av:{prisliste[rabatt_indeks:]}")
    print(f"Pris: {sum(prisliste[rabatt_indeks:])} kroner.")

bergn_salg(199,235,139,499,349,129)